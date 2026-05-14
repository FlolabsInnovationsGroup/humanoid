import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription, SetEnvironmentVariable, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('ros_workspace')
    world_path = os.path.join(pkg_share, 'worlds', 'office_world.sdf')
    models_path = os.path.join(pkg_share, 'models')
    urdf_file = os.path.join(pkg_share, 'models', 'robot', 'model.urdf.xacro')

    doc = xacro.process_file(urdf_file)
    robot_description_content = doc.toxml()

    set_gz_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=[models_path]
    )

    gz_sim_launch = ExecuteProcess(
        cmd=['gz', 'sim', '-r', world_path],
        output='screen'
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_content}]
    )

    # Write the merged URDF so Gazebo can spawn it via gz service.
    _URDF_TMP = '/tmp/desktop_mini_robot_sim.urdf'
    with open(_URDF_TMP, 'w') as f:
        f.write(robot_description_content)

    spawn_robot = TimerAction(
        period=20.0,
        actions=[ExecuteProcess(
            cmd=[
                'gz', 'service',
                '-s', '/world/Office/create',
                '--reqtype', 'gz.msgs.EntityFactory',
                '--reptype', 'gz.msgs.Boolean',
                '--timeout', '5000',
                '--req',
                (
                    f'name: "desktop_mini_robot" '
                    f'sdf_filename: "{_URDF_TMP}" '
                    f'pose {{ position {{ x: 0.2 y: 0 z: 0.85 }} '
                    f'orientation {{ w: 1 }} }}'
                ),
            ],
            output='screen',
        )]
    )

    ros_gz_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='ros_gz_bridge',
        output='screen',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model',
            '/ir_sensor/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
        ]
    )

    return LaunchDescription([
        set_gz_resource_path,
        gz_sim_launch,
        robot_state_publisher,
        spawn_robot,
        ros_gz_bridge,
    ])