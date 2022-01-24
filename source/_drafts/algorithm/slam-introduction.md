---
title: slam introduction
date: 2017-03-26 19:47:39
toc: true
---

SLAM - Simultaneous Localization and Mapping
高翔, 张涛, 颜沁睿, 刘毅, 视觉SLAM十四讲：从理论到实践, 电子工业出版社, 2017

<!-- more -->

# Framework
- Sensor
- Vision Odametry
- Back-end
- Mapping
- Loop Closure Detection

When we implement slam algorithm, we focus on these four asspects:
1. Present the map.
dense or sparse
2. perceive information 
how to perceive the information roundly. the field of view of RGB-F camera is narrow, but that of LIDAT is too wide. 

3. Associate the data
the coordinate, timestamp and data type of different sensors are different.

4. Location and Mapping
how to locate and build the model, which involves many math problems like Physical model establishment, state estimation and optimization.
There are other loopback detection problems, exploration problems, and kidnapping.

# Sensor
## LIDAR
Laser rader is the oldest sensor in SLAM, which provides the information about the distance between sensor and obstacle with high precision of angles and ranges.
But because most of robots are limited in the ground, so the Mapping of slam is 2D-map in many filter ways, like Kalman filter and particle filter.
- advantage: high precision,wide viewing range; fast; low computational effort; 

- disadvantage: high cost.

low cost radar angle resolution is not high enough which will affect the modeling accuracy

## Camera
Camera is becoming popular in recent decade, with the rapid growth of CPU/GPU processing speed.
SLAM can be divided by typies of cameras.
1. Monocular Camera
advantage: low cost, simple.
However, the unability to determine the depth also has a benefit: it makes monocular SLAM not affected by the size of the environment, so it can be used both indoors and outdoors.  
disadvantage: can't get the exact information of depth. So it can't know the robot movement trajectory and the true size of the map.
It can get the relative depth estimation by solving the similar transformation space Sim(3), rather than the traditional Euclidean space SE(3). If we have to solve in SE(3), we need to use some external means, such as GPS, IMU and other sensors to determine the track and map scale.

On the other hand, the monocular camera can not rely on an image to obtain the relative distance of the object in the image from itself. To estimate this relative depth, monocular SLAM relies on triangulation in motion to solve the camera motion and estimate the spatial position of the pixel. That is, its trajectory and map will converge and know the location of the pixel only after the camera movement. At the same time, the camera movement can not be a pure rotation, which gives the application of monocular SLAM has brought some trouble, but in the daily use of SLAM, the camera will rotate and move. 

    - Monocular Camera + Inertial Measurement Unit(IMU)

2. Binocular Camera

The binocular camera estimates the position of the spatial point through the baseline between multiple cameras. Unlike monocular, stereoscopic vision can be estimated at the time of motion, and can be estimated at rest, eliminating many of the troubles of monocular vision. However, binocular or multi-nocular camera configuration and calibration are more complex, and its depth range is also limited by the baseline and resolution. Calculating the distance by a binocular image is a matter of very computational effort and is now done with an FPGA.

3. RGB-D

Its biggest feature is that through the infrared structural light or Time-of-Flight principle, directly measurea the distanceof each pixel from the camera. Therefore, it can provide richer information than traditional cameras, and it does not have to calculate the depth as time or effort as monocular or binocular. However, now most of the RGBD camera there are still with narrow measurement range, noisy, small field of vision and many other issues. Out of range limits, it is mainly for indoor SLAM.

    - Structural Light Method
    Structural light method is an active optical measurement technology, the basic principle is the structure of the projectile projection to the surface of the measured object can be controlled by the light point, light strip or light plane. By the image sensor to obtain the image, through the system geometry, using the triangular principle to calculate the three-dimensional coordinates of the object. 
    advantage: simple calculation, small volume, low price, large potting process, easy installation and maintenance, and is widely used in the actual three-dimensional contour measurement. 
    
    However, the measurement accuracy is limited by physical optics, and there are occlusion problems. Because of the speed of mutual contradiction. it is difficult to be improved at the same time.
    

    - Time of Flight(ToF)
    The sensor sends the modulated near-infrared light, after the reflection of the object, it gets the information of depth through the calculation of light transmission and reflection time difference or phase difference, which are converted to the distance of the scene to be shot.
    
    
4. fisheye camera / panoramic camera

## Hybrid Sensors

