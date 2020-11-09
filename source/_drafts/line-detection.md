---
title: Line Detection Methods
date: 2017-03-24 00:00:00
toc: true
---
车道检测
<!---more--->
# Line Detection Method

# categories

1. LIDAR with laser - similar with the principles of radar, using laser to detect the location and the speed of the target, with higher cost.

2. Image processing with stereo camera, with lower cost and  low accuracy.



both of them need co-work with the 3D-map.


![automotive](https://pic1.zhimg.com/b69cfa2069e4c611d7ff430bf844df8c_b.png)

Then I do some summary of the Image Processing for lane detection.


# The methods based on the camera.
## Recognition method based on Feature
The method of feature recognition is based on the combination of some features of road boundary image (color feature, gray gradient feature, etc.). Feature based recognition methods can be divided into two categories: recognition based on gray features and color features. At present, most of the methods are based on gray features.

1. Recognition method based on gray feature
   The recognition method based on gray feature is the recognition of road boundary and lane mark from the sequence gray images in front of the vehicle.
- FLPs (A set of the feature lines in pairs)
    use the linear feature of lane edge in urban traffic environment as the main basis for road detection to establish a linear road model as closely as possible. The algorithm of linear parameters of the road model based on using a Calman filter tracking program detects each FLPs, estimate the model parameters from the road all in FLPs by annealing diagnosis technology, then using a Calman filter frame tracking road boundary, so as to get the test results more accurate and more stable.

- FOE (the focus of expansion)
    using the road marking features about the focus of expansion and when the road boundary exists most boundary points towards the FOE are located on the road boundary, then put forward a new method to identify various shapes of lanes recognition method based on the boundary of the road. Firstly, select a low threshold to obtain an edge image by zero crossing technique,  to get the position and direction of the edge point, to denoise the edge features of image, we use the feature of FOE. At the end, with histogram analysis to denoise image, Hough transform is used to get two lines, and the center of the lines is the lane mark. The method is robust to illumination change and shadow, but it is difficult to identify the curve Lane.
- Detection and tracking of road using spline curve.
   The algorithm uses the two-dimensional model of the road, will obtain the center line of the road by using a priori knowledge about the two lane mark. Then combined with the road model selected, we will detect the center line of the road to the control point for the sampling curve. Finally detect the lanes. The method uses CHEVP algorithm (Canny/Hough Estimation of Vanishing Points) to determine the location of the original B-Snake curve, and then use the MMSE (Minimum Mean Square Error) algorithm to update the control points of B-Snake curve. The advantage of this method is that it has good robustness to the noise, shadow and illumination changes in the process of image acquisition.   


2. Recognition method based on color feature

The main disadvantage of using 3D model is that the model is relatively simple or the noise intensity is relatively large, and the recognition accuracy is low.


## Recognition method based on model

1. Recognition method based on the identification of 2D road image model


2. Recognition method based on the identification of 3D road image model


# Recognition method based on the fusion of camera and other sensor 
- laser

  The laser sensor is used to collect the image to obtain the distance information of the vehicle, and a color camera and a laser sensor are combined to know the road surface and locate the road boundary



- Multi sensor fusion technology for detection of roadside, walls and fences. 

  Use the wired scanning laser rangefinder, vehicle state estimator, cameras, laser scanners to detect and track the vehicle around a range of objects, to eliminate the wrong perception of the surrounding environment.


# Conclusion
At present, there are still some technical difficulties in the identification of road boundary and lane markings based on vision.


1. effective road boundary and lane mark identification under the condition of illumination change and shadow occlusion.
2. detection of road boundary and lane markings in urban traffic environment. At present, there is little attention on the perception of road traffic in the city environment, because the traffic environment of city is not very clear, casual and geometric features of road curvature is harsh, and many vulnerable road users, it becomes more complex. The use of machine vision technology to achieve a better road perception becomes particularly difficulty.
3. identification of road boundary and lane markings in adverse weather conditions. In the harsh climate, road lane identification and contrast is relatively small, at the same time, due to the sharp reduction of the horizon, it will lead to some Lane parameter estimation error, so that a lot of lane recognition system in harsh driving conditions (rain and snow) will encounter problems.
4. identification of unstructured road.



In recent years, it has been shown that the method of road boundary and lane mark recognition based on vision has the following trends:
1.  by adding special hardware to speed up the process of image processing and the use of efficient and fast recognition algorithm to improve the real-time processing of the system.
2.  the fusion of multiple sensors is used to increase the perception of the surrounding environment.
3.  the comprehensive utilization of multi feature information of the road image, strengthen the research on the algorithm of road boundary and lane identification (such as to improve the adaptability of the model or assume a higher road model), to broaden the scope of object recognition, improve the adaptability of the system.
4.  identification of multiple lanes. When the vehicle is in a lane changing operation, it is necessary to identify the multiple lanes in front of the vehicle to obtain a more accurate estimation of the position of the vehicle. At the same time, multi lane identification is also helpful to identify obstacles in each lane.




