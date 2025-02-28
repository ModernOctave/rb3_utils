from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    view = LaunchConfiguration('view')
    
    view_launch_arg = DeclareLaunchArgument(
        'view',
        default_value='false',
        description='Whether to also display the camera feed in a window using the `camera_viewer` node.'
    )

    camera_node = Node(
        package='gscam',
        executable='gscam_node',
        name='rb_camera_tracking',
        output='screen',
        parameters=[{
            "camera_name": "camera_tracking",
            "camera_info_url": "package://gscam/examples/uncalibrated_parameters.ini",
            "gscam_config": "qtiqmmfsrc camera=1 ! video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 ! videoconvert",
            "use_gst_timestamps": True,
            "frame_id": "/camera_tracking",
            "sync_sink": False,
        }],
        arguments=[{'use_intra_process_comms': True}],
        remappings=[
            ('/camera/image_raw', '/camera_tracking/image_raw'),
            ('/camera/camera_info', '/camera_tracking/camera_info'),
        ]
    )

    # Define the camera viewer node
    camera_viewer_node = Node(
        package='rb3_utils',
        executable='camera_viewer',
        name='camera_viewer',
        output='screen',
        parameters=[{
            "image_topic": "/camera_tracking/image_raw"
        }],
        condition=IfCondition(view)
    )

    return LaunchDescription([
        view_launch_arg,
        camera_node,
        camera_viewer_node
    ])