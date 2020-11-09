---
title: ROS NOTE
date: 2017-07-08 21:00:00
toc: true
---



The note when I use ROS Kinetic.

<!-- more -->

# Install

```bash
# Setup your sources.list
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
# Set up your keys
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
# Installation
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full
# Initialize rosdep
sudo rosdep init
rosdep update
# Environment setup
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
# Getting rosinstall
sudo apt-get install python-rosinstall
# Managing Your Environment
source /opt/ros/kinetic/setup.bash
```



# Initialization

```bash
# Create a ROS Workspace
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
source devel/setup.bash
```



# ROS File System

```bash
# get information about packages
rospack find [package_name]
# change directory (cd) directly to a package or a stack.
roscd [locationname[/subdir]]
# print the working directory
pwd
# echo ROS_PACKAGE_PATH
echo $ROS_PACKAGE_PATH
# to the folder where ROS stores log files
roscd log
#  ls directly in a package by name rather than by absolute path.
rosls [locationname[/subdir]]

```



# Package

```bash
# Creating a catkin Package
catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
# to show the first-order dependencies of the package
rospack depends1 <package_name>
# These dependencies for a package are stored in the package.xml file
roscd <package_name>
cat package.xml
# recursively determine all nested dependencies.
rospack depends <package_name>
```





# Building a ROS Package

```bash
# source your environment setup file
source /opt/ros/kinetic/setup.bash
# use catkin_make
catkin_make [make_targets] [-DCMAKE_VARIABLES=...]
```



# rosrun

```bash
# use one thread to run the roscore
roscore
# If no permission, probably the ~/.ros folder is owned by root
# change recursively the ownership of that folder with:
sudo chown -R <your_username> ~/.ros
# run a node within a package
rosrun [package_name] [node_name]
```



# rosnode

```bash
# list
rosnode list
# get more info
rosnode info [node_name]
# run a node and change its name
rosrun [package_name] [node_name] __name:=[change_to_name]
# Ping a node to test
rosnode ping [node_name]
```



# rostopic

- rostopic

```bash
# [topic] = /topic_name
# display bandwidth used by topic
rostopic bw     
# print messages to screen (start a system node to subscribe the topic )
rostopic echo [topic]
# display publishing rate of topic
rostopic hz     
# print information about active topics
rostopic list   
# publish data to topic
rostopic pub    
# print topic type
rostopic type   
# list all topics
rostopic list [/topic]
# list full details of each topic about publishers and subscribers
rostopic list -v
rostopic list --verbose    
# list only publishers
rostopic list  -p                    
# list only subscribers
rostopic list  -s    
```

- ROS Messages

Communication on topics happens by sending ROS messages between nodes.

```bash
# returns the message type of any topic being published.
rostopic type [topic]
# the details of the message
rosmsg show [topic]
```



```bash
# reports the rate at which data is published.
rostopic hz [topic]
```



```bash
# Publish# publishes data on to a topic currently advertised.
rostopic pub [topic] [msg_type] [args]
```

sample:

```bash
rostopic pub -1 /turtle1/command_velocity turtlesim/Velocity  -- 2.0  1.8
# -1	This option (dash-one) causes rostopic to only publish one message then exit
# --	his option (double-dash) tells the option parser that none of the following arguments is an option. 
# '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]' 	These arguments are actually in YAML syntax
rostopic pub /turtle1/command_velocity turtlesim/Velocity -r 1 -- 2.0  -1.8
# -r	publish a steady stream of commands
```





# rosservices

Services are another way that nodes can communicate with each other. 

Services allow nodes to send a request and receive a response.

```bash
# [service] = /service_name
# print information about active services
rosservice list [service]            
# call the service with the provided args
rosservice call [service] [args]      
# print service type
# std_srvs/Empty	no need for arguments
rosservice type [service]    

# find services by service type
rosservice find [service]       
# print service ROSRPC uri
rosservice uri [service]   


```

# rosparam

rosparam allows you to store and manipulate data on the ROS Parameter Server



| 1       | 1.0   | one    | true    | [1, 2, 3]        | {a: b, c: d} |
| ------- | ----- | ------ | ------- | ---------------- | ------------ |
| integer | float | string | boolean | list of integers | dictionary   |



```bash
# set parameter
rosparam set [param_name] [param_value]        
# get parameter
rosparam get 
# to show us the contents of the entire Parameter Server.
rosparam get /
# load parameters from file
rosparam load           
# dump parameters to file
rosparam dump           
# delete parameter
rosparam delete         
# list parameter names
rosparam list           

# write all the parameters to the file params.yaml
# rosparam dump params.yaml
rosparam dump [file_name] [namespace]
# load these yaml files into new namespaces
# rosparam load params.yaml copy
# rosparam get /copy/background_b
rosparam load [file_name] [namespace]
```







