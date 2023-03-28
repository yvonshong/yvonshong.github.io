---
title: 欧拉角、四元数、旋转矩阵、旋转向量的相互转换（C++、python）
date: 2023-03-23 20:00:00
categories: tech
toc: true
---

记录 C++(Eigen), Python(scipy)的旋转表达式之间的转换。

<!-- more -->
# C++ Eigen

## 欧拉角转其他

```cpp
// 初始化欧拉角
Eigen::Vector3d eulerAngle(roll,pitch,yaw);

// 欧拉角转旋转向量
Eigen::AngleAxisd rollAngle(roll, Eigen::Vector3d::UnitX()); 
Eigen::AngleAxisd pitchAngle(pitch, Eigen::Vector3d::UnitY()); 
Eigen::AngleAxisd yawAngle(yaw, Eigen::Vector3d::UnitZ()); 

Eigen::AngleAxisd rotation_vector = yawAngle * pitchAngle * rollAngle;

// 欧拉角转四元数
Eigen::Quaterniond q = yawAngle * pitchAngle * rollAngle;

// 欧拉角转旋转矩阵
Eigen::Matrix3d rotationMatrix = yawAngle * pitchAngle * rollAngle;
```


## 四元数转其他


```cpp
// 初始化四元数
Eigen::Quaterniond quaternion(w,x,y,z); // Halmiton!

// 四元数转旋转向量
Eigen::AngleAxisd rotation_vector(quaternion);

// 四元数转旋转矩阵
Eigen::Matrix3d rotationMatrix = quaternion.toRotationMatrix(); 
Eigen::Matrix3d rotationMatrix = quaternion.matrix(); 

// 四元数转欧拉角
Eigen::Vector3d eulerAngle=quaternion.matrix().eulerAngles(0,1,2);
```


## 旋转矩阵转其他


```cpp
// 初始化
Eigen::Matrix3d rotationMatrix;
rotationMatrix<<x_00,x_01,x_02,x_10,x_11,x_12,x_20,x_21,x_22;

// 旋转矩阵转旋转向量
Eigen::AngleAxisd rotationVector(rotationMatrix);
Eigen::AngleAxisd rotationVector = rotationMatrix;
rotationVector.fromRotationMatrix(rotationMatrix);

// 旋转矩阵转欧拉角
Eigen::Vector3f eulerAngle = rotationMatrix.eulerAngles(0, 1, 2);  

// 旋转矩阵转四元数
Eigen::Quaterniond quaternion(rotation_matrix);

```


## 旋转向量转其他

```cpp
// 初始化
Eigen::AngleAxisd rotationVector(rotationAngle, Eigen::Vector3d(x,y,z))
Eigen::AngleAxisd yawAngle(rotationAngle, Eigen::Vector3d::UnitZ());

// 旋转向量转欧拉角
Eigen::Vector3d eulerAngle=rotationVector.matrix().eulerAngles(0,1,2);

// 旋转向量转旋转矩阵
Eigen::Matrix3d rotationMatrix=rotationVector.matrix();
Eigen::Matrix3d rotationMatrix=rotationVector.toRotationMatrix();

// 旋转向量转四元数
Eigen::Quaterniond quaternion(rotationVector);
```


# Python scipy

[https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html) 

```python
from scipy.spatial.transform import Rotation as R 
# quaternion
quaternion = [0, 0, np.sin(np.pi/4), np.cos(np.pi/4)] # [x,y,z,w] JPL!
scipy_r = R.from_quat(quaternion) 

quaternion = scipy_r.as_quat() 

# rotation matrix
rotation_matrix = [[0, -1, 0],[1,0,0],[0,0,1]]
scipy_r = R.from_matrix(rotation_matrix) 

rotation_matrix = scipy_r.as_matrix() 

# rotation vector
rotation_vector = np.pi/2 * np.array([0, 0, 1])
scipy_r = R.from_rotvec(rotation_vector) 

rotation_vector = scipy_r.as_rotvec() 

# eular angle
eular_angle = [np.pi/4, 0, 0]
scipy_r = R.from_euler('zyx', eular_angle, degrees=True) 

euler_angle_degree = scipy_r.as_euler('zyx',degrees=True) 

```
