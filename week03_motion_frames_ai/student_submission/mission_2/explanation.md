# Mission 2

## Snapshot

{'schema_version': 2, 'captured_at': '2026-09-25T07:08:41.119414+00:00', 'frames': ['odom', 'base_link', 'base_scan', 'rear_camera_link', 'hall_camera'], 'frame_chain': ['hall_camera', 'odom', 'base_link', 'base_scan', 'rear_camera_link'], 'transforms': {'base_scan_to_base_link': {'translation': {'x': -0.032, 'y': 0.0, 'z': 0.172}, 'yaw': 0.0}, 'rear_camera_to_base_link': {'translation': {'x': -0.18, 'y': 0.0, 'z': 0.22}, 'yaw': -3.1415926535795866}, 'hall_camera_to_base_link': {'translation': {'x': -9.599863627443788e-09, 'y': -2.0, 'z': 1.19}, 'yaw': 1.5707963268004614}}, 'point_prompts': {'hall_camera_point': 'Transform point (0.5, 0.0, 0.0) from hall_camera to base_link.'}, 'transformed_points': {'scan_point_in_base': {'x': 0.968, 'y': 0.0}, 'rear_camera_point_in_base': {'x': -1.18, 'y': -1.0206624774663903e-11}, 'hall_camera_point_in_base': {'x': -9.602646037771933e-09, 'y': -1.5}}, 'source': 'live'}

## Frame Context

The rear-camera transform stays fixed because as the robot moves the rear camera's position is always going to stay the same relative to the robot as it's moving with the robot, however with the hallway-camera-to-base_link as the robot moves, the base_link moves which changes the relationship between the hallway-camera because the hallway-camera is not moving and its being compared to a camera that is moving either further or closer.

## Initial Prompt

Write ROS 2 Python code that converts a point detected by the hallway camera into the robot's base_link frame.

## Initial Output

If your hallway camera publishes the detected point as a geometry_msgs/PointStamped, the usual ROS 2 approach is to use TF2 to transform that point from the camera's frame into base_link.

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
What is happening

Suppose the camera detects:

frame_id = "hallway_camera"
x = 2.0
y = 0.5
z = 1.0

The important line is:

transform = self.tf_buffer.lookup_transform(
    'base_link',
    point_camera.header.frame_id,
    rclpy.time.Time()
)

This asks TF2:

"How do I transform coordinates from the camera's frame into base_link?"

Then:

point_base = do_transform_point(point_camera, transform)

actually performs the coordinate conversion.

The resulting message will have:

frame_id = "base_link"

and its x, y, and z values will represent the same physical point relative to the robot's base.

The important requirement is that TF2 must know the relationship between the camera frame and base_link, for example:

base_link
    |
    └── hallway_camera

Usually that transform comes from your robot's URDF/TF system.

## Initial Source

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

## Initial Analysis

It assumes that the points are published as PointStamped in geometry_msgs by the hallway camera, It seems also when the Node gets initialized it assumes that there's already a point thats been detect by the hallway camera?  (Not sure about this one) Queue Sizes for the subscription and publishers are hard set to 10, there are scenarios where we may want more or less. The topic name /hallway_camera/point also seems like a hardcoded path when it could be something very different. 

## Improved Changes

The prompt above forces points that take check if the frame_id is hall_camera otherwise it raises an error, stop them from using any hard coded offsets and does not allow them to create any new publishers so it's containing the code without creating new nodes.

## Live Pending

True

## Synthesis

The initial AI output assumed that it could create its own publishers and subscribers but the improved prompt forced it so that it could not create any publishers. If the wrong transformations were used people could get hurt or trip over the robot, The guard or in this case the transformation would usually detect that problem by seeing if it transforms properly and if it doesnt to raise an error or return nothing, if the transform data is unavailable the robot should just not move at all and stay still.

## Live Issue

Ran into a couple of errors where it tried using attributes that didn't exist, i told the AI about these issues and they fixed the code to the point where the unit tests managed to pass but the live and live_passed both seem to have failed.