# roslaunch

```bash
# starts nodes as defined in a launch file.
roslaunch [package] [filename.launch]

```

filename.launch sample

```xml
<launch>
  <group ns="turtlesim1"><!--namespace-->
    <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
  </group>
  <group ns="turtlesim2"> 
    <node pkg="turtlesim" name="sim" type="turtlesim_node"/>
  </group>
  <node pkg="turtlesim" name="mimic" type="mimic">
    <remap from="input" to="turtlesim1/turtle1"/>
    <remap from="output" to="turtlesim2/turtle1"/>
  </node>
</launch>
```

# rosmsg and rossrv

- msg: 

  msg files are simple text files that describe the fields of a ROS message. They are used to generate source code for messages in different languages.

  msg files are stored in the msg directory of a package, 


   a special type in ROS: `Header`

sample:

``` bash
 Header header
 string child_frame_id
 geometry_msgs/PoseWithCovariance pose
 geometry_msgs/TwistWithCovariance twist
```

- srv: 

  an srv file describes a service. It is composed of two parts: a request and a response.

  and srv files are stored in the srv directory.

  msgs are just simple text files with a field type and field name per line. 

  - int8, int16, int32, int64 (plus uint*)
  - float32, float64
  - string
  - time, duration
  - other msg files
  - variable-length array[] and fixed-length array[C]

sample

```bash
int64 A
int64 B
---
int64 Sum
```



- creating a msg

```bash
roscd beginner_tutorials
mkdir msg
echo "int64 num" > msg/Num.msg
```

Open `package.xml`, and make sure these two lines are in it and uncommented:

```xml
<build_depend>message_generation</build_depend>
<run_depend>message_runtime</run_depend>
```

`CMakeLists.txt` to add the `message_generation` dependency to the `find_package` call 

```tx
find_package(catkin REQUIRED COMPONENTS
   roscpp
   rospy
   std_msgs
   message_generation
)
```

make sure you export the message runtime dependency

```txt
catkin_package(
  ...
  CATKIN_DEPENDS message_runtime ...
  ...)
```

```txt
add_message_files(
  FILES
  Num.msg
)
```

```txt
generate_messages()
```

- using rosmsg

```bash
# make sure that ROS can see it 
rosmsg show [message type]
```



- creating srv

```bash
roscd beginner_tutorials
mkdir srv
# copy from other service
roscp [package_name] [file_to_copy_path] [copy_path]
# roscp rospy_tutorials AddTwoInts.srv srv/AddTwoInts.srv


```



make sure that the srv files are turned into source code for C++, Python, and other languages.

`CMakeLists.txt`

```txt
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs message_generation)
```

```txt
add_service_files(
  FILES
  AddTwoInts.srv
)
```



`package.xml`

 `message_generation` works for both `msg` and `srv`.

```xml
<build_depend>message_generation</build_depend>
<run_depend>message_runtime</run_depend>
```



- using rossrv

```bash
rossrv show <service type>
# rossrv show beginner_tutorials/AddTwoInts
```



- final

`CMakeLists.txt`

```txt
generate_messages(
  DEPENDENCIES
  std_msgs
)
```

```bash
# compile the package
catkin_make
```



- help

```bash
rosmsg -h
# Show message description
rosmsg show 
# Find files that use message
rosmsg users  
# Display message md5sum
rosmsg md5  
# List messages in a package
rosmsg package  
# List packages that contain messages
rosmsg packages 

rosmsg show -h
rosmsg show [options] <message type>
# Options:
#  -h, --help  show this help message and exit
#  -r, --raw   show raw message text, including comments
```





# Tool

```bash
# rqt_graph creates a dynamic graph of what's going on in the system about the communication.
rosrun rqt_graph rqt_graph
# displays a scrolling time plot of the data published on topics. 
# If you're using electric or earlier, rqt is not available. Use rxplot instead.
rosrun rqt_plot rqt_plot
# rqt_console displays output from nodes. 
rosrun rqt_console rqt_console
# rqt_logger_level changes the verbosity level (DEBUG, WARN, INFO, and ERROR) of nodes as they run.
rosrun rqt_logger_level rqt_logger_level

# edit a file within a package
rosed [package_name] [filename]
# To set the default editor to emacs you can edit your ~/.bashrc file to include:
export EDITOR='emacs -nw'

# roswtf examines your system to try and find problems. 
# If you find yourself stumped by a build or communication issue, try running it and seeing if it can point you in the right direction.
roswtf
# set your ROS_PACKAGE_PATH to a bad value. We're also going to stop our roscore to simplify the output that you see.
ROS_PACKAGE_PATH=bad:$ROS_PACKAGE_PATH roswtf

```



# Publisher and Subscriber 

- Publisher

```bash
mkdir -p ~/catkin_ws/src/[package_name]/src
```

