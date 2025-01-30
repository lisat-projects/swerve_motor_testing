'''import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray
from std_msgs.msg import String'''
import can

# represents 1 motor
class SwerveSubscriber(Node):

    # creating new instance
    def __init__(self):
        super().__init__('swerve_motor')
        self.subscription = self.create_subscription(
            Int32MultiArray,
            'swerve',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'can_msg', 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        data = float(msg.data)
        # TODO: Make this more abstract for actual control
        if data == 4.0:
            can_msg = String()
            # 74 = vesc id of the thing to send to
            # CAN_PACKET_SET_CURRENT = command
            # 4 = value, int = type
            can_msg.data = "74 CAN_PACKET_SET_CURRENT 4 int"
            self.publisher_.publish(can_msg)

def main(args=None):
    rclpy.init(args=args)

    swerve_subscriber = SwerveSubscriber()

    rclpy.spin(swerve_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    swerve_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

