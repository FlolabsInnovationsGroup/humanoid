import os
import xacro
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    package_name = 'ros_workspace'
    
    urdf_file = os.path.join(get_package_share_directory(package_name), 'models', 'robot', 'model.urdf.xacro')
    rviz_config = os.path.join(get_package_share_directory(package_name), 'config', 'robot_view.rviz')

    doc = xacro.process_file(urdf_file)
    robot_description_content = doc.toxml()

    return LaunchDescription([
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        ),  

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description_content}]
        ),
        
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            parameters=[{'robot_description': robot_description_content}]
        )
    ])