#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import LaserScan

# TODO: import ROS msg types and libraries
import rospy
from ackermann_msgs.msg import AckermannDriveStamped, AckermannDrive

class PurePursuit(object):
    """
    The class that handles pure pursuit.
    """
    def __init__(self):
        # TODO: create ROS subscribers and publishers.
	lidarscan_topic = '/scan'
        drive_topic = '/vesc/high_level/ackermann_cmd_mux/input/nav_2'

        #self.lidar_sub = rospy.Subscriber(lidarscan_topic, LaserScan, self.lidar_callback)
        self.drive_pub = rospy.Publisher(drive_topic, AckermannDriveStamped, queue_size = 10)

    def pose_callback(self, pose_msg):
        # TODO: find the current waypoint to track using methods mentioned in lecture
	lookahead_dist = 1.5

        # TODO: transform goal point to vehicle frame of reference

        # TODO: calculate curvature/steering angle
	steering_angle = None

        # TODO: publish drive message, don't forget to limit the steering angle between -0.4189 and 0.4189 radians
	drive_msg = AckermannDriveStamped()
	drive_msg.drive.steering_angle = steering_angle
	self.drive_pub.publish(drive_msg)


def main():
    rospy.init_node('pure_pursuit_node')
    pp = PurePursuit()
    rospy.spin()
if __name__ == '__main__':
    main()
