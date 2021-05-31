#!/usr/bin/python3

import rospy
from  geometry_msgs.msg import Twist 
import cv2 as cv
class KeyboardTeleop:
    def _init_(self):
        rospy.init_node('keyboard_teleop')
        self.sub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)
        self.msg = Twist()
    
        k = cv.waitKey(1)

        if k == ord('w'):
            self.msg.linear.x = 0.2
            self.msg.angular.x = 0
        elif k == ord('s'):
            self.msg.linear.x = -0.2
            self.msg.angular.x = 0    
        elif k == ord('d'):
            self.msg.linear.x = 0.2
            self.msg.angular.x = -0.3 
        elif k == ord('a'):
            self.msg.linear.x = 0.2
            self.msg.angular.x = 0.3         
        elif k == ord('q'): 
            rospy.signal_shutdown("shutdown")  
            cv.destroyAllwindows()  
        else:
            self.msg.linear.x = 0
            self.msg.angular.x = 0    
        self.pub.pulish(self.msg)    
        self.rate.sleep()
if __name__== '_main_':
    kt = KeyboardTeleop()
  
      
  