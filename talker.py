print ("talker.py")

from ast import Str
from numpy import rate
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) #10hz
    while not rospy.is_shutdown():
        hello_str = "María Belén Lezcano Villalba%s"
rospy.get_time()
rospy.loginfo (hello_str)
rospy.Publisher.publish(hello_str)
rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    
