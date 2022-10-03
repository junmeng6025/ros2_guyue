# ROS2 Tutorial
ROS2 tutorial by [GuyueHome](https://www.bilibili.com/video/BV16B4y1Q7jQ/?spm_id_from=333.337.search-card.all.click)  
Version information:  
![ROS](https://img.shields.io/badge/ros2-humble-brightgreen)
![Ubuntu](https://img.shields.io/badge/ubuntu-20.04-brightgreen)  
  
  
# ROS2 vs. ROS1  
**Different:**  
- ROS2: No need of `rosmaster` anymore. Using `DDS` communication mechanism.  
- ROS2: More OOP-style programming.  
  
**Similar:**  
- Similar framework and communication concepts: topic, service, action etc.  
  
# Install ROS2
Check the [official documentation](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html)  
**What if I have to install ROS2 with ROS already in my PC?**  
- Settings for [ROS2 coexistence with ROS](https://stackoverflow.com/questions/61333625/ros2-coexistence-with-ros#:~:text=Based%20on%20Shrijit%20Singh%20comment%2C).  
# Test your ROS2
### 1) Talker and listener  
Open two terminals, first source the ros2 to both of them, then
```bash
ros2 run demo_nodes_cpp talker
```
for a demo-publisher wrote with C++ on one terminal and
```bash
ros2 run demo_nodes_py listener
```
for a demo-subscriber wrote with Python on the other terminal.  
### 2) Turtlesim  
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
### 1) `ros2 node + Enter`: check all the available cmds for node
- `ros2 node list` check the active nodes;  
- `ros2 node info /node-name` check the information of a certain node;  
### 2) `ros2 topic + Enter`: check all the available cmds for topic
- `ros2 topic list`  
- `ros2 topic info /topic-name`  
- `ros2 topic echo /topic-name` print the message from a topic in real-time;  
- `ros2 topic pub --rate 1 /topic-name message-type "{title1: {x: val, y: val, z: val}, ...}"` publish a message to the topic;  
eg. Publish a velocity command of type `geometry_msgs/msg/Twist` to turtlesim's topic `/turtle1/cmd_vel`:  
```bash
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```
### 3) `ros2 service + Enter`: check all the available cmds for service
- `ros2 service call /service-name service-type {service-parameters}`  
eg. Add another turtle into the turtlesim  
```bash
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"
```
### 4) ros bag
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

