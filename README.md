# rb3_utils
This package contains a set of utilities for the Qualcomm RB3 platform.

> [!WARNING]
> Subscribing to the `/camera_*/image_raw` topic over the network (from a system other than the RB3) using a node or RVIZ2 will cause the RB3 to crash. This is due to the RB3 not being able to handle the network traffic. To visualize the camera feed connect a monitor to the RB3 and use the `camera_viewer` node or use the `camera_main_launch.py` and `camera_tracking_launch.py` launch files with the `view` argument set to `true`.

## Launch files
### camera_main_launch.py
This launch file launches a gscam node which publishes the RB3 main camera feed to the `/camera_main/image_raw` topic.
#### Arguments
- `view` (`bool`, default: "false"): Whether to also display the camera feed in a window using the `camera_viewer` node.

### camera_tracking_launch.py
This launch file launches a gscam node which publishes the RB3 tracking camera feed to the `/camera_tracking/image_raw` topic.
#### Arguments
- `view` (`bool`, default: "false"): Whether to also display the camera feed in a window using the `camera_viewer` node.

## Nodes
### camera_viewer
This node subscribes to a camera topic and displays the images in a window using OpenCV.
#### Parameters
- `image_topic` (`string`, default: "/camera/image_raw"): The topic name of the camera to subscribe to.

## References
- [Using ROS2 with the Qualcomm RB5](https://gist.github.com/stephendade/277f4d3d02bff565f393306c06ef570f)
- [qtiqmmfsrc - Qualcomm Docs](https://docs.qualcomm.com/bundle/publicresource/topics/80-70014-50/qtiqmmfsrc.html)
