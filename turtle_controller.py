#!/usr/bin/env python3
import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class TurtleController:
    def __init__(self):
        # 初始化ROS节点
        rospy.init_node('turtle_controller', anonymous=True)
        
        # 创建发布者和订阅者
        self.velocity_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        
        # 目标点坐标
        self.target_x = 4.0
        self.target_y = 4.0
        
        # 当前位置和方向
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_theta = 0.0
        
        # 设置循环频率
        self.rate = rospy.Rate(10)  # 10Hz
    
    def pose_callback(self, data):
        # 更新当前位置和方向
        self.current_x = data.x
        self.current_y = data.y
        self.current_theta = data.theta
    
    def calculate_distance(self):
        # 计算当前位置与目标点的距离
        return math.sqrt((self.target_x - self.current_x)**2 + (self.target_y - self.current_y)**2)
    
    def calculate_angle(self):
        # 计算朝向目标点需要的角度
        return math.atan2(self.target_y - self.current_y, self.target_x - self.current_x)
    
    def run(self):
        # 等待获取初始位置
        while not rospy.is_shutdown() and (self.current_x == 0.0 and self.current_y == 0.0):
            rospy.sleep(0.1)
        
        rospy.loginfo(f"当前位置: ({self.current_x}, {self.current_y})")
        rospy.loginfo(f"目标位置: ({self.target_x}, {self.target_y})")
        
        # 控制海龟移动到目标点
        while not rospy.is_shutdown() and self.calculate_distance() > 0.1:
            # 创建速度消息
            vel_msg = Twist()
            
            # 计算距离和角度
            distance = self.calculate_distance()
            target_angle = self.calculate_angle()
            angle_diff = target_angle - self.current_theta
            
            # 归一化角度差到 [-pi, pi]
            while angle_diff > math.pi:
                angle_diff -= 2 * math.pi
            while angle_diff < -math.pi:
                angle_diff += 2 * math.pi
            
            # 设置角速度 (转向)
            vel_msg.angular.z = 4.0 * angle_diff
            
            # 设置线速度 (前进)
            if abs(angle_diff) < math.pi/4:  # 当角度大致正确时才前进
                vel_msg.linear.x = 0.5 * distance
            
            # 发布速度指令
            self.velocity_pub.publish(vel_msg)
            
            # 按照设定频率休眠
            self.rate.sleep()
        
        # 停止移动
        vel_msg = Twist()
        self.velocity_pub.publish(vel_msg)
        rospy.loginfo("已到达目标位置!")

if __name__ == '__main__':
    try:
        controller = TurtleController()
        controller.run()
    except rospy.ROSInterruptException:
        pass
