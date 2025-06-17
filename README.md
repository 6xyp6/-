# -
基于ros的海龟运动，移动机器人路径规划与自主导航


海龟部分

在虚拟机中断创建工作空间和功能包，输入下面指令来创建ROS工作空间（名为catkin_ws）
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src

创建功能包（名为turtle_control）
catkin_create_pkg turtle_control rospy geometry_msgs turtlesim
编译工作空间
cd ~/catkin_ws
catkin_make
加载环境变量（每次打开新终端都需要执行）
source devel/setup.bash

之后打开 VSCode 并创建 Python 文件
打开终端，输入以下命令启动 VSCode 并定位到工作空间
code ~/catkin_ws/src/turtle_control
打开文件 turtle_controller.py（下列所有文件都已给出）
在 VSCode 中，点击 create a launch.json file ，选择ros环境，打开launch.json文件

之后在终端创建 launch 启动文件
mkdir ~/catkin_ws/src/turtle_control/launch
touch ~/catkin_ws/src/turtle_control/launch/turtle_control.launch
在vscode中打开文件 launch/turtle_control.launch

接下来进行仿真，打开终端，首先进行文件编译
cd ~/catkin_ws
catkin_make
source devel/setup.bash
添加脚本权限
chmod +x ~/catkin_ws/src/turtle_control/src/turtle_controller.py

分步启动仿真，每步一个新终端
1.启动ros核心
roscore
2.启动 turtlesim
source ~/catkin_ws/devel/setup.bash
rosrun turtlesim turtlesim_node
3.启动控制节点
source ~/catkin_ws/devel/setup.bash
rosrun turtle_control turtle_controller.py
