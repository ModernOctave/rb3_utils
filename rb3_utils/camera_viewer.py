import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraViewer(Node):
    def __init__(self):
        super().__init__('camera_viewer')
        self.bridge = CvBridge()
        self.declare_parameter('image_topic', '/camera/image_raw')
        self.image_topic = self.get_parameter('image_topic').value
        self.subscription = self.create_subscription(Image, self.image_topic, self.image_callback, 0)
        cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Camera Feed", 1280, 720)

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        cv2.imshow("Camera Feed", frame)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)

    node = CameraViewer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