`talker.cpp`

```c++
// use the most common public pieces of the ROS system.
#include "ros/ros.h"
// This is a header generated automatically from the String.msg file in that package
#include "std_msgs/String.h"

#include <sstream>

/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{
  /**
   * The ros::init() function needs to see argc and argv so that it can perform
   * any ROS arguments and name remapping that were provided at the command line. For programmatic
   * remappings you can use a different version of init() which takes remappings
   * directly, but for most command-line programs, passing argc and argv is the easiest
   * way to do it.  The third argument to init() is the name of the node.
   *
   * You must call one of the versions of ros::init() before using any other
   * part of the ROS system.
   */
  // Initialize ROS. This allows ROS to do name remapping through the command line
  // The name used here must be a base name, ie. it cannot have a / in it.
  ros::init(argc, argv, "talker");

  /**
   * NodeHandle is the main access point to communications with the ROS system.
   * The first NodeHandle constructed will fully initialize this node, and the last
   * NodeHandle destructed will close down the node.
   */
  // Create a handle to this process' node. 
  // The first NodeHandle created will actually do the initialization of the node, and the last one destructed will cleanup any resources the node was using.
  ros::NodeHandle n;

  /**
   * The advertise() function is how you tell ROS that you want to
   * publish on a given topic name. This invokes a call to the ROS
   * master node, which keeps a registry of who is publishing and who
   * is subscribing. After this advertise() call is made, the master
   * node will notify anyone who is trying to subscribe to this topic name,
   * and they will in turn negotiate a peer-to-peer connection with this
   * node.  advertise() returns a Publisher object which allows you to
   * publish messages on that topic through a call to publish().  Once
   * all copies of the returned Publisher object are destroyed, the topic
   * will be automatically unadvertised.
   *
   * The second parameter to advertise() is the size of the message queue
   * used for publishing messages.  If messages are published more quickly
   * than we can send them, the number here specifies how many messages to
   * buffer up before throwing some away.
   */
  // Tell the master that we are going to be publishing a message of type std_msgs/String on the topic chatter. 
  // This lets the master tell any nodes listening on chatter that we are going to publish data on that topic. 
  // The second argument is the size of our publishing queue. In this case if we are publishing too quickly it will buffer up a maximum of 1000 messages before beginning to throw away old ones.
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
// A ros::Rate object allows you to specify a frequency that you would like to loop at. 
  ros::Rate loop_rate(10);

  /**
   * A count of how many messages we have sent. This is used to create
   * a unique string for each message.
   */
  int count = 0;
  // ros::ok() will return false if:
// - a SIGINT is received (Ctrl-C)
// - we have been kicked off the network by another node with the same name
// - ros::shutdown() has been called by another part of the application.
// - all ros::NodeHandles have been destroyed
  while (ros::ok())
  {
    /**
     * This is a message object. You stuff it with data, and then publish it.
     */
    std_msgs::String msg;

    std::stringstream ss;
    ss << "hello world " << count;
    msg.data = ss.str();
// print out
    ROS_INFO("%s", msg.data.c_str());

    /**
     * The publish() function is how you send messages. The parameter
     * is the message object. The type of this object must agree with the type
     * given as a template parameter to the advertise<>() call, as was done
     * in the constructor above.
     */
    // broadcast the message to anyone who is connected.
    chatter_pub.publish(msg);
// callback function
    ros::spinOnce();
// sleep for the time remaining to let us hit our 10Hz publish rate.
    loop_rate.sleep();
    ++count;
  }
  return 0;
}
```

- Subscriber

```bash
mkdir -p ~/catkin_ws/src/[package_name]/src
```

``listener.cpp` `

```c++
#include "ros/ros.h"
#include "std_msgs/String.h"

/**
 * This tutorial demonstrates simple receipt of messages over the ROS system.
 */
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
// This is the callback function that will get called when a new message has arrived on the chatter topic. 
// The message is passed in a boost shared_ptr, which means you can store it off if you want, without worrying about it getting deleted underneath you, and without copying the underlying data.
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  /**
   * The ros::init() function needs to see argc and argv so that it can perform
   * any ROS arguments and name remapping that were provided at the command line. For programmatic
   * remappings you can use a different version of init() which takes remappings
   * directly, but for most command-line programs, passing argc and argv is the easiest
   * way to do it.  The third argument to init() is the name of the node.
   *
   * You must call one of the versions of ros::init() before using any other
   * part of the ROS system.
   */
  ros::init(argc, argv, "listener");

  /**
   * NodeHandle is the main access point to communications with the ROS system.
   * The first NodeHandle constructed will fully initialize this node, and the last
   * NodeHandle destructed will close down the node.
   */
  ros::NodeHandle n;

  /**
   * The subscribe() call is how you tell ROS that you want to receive messages
   * on a given topic.  This invokes a call to the ROS
   * master node, which keeps a registry of who is publishing and who
   * is subscribing.  Messages are passed to a callback function, here
   * called chatterCallback.  subscribe() returns a Subscriber object that you
   * must hold on to until you want to unsubscribe.  When all copies of the Subscriber
   * object go out of scope, this callback will automatically be unsubscribed from
   * this topic.
   *
   * The second parameter to the subscribe() function is the size of the message
   * queue.  If messages are arriving faster than they are being processed, this
   * is the number of messages that will be buffered up before beginning to throw
   * away the oldest ones.
   */
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

  /**
   * ros::spin() will enter a loop, pumping callbacks.  With this version, all
   * callbacks will be called from within this thread (the main one).  ros::spin()
   * will exit when Ctrl-C is pressed, or the node is shutdown by the master.
   */
// ros::spin() enters a loop, calling message callbacks as fast as possible. 
// Don't worry though, if there's nothing for it to do it won't use much CPU.
  ros::spin();

  return 0;
}
```

