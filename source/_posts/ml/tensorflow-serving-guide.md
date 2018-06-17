---
title: tensorflow serving deploy tutorial
date: 2017-08-23 19:05:39
categories: code
tags: 
- ml
- tf
toc: true
---

tensorflow serving 部署教程

<!-- more -->

Server-end：
	1. Install tenserflow using anaconda (Python 3.5 & tensorflow with GPU support) (official tutorial: https://www.tensorflow.org/install/install_linux) (Chinese tutorial: http://www.linuxdiyf.com/linux/25614.html)
		a. Install anaconda
		b. conda create -n tensorflow python=3.5
		c. activate tensorflow
		d. Install NVIDIA driver for GPU with the `sudo service lightdm stop` and ban the Intel Driver  (tutorial: https://gist.github.com/dangbiao1991/7825db1d17df9231f4101f034ecd5a2b )
			i. go to the official website to download the correct driver (.run file) for you GPU
			ii. Enter the command when set up your computer with Ctrl+Alt+F1
			iii. stop the desktop service `sudo service lightdm stop`
			iv. Uninstall the whole old driver
			v. Add the nouveau(the embedded driver) to blacklist
			vi. Forbidden the nouveau module
			vii. Reboot
			viii. Install the NVIDIA-Driver.run with command when set up
		e. Install cuda toolkit
			i. Move to /usr/local/cuda
		f. Install cudnn
			i. Move to /usr/local/cuda
		g. Export the path
			export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"
export CUDA_HOME=/usr/local/cuda
		h. pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/gpu/tensorflow_gpu-1.3.0-cp35-cp35m-win_amd64.whl
	2. Install serving (official tutorial: https://www.tensorflow.org/serving/setup#installing_using_apt-get )
		a. Installing using apt-get
			i. sudo apt-get remove tensorflow-model-server
			ii. echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | sudo tee /etc/apt/sources.list.d/tensorflow-serving.list
			iii. curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | sudo apt-key add -
			iv. sudo apt-get update && sudo apt-get install tensorflow-model-server
			v. sudo apt-get upgrade tensorflow-model-server
	3. Serving a model on server
		a. Using python script with export function to product the model.pb (proto buffer)
			i. python tensorflow_serving/example/mnist_saved_model.py /tmp/mnist_model
		b. Load exported model on the server
			i. tensorflow_model_server --port=9000 --model_name=mnist --model_base_path=/tmp/mnist_model/


Client-end:
	1. Python
		a. Install python 2.7 environment with anaconda
		b. python tensorflow_serving/example/mnist_client.py --num_tests=1000 --server=localhost:9000
	2. Cpp
		a. Linux environment:
			i. Build the system include tensorflow packages.
		b. Win environment:
			i. Tensorflow could't build the exe and lib on Windows.
		
		
		
