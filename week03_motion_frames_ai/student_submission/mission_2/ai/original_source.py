import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PointStamped
import tf2_ros
from tf2_geometry_msgs import do_transform_point


class CameraPointTransformer(Node):

    def __init__(self):
        super().__init__('camera_point_transformer')

        # TF2 buffer/listener
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(
            self.tf_buffer, self
        )

        # Point detected by the hallway camera
        self.subscription = self.create_subscription(
            PointStamped,
            '/hallway_camera/point',
            self.point_callback,
            10
        )

        # Transformed point in base_link
        self.publisher = self.create_publisher(
            PointStamped,
            '/point_base_link',
            10
        )

    def point_callback(self, point_camera):
        try:
            # Get transform from camera frame -> base_link
            transform = self.tf_buffer.lookup_transform(
                'base_link',
                point_camera.header.frame_id,
                rclpy.time.Time()
            )

            # Transform the point
            point_base = do_transform_point(
                point_camera,
                transform
            )

            self.publisher.publish(point_base)

            self.get_logger().info(
                f'Point in base_link: '
                f'x={point_base.point.x:.2f}, '
                f'y={point_base.point.y:.2f}, '
                f'z={point_base.point.z:.2f}'
            )

        except tf2_ros.TransformException as ex:
            self.get_logger().warn(
                f'Could not transform point: {ex}'
            )


def main(args=None):
    rclpy.init(args=args)

    node = CameraPointTransformer()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()