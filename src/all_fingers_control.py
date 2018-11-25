#!/usr/bin/env python
#This code is written by Mostafa Atalla to automate the control of the UbiRos Gentle Pro Soft gripper
#


import rospy
import time
import sys, select, termios, tty
from std_msgs.msg import UInt16



msg = """
Press w to close all of the fingers by increment 5%
Press s to open all of the fingers by increment 5%
Press a to close all of the fingers once at a time.
Press z to open all of the fingers once at a time.

"""

#getkey function is for detecting the key entered through the keyboard
def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


#This if statement is making sure that this is the node that is called directly by the user
if __name__=="__main__":

    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('all_fingers_control')
    pub = rospy.Publisher('UbirosGentlePro', UInt16, queue_size = 1)

#Initiation of variables
    p_increment=5
    n_increment=-5
    all_fingers=0
    all_fingers_old=0
    status = 0


    print(msg)

#The main while loop the keeps the code running until the user closes it and it takes actions based on the key pressed
    while(1):
        key = getKey()
        if (key == '\x03'):
            break

        elif (key == 'w'):
            if (all_fingers < 100):

                all_fingers=p_increment+all_fingers_old
                pub.publish(all_fingers)
                print 'Current close percentage is', all_fingers, '%'

            else:
                print('Max Storke has been acheived')
            status = (status + 1) % 15

        elif (key=='s'):
            if (all_fingers > 0):
                all_fingers=n_increment+all_fingers_old
                pub.publish(all_fingers)
                print 'Current close percentage is',all_fingers, '%'

            else:
                print('Min Storke has been acheived')
            status = (status + 1) % 15

        elif (key == 'a'):
            for i in range(all_fingers_old,101):
                all_fingers=i
                pub.publish(all_fingers)
                time.sleep(0.01)
                print 'Current close percentage is', all_fingers, '%'
            print(msg)

        elif (key == 'z'):
            for i in range(all_fingers_old,-1,-1):
                all_fingers=i
                pub.publish(all_fingers)
                time.sleep(0.01)
                print 'Current close percentage is', all_fingers, '%'
            print(msg)

        else:
            print('Enter the proper key')
            status = (status + 1) % 15

        if (status == 10):
            print(msg)



        all_fingers_old=all_fingers

#This two lines are executed once the user exits the code, they return the fingers back to 10% position.
    all_fingers=10
    pub.publish(all_fingers)

