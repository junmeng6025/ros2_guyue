# ROS2 Tutorial
ROS2 tutorial by [GuyueHome](https://www.bilibili.com/video/BV16B4y1Q7jQ/?spm_id_from=333.337.search-card.all.click)  
Version information:  
![ROS](https://img.shields.io/badge/ros2-humble-blue)
![Ubuntu](https://img.shields.io/badge/ubuntu-20.04-blue)  
  
  
# ROS2 vs. ROS1  
**Different:**  
- ROS2: No need of `rosmaster` anymore. Using `DDS` communication mechanism.  
- ROS2: More OOP-style programming.  
  
**Similar:**  
- Similar framework and communication concepts: topic, service, action etc.  
  
# Install ROS2
Check the [official documentation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)  
**What if I have to install ROS2 with ROS already in my PC?**  
- Settings for [ROS2 coexistence with ROS](https://stackoverflow.com/questions/61333625/ros2-coexistence-with-ros#:~:text=create%20in%20your%20home%20directory%20the%20file%20.bash_aliases).  
# Test your ROS2
## 1) Talker and listener  
Open two terminals, first source the ros2 to both of them, then
```bash
ros2 run demo_nodes_cpp talker
```
for a demo-publisher wrote with C++ on one terminal and
```bash
ros2 run demo_nodes_py listener
```
for a demo-subscriber wrote with Python on the other terminal.  
## 2) Turtlesim  
Open 2 terminals, first source the ros2, then  
```bash
ros2 run turtlesim  turtlesim_node
```
to launch the turtlesim node and  
```bash
ros2 run turtlesim turtle_teleop_key
```
to run the keyboard control node.  
  
# Common-used ROS2 commands  
## 1) `ros2 node + Enter`: check all the available cmds for node
- `ros2 node list` check the active nodes;  
- `ros2 node info /node-name` check the information of a certain node;  
## 2) `ros2 topic + Enter`: check all the available cmds for topic
- `ros2 topic list`  
- `ros2 topic info /topic-name`  
- `ros2 topic echo /topic-name` print the message from a topic in real-time;  
- `ros2 topic pub --rate 1 /topic-name message-type "{title1: {x: val, y: val, z: val}, ...}"` publish a message to the topic;  
eg. Publish a velocity command of type `geometry_msgs/msg/Twist` to turtlesim's topic `/turtle1/cmd_vel`:  
```bash
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```
## 3) `ros2 service + Enter`: check all the available cmds for service
- `ros2 service call /service-name service-type {service-parameters}`  
eg. Add another turtle into the turtlesim  
```bash
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"
```
## 4) ros bag
- `ros2 bag record /topic-name`
eg. record the `/turtle1/cmd_vel`  
```bash
ros2 bag record /turtle1/cmd_vel
```
The recorded data would be saved to the current path of the terminal.   
- `ros2 bag play bag-name`
eg. play the recorded `/turtle1/cmd_vel`  
```bash
ros2 bag play rosbag2_2022_10_03-12_49_13
```
**Here** replace the bag name with yours correspondingly.  
  
# Configure the ROS2 developing environment
## 0) `rosdepc` install dependencies for an existing ros project
`rosdepc` is a tool that can help to install all the dependencies for a workspace automatically.  
### install and initialize rosdepc
```bash
sudo pip3 install rosdepc
sudo rosdepc init & rosdepc update
```
### install dependencies for workspace
```bash
# cd to the workspace root path
rosdepc install -i --from-path src --rosdistro galactic -y
```
## 1) Workspace
```bash
mkdir -p ~/colcon_ws/src  # create workspace and src folders
cd colcon_ws
colcon build  # compile the workspace
```
after `colcon build` the folder structure would be like  
```bash
colcon_ws
├── build
│   └── COLCON_IGNORE
├── install
│   ├── COLCON_IGNORE
│   ├── local_setup.sh  # source install/local_setup.sh
│   ├── _local_setup_util_sh.py
│   └── setup.sh
├── log
│   └── ...
└── src  # contains the packages

```
## 2) Package
```
ros2 pkg create --build-type <build-type> <package_name>
```
create a package
```bash
cd ~/colcon_ws/src
ros2 pkg create --build-type ament_cmake learning_pkg_c       # C++
ros2 pkg create --build-type ament_python learning_pkg_python # Python
```
for **c++ package**, there should be `package.xml` and `CMakeLists.txt`.  
for **python package**, there should be `package.xml`, `setup.cfg` and `setup.py`.  
The information of dependencies for `rosdepc` is exactly provided by `package.xml`.  
  
# ROS node
## What is node?
- execute a certain process of the App;  
- an independent `.exe` file;  
- compliable for multiple programming languages, e.g. cooperation of a `talker.cpp` and a `listener.py`;  
- can be launched on differnent host machines distributedly.  
- be managed with a **sole** node name.  
## 0) Source the ROS2 to the current terminal before launching VSCode
Sometimes we might encounter problems like **"Import rclpy cannot be resolved"**. This can happen when we didn't link to ROS2's shell environment correctly, especially we have ROS and ROS2 coexist and any of them is NOT sourced defaultly to our terminal.  
Actually, the necessary libraries `rclpy` and `rclcpp` are supposed to be installed along with ros2.  
- *(If not, install the library `rclpy` manuelly:  https://index.ros.org/r/rclpy/)*  
   

According to the [official guide](https://code.visualstudio.com/docs/supporting/faq#_resolving-shell-environment-fails:~:text=Launch%20VS%20Code%20from%20a%20terminal), we can avoid VS Code's resolving shell environment phase by launching VS Code directly from a fully initialized terminal:
```bash
source /opt/ros/galactic/setup.bash  # link to ROS2's shell environment
cd colcon_ws/src
code .
```
  
## 1) Write the node: Object-oriented Programming (OOP)  
- create package
- create script
  - add this at the begining of the `.py` script
    ```python
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    ```
- make executable `.exe` file
  - **C++:** configure `CMakeList.txt`
  - **Python:** via the command `chmod +x node.py`
## 2) Compile the node
### Python
Configure the `setup.py`: add the **node entry** in `entry_points`:  
e.g.:  
```Python
entry_points={
        'console_scripts': [
        'node_helloworld = learning_node.node_helloworld:main',
        ...
        ],
    },
```
Note that every time we've modified the `.py` script we need to re-build the workspace so that the changes could be updated, which is different from ROS1.  
- for ROS1, the Python node we would run is exactly the script we've modified in `/src`
- for ROS2, the Python node is in `/install`, generated from the script via `$ colcon build`.
## 3) Run the node
We MUST source the `setup.sh` before running a ros node, which is likely to what we did with ROS1
```bash
cd colcon_ws
source install/setup.sh  # for ROS1, it was $ source devel/setup.bash
ros2 run learning_node node_helloworld
```
Command syntax:
```
$ ros2 run <pkg_name> <node_name>
```
### C++
`<node_name>` stands for an `.exe` file which was built by `CMake` during compiling;  
### Python
`<node_name>`, or exactly `<node_name.py>` is an `.exe` file directly converted from the `.py` script.  
  