# Vision Odametry

vision Odometry, that is, vision odometer. It estimates the relative motion (Ego-motion) of the robot at two moments. In the laser SLAM, we can match the current observations with the global map, and use ICP to solve the relative motion. And for the camera, it moves in Euclidean space, and we often need to estimate a three-dimensional transformation matrix - SE3 or Sim3 (monocular). Solving this matrix is ​​the core of VO, and the idea of ​​solving is divided into feature-based ideas and direct methods that do not use features.

The feature-based approach is currently the mainstream of VO. For two images, the feature of the image is extracted first, and then the camera's transformation matrix is ​​calculated according to the feature matching of the two graphs. The most commonly used are point features, such as Harris Corner, SIFT, SURF, ORB. If you use an RGBD camera, you can directly estimate the motion of the camera with feature points of known depth. Given a set of feature points and the pairing relationship between them, the camera's attitude is solved, which is called the Perspective-N-Point. PnP can be solved by nonlinear optimization, and the positional relationship between two frames is obtained.

The method of not using the feature for VO is called the direct method. It directly finds the relative motion between the frames using all the pixels of the image in a pose estimation equation. 
For example, in RGBD SLAM, the transformation matrix between two point clouds can be solved using ICP (Iterative Closest Point). For monocular SLAM, we can match the pixels between two images, or match the image with a global model. A typical example of a direct method is SVO and LSD-SLAM. They used the direct method in monocular SLAM, and achieved good results. Tthe direct function of the VO requires more computation, and the camera's image acquisition rate also has a higher demand.

# Back-end
After estimating the inter-frame motion, theoretically the robot's trajectory can be obtained. However, in vision odometer and ordinary odometer, there is the cumulative error which will lead to drift. So in the SLAM, we will put the relative motion between the frame into a process known as the back-end processing.

After the 21st century, SLAM researchers began to introduce Bundle Adjustment into SLAM by drawing on the methods in the SfM (Structure from Motion) problem. The optimization method and the filter method are fundamentally different. It is not an iterative process, but rather the information in all past frames. By optimizing, the error is evenly divided into each observation. Bundle Adjustment in SLAM is often given in the form of graphs, so researchers are also known as Graph Optimization. Graph optimization can visually represent optimization problems, can be used to quickly solve the sparse algebra, the expression loop is also very convenient, and thus become the mainstream of today's vision SLAM optimization method.

In traditional, we will optimize the results of the front end using filters like EKF, UKF, PF, or optimization theory like TORO, G2O for tree or graph optimization. And finally get the optimal pose estimation.

After the 21st century, SLAM researchers began to introduce Bundle Adjustment into SLAM by drawing on the methods in the SfM (Structure from Motion) problem, which is fundamentally different with the optimization method and the filter method. It is not an iterative process, but rather considering the information in all past frames. The error is evenly divided into each observation by optimizing. Bundle Adjustment in SLAM is often given in the form of graphs, which is also known as Graph Optimization. Graph optimization can visually represent optimization problems, can be solved quickly using sparse algebra, and the expression for loop is also very convenient, and thus it becomes the mainstream of vision SLAM optimization method.

# Mapping
- Raster Map 
- Topology Map 
- 2D / 3D

# Loop Closure Detection
Loop closure detection refers to the ability of the robot to identify the scene that has been reached. If the test is successful, the cumulative error can be significantly reduced. Loop closure detection is an algorithm for detecting the similarity of observed data. For vision SLAM, most systems use the model of Bag of Words. The Bag of Words clusters the visual features (SIFT, SURF, etc.) of the image, and then creates a dictionary to find what "word" is included in each figure. 
There are also researchers using the traditional pattern recognition method, regarding the Loop closure detection as a classification problem, training classifier for classification.
The difficulty of Loop closure detection is that the wrong test results may make the bad map. These errors are divided into two categories: 
1. False Positive, also known as Perceptual Aliasing, which refers to the fact that different scenes are treated as the same; 
2. False Negative, also known as Perceptual Variability, refers to the fact that the same scene regarded as two. 

A good Loop closure detection algorithm should be able to detect the true loops as much as possible. Researchers often use the accuracy rate - recall rate curve to evaluate a test algorithm.

# Future
the next direction of SLAM technology development:
- Multi-sensor fusion
- optimized data association and loopback detection
- integration with front-end heterogeneous processors
- improved robustness and relocation accuracy