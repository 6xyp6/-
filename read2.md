基于ROS的移动机器人路径规划与自主导航

首先需要下载wpb_home与wpr_simulation（以给出），并将他们发到/catkin_ws/src的路径下
之后进入脚本目录
cd ~/catkin_ws/src/wpb_home/wpb_home_bringup/scripts
执行安装脚本
./install_for_noetic.sh
再进入
cd ~/catkin_ws/src/wpr_simulation/scripts
再次安装脚本
./install_for_noetic.sh

之后进行编译工作
返回工作空间顶层目录
cd ~/catkin_ws
编译（自动处理所有包的依赖关系）
catkin_make
刷新环境变量
source devel/setup.bash

之后启动Gazebo仿真环境
source devel/setup.bash
roslaunch wpr_simulation wpb_gmapping.launch

启动键盘控制节点
source devel/setup.bash
rosrun wpr_simulation keyboard_vel_ctrl

之后控制小车对仿真地图进行探索，直到rviz界面中没有阴影部分了则探索完毕
探索之后保存地图
rosrun map_server map_saver -f ~/catkin_ws/map/my_map

之后将两张地图文件map.yaml和map.pgm更该路径到/catkin_ws/src/wpr_simulation/maps 下

要开启导航，则返回catkin_ws目录下，输入
oslaunch wpr_simulation wpb_navigation.launch
即可开始导航
2D Pose Estimate用于调整机器人初始位姿
2D Nav Goal用于规划小车目的地与到达目的地后的朝向







