- build nodes

`package.xml` 

`CMakeLists.txt`

``txt

```
cmake_minimum_required(VERSION 2.8.3)
project(beginner_tutorials)

## Find catkin and any catkin packages
find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs genmsg)

## Declare ROS messages and services
add_message_files(FILES Num.msg)
add_service_files(FILES AddTwoInts.srv)

## Generate added messages and services
generate_messages(DEPENDENCIES std_msgs)

## Declare a catkin package
catkin_package()

#####################################################
## Build talker and listener
include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(talker src/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
add_dependencies(talker beginner_tutorials_generate_messages_cpp)

add_executable(listener src/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
add_dependencies(listener beginner_tutorials_generate_messages_cpp)
```

# Service and Client

- Service

`add_two_ints_server.cpp`

```c++
#include "ros/ros.h"
// beginner_tutorials/AddTwoInts.h is the header file generated from the srv file that we created earlier.
#include "beginner_tutorials/AddTwoInts.h"

bool add(beginner_tutorials::AddTwoInts::Request  &req,
         beginner_tutorials::AddTwoInts::Response &res)
{
  res.sum = req.a + req.b;
  ROS_INFO("request: x=%ld, y=%ld", (long int)req.a, (long int)req.b);
  ROS_INFO("sending back response: [%ld]", (long int)res.sum);
  return true;
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "add_two_ints_server");
  ros::NodeHandle n;

  ros::ServiceServer service = n.advertiseService("add_two_ints", add);
  ROS_INFO("Ready to add two ints.");
  ros::spin();

  return 0;
}
```

- Client

`add_two_ints_client.cpp`

```c++
#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"
#include <cstdlib>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "add_two_ints_client");
  if (argc != 3)
  {
    ROS_INFO("usage: add_two_ints_client X Y");
    return 1;
  }

  ros::NodeHandle n;
  // this creates a client for the add_two_ints service. 
  // The ros::ServiceClient object is used to call the service later on.
  ros::ServiceClient client = n.serviceClient<beginner_tutorials::AddTwoInts>("add_two_ints");
  beginner_tutorials::AddTwoInts srv;
  srv.request.a = atoll(argv[1]);
  srv.request.b = atoll(argv[2]);
  // calls the service
  //  Since service calls are blocking, it will return once the call is done. 
  // If the service call succeeded, call() will return true and the value in srv.response will be valid. 
  // If the call did not succeed, call() will return false and the value in srv.response will be invalid.
  if (client.call(srv))
  {
    ROS_INFO("Sum: %ld", (long int)srv.response.sum);
  }
  else
  {
    ROS_ERROR("Failed to call service add_two_ints");
    return 1;
  }
  return 0;
}
```

- build node

```txt
add_executable(add_two_ints_server src/add_two_ints_server.cpp)
target_link_libraries(add_two_ints_server ${catkin_LIBRARIES})
add_dependencies(add_two_ints_server beginner_tutorials_gencpp)

add_executable(add_two_ints_client src/add_two_ints_client.cpp)
target_link_libraries(add_two_ints_client ${catkin_LIBRARIES})
add_dependencies(add_two_ints_client beginner_tutorials_gencpp)
```

# rosbag

```bash
# all published topics should be accumulated in a bag file.
rosbag record -a
# checks the contents of the bag file without playing it back.
# topic names and types as well as the number (count) of each message topic contained in the bag file
rosbag info <your bagfile>
# replay the bag file to reproduce behavior in the running system.
rosbag play [option] <your bagfile>
# -r value	change the rate of publishing by a specified factor
# -d 	 If rosbag play publishes messages immediately upon advertising, subscribers may not receive the first several published messages. The waiting period can be specified with the -d option.
# Recording a subset of the data
rosbag record [topic_name]
```









































