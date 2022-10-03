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
$ ros2 run demo_nodes_cpp talker
```
for a demo-publisher wrote with C++ on one terminal and
```bash
$ ros2 run demo_nodes_py listener
```
for a demo-subscriber wrote with Python on the other terminal.  
### 2) Turtlesim  
Open 2 terminals, first source the ros2, then  
```bash
$ ros2 run turtlesim  turtlesim_node
```
to launch the turtlesim node and  
```bash
$ ros2 run turtlesim turtle_teleop_key
```
to run the keyboard control node.  
