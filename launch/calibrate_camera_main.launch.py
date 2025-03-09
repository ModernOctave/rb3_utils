from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():
    camera_main_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('rb3_utils'),
                    'launch',
                    'camera_main.launch.py'
                ])
            ),
        )
    
    camera_calibration_node = Node(
        package='camera_calibration',
        executable='cameracalibrator',
        name='camera_calibration',
        output='screen',
        arguments=['--size', '8x6', '--square', '0.025'],
        remappings=[
            ('image', 'camera_main/image_raw'),
            ('camera', 'camera_main'),
            ('camera/set_camera_info', 'camera_main/set_camera_info')
        ],
        
    )

    return LaunchDescription([
        camera_main_launch,
        camera_calibration_node,
    ])