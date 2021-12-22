---
title: The optimization of loop closure in SLAM based on CNN
date: 2017-11-010 13:00:00
toc: true
---
Traditionally, we use the the feature detector to describe the image and build the database, which is the bag of words, filled with various feature points. With the development of neural network, we can use the CNN as a kind of descriptor to detect loop closure. In this paper, we will focus on the various traditional feature detectors, and try to use convolutional neural network to optimize the loop closure, one step of SLAM.
<!-- more -->

# Introduction

SLAM, Simultaneous localization and mapping, this technology is widely used in the perception of robot inside and autopilot outside, the scene where needs to build the map of the environment for relocation or navigation. 

There are two main points for this solution, localization and mapping.

Mapping means, get the around information from various sensors like camera and LIDAR. We will focus on visual SLAM, using camera. traditionally,once it gets the information from camera, we will store the feature points in the database.

Then it is localization, the subject will use the information to estimate the location of itself in the world. for example, it could use the IMU sensor to estimate its route, or we could use the features between different frames to estimate the motion directly using the  method of Multiple View Geometry. to be exact, it will optimize relocation. it means that the subject could recognize the scene which it has been. This part is about the loop closure in SLAM. we could run a thread to detect whether get the scene  it has been, by matching the present information with database.

Of course, current research and implementation of SLAM are  that the system is divided into frontend and backend two parts. Frontend is the role of odometer and it will get the information for mapping, and backend is the optimization of the whole result, like the estimation filter and detection loop closure. Currently, the main algorithm is buddle adjustment.

 The detail about the motion estimation. because of the noise, we are not able to get the exact equation of motion $x_k =f(x_{k-1},u_k,w_k)  $  $^{[1]}$  , but the equation of observation $y_k= g(x_k,n_k)$.  Of course we will not use the whole frame of the images from camera. So it is Key frame extraction. It is unwise to spell every frame on a map. Because the distance between frames is very close, the map needs to be updated frequently, wasting time and space. So we want to add a key frame when the movement is over a certain interval. Finally, just put the key frame on the map.  but the estimation and Key frame extraction are not the focus of this paper.

The loop closure, which is really of vital importance for mapping and navigation. Because once we detect loop of the path, we can correct the old mapping and relocation. The current mainstream technology focus on extracting the feature detector, the pattern in the pixels, and then retrieval the pattern in the bag of words.

 

# Traditional Feature Detectors

## SIFT

SIFT algorithm $^{[2]}$ is a local feature extraction algorithm proposed by Lowe in 1999, and has become a famous algorithm with good stability and robustness. The algorithm has the following advantages: 

1. It is a considerable sum of feature points are  with the appropriate parameter setting;
2. The features extracted by the SIFT algorithm have the high high uniqueness, so that it can be accurately matched in large database; 
3. SIFT features have rotation, scale, translation and brightness invariance , sometimes even it will not change with viewpoint.

##SURF

The SURF feature $^{[3]}$, which is proposed by Herbert Bay et al in 2006 for the full name of the Speeded Up Robust Features, is essentially an improved version of the SIFT feature, its main characteristic is fast, and with the characteristics of the scale invariant to illumination, and for affine and perspective change, it also has strong robustness.

## ORB

ORB algorithm $^{[4]}$ was proposed by Ethan Rublee in ICCV 2011, which is based on the feature of visual information detection and description algorithm. Feature point detection using FAST corner detection, and brought the solution to the absence of direction in the FAST feature. Feature description part is the BRIEF feature descriptor, based on the comparison by pixel bits and improved the sensitivity to image noise and the absence of rotation invariance.

 # Loop closure

The key to the problem is how to judge the similarity of the two frames. The most intuitive way is to match the features and evaluate the number of matches. But since the feature matching is time consuming, the loop closure detection needs to match all the key frames of the past. Thus, Bag of Words model is proposed to speed up feature matching.

## Bag of Words

Bag of Words $^{[5]}$ is a concept that is frequently used in the Natural Language Processing field. In text, for example, an article may have ten thousand words, of which there may be only 500 different words with different frequency. Bag of Words is like a bag with the same words in each bag. This constitutes a representation of text. This representation does not take into account the order and grammar. In the field of computer vision, images are usually represented by feature points and their feature descriptions. If the feature description is regarded as a word, then the corresponding Bag of Words model can be constructed. Using BoW, the image can be conveniently transformed into a low dimensional vector representation. The  comparison of the similarity of the two images is translated into the  comparison of the similarity of the two vectors. It is essentially a process of compressing information.

For Visual vocabulary, the steps are as follows.

- firstly, detect the features of an image set, and then form feature descriptions. 
- form a dictionary based on the descriptor clustering, such as level kmeans algorithm to form a vocabulary tree: the descriptor in the same subset of one node are similar, and this set can be considered as a visual word (certainly the top words are more complex).
- For each image in the image set, the corresponding feature description is extracted and classified. Then the status of absence of the word can be described as a vector.
- Then the similarity between two images can be known according to the similarity of vectors.

The BoW approach has some very good advantages:

1. Dictionaries can be trained offline. In real time applications, the more things you can do offline, the better the system is.
2. The search speed is swift. Small sized images can be completed at milliseconds. There are usually two auxiliary indicators of positive (direct index) and reverse (inverse index). The inverse index stores the weight and number of the image features arriving at the node, so that it can be used to quickly find similar images. The direct index with features of each image and its corresponding node is stored in the the parent node of a dictionary tree. It can be used for fast feature point matching (only need to match the parent node of the following words).
3. Many slam applications themselves need to compute feature points and descriptions, so they can be searched using features.
4. The author of ORBSLAM also used dictionary characteristics for fast feature selection, to reduce the time of feature matching needed (especially for large scale dataset).

Of course, it has its own disadvantages:

1. If the scenario is specific, we must train our own dictionary. A general dictionary is not very good.
2. BoW generally does not take into account the geometric relationships between features
3. If the application itself does not need to calculate the features, additional computational time is taken into account.
4. Like ORB SLAM, BoW is only used for fast selection of images, and subsequent verification and validation by other methods are required.
5. If the scene is characterized by little or repeated features, it is hard to use in the system.

## ConvNets

How about using deep learning to optimize the step that we use the detector to recognize the scene which it has been? The focus of loop closure is to judge the similarity of the two frames! That's the reason why we think we can use deep learning and CNN to improve it. Deep learning is really good at classification and recognition. 

# CNN Descriptor

Convolutional networks (ConvNets) currently set the state of the art in visual recognition. The aim of [Visual Geometry Group](http://www.robots.ox.ac.uk/~vgg/)  $^{[6]}$ project, VGG,  is to investigate how the ConvNet depth affects their accuracy in the large-scale image recognition setting. And a significant improvement on the prior-art configurations can be achieved by increasing the depth to 16-19 weight layers in VGG net, which is substantially deeper than what has been used in the prior art. Now VGG is one of the most common ConvNet architectures today thanks to its simplicity and effectiveness. 

So we can use the ConvNets, VGG net, to describe a image and retrieval it in a coordinate system, which is full of the "Img2Vec", skipping the step of image feature extraction. Because of the disadvantage of BoW noted above, we could use ConvNets to try to solve the problem.

The solution is as follows.

1. Select key frames in the frontend.
2. Extract the information for mapping. Traditionally we will still use feature points for tracking. Maybe we can use the ConvNets as a detector, like object detection with semantics.
3. For each key frame, we use the trained model of VGG net to translate the image into vector and store it in database.
4. The similarity checking for loop closure of two frames can be easily achieved  according to the vectors.



There are many advantages of the method.

1. The VGG model is perfectly trained by the team of Oxford Univeristy.
2. We reduce the process of building bag of words.
3. The system with bag of words needs too much time to load the BoW when initialization.



But there is a distinct drawback. Most technologies about SLAM using feature points for mapping, so only if we change the detector of the image in the frontend of the system, we will not extract the feature points anymore.

# Summary

In this paper, we sum up the details of loop closure from image feature. And we analyze the system of Bag of Words model in SLAM. The we propose a method that optimize loop closure using ConvNets to describe key frames. Obviously, we can solve the disadvantage of BoW. And next we will focus on using ConvNets to eliminate the feature detector by pixel.