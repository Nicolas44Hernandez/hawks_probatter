#!/bin/bash

DNSMASQ_CONFIG_FILE="/etc/dnsmasq.conf"
HOSTAPD_CONFIG_FILE="/etc/hostapd/hostapd.conf"
INTERFACES_CONFIG_FILE="/etc/network/interfaces"
INIT_FILE="/etc/init.d/ap.sh"
RESOURCES=../resources


source ../variables/wlan-addr.env
echo "SETUP FOR RPI SERVER BOX"

echo "********STAGE 1: UPDATE AND UPGRADE SYSTEM ********"
sudo apt -y update
sudo apt -y upgrade


echo "********STAGE 2: INSTALL PACKAGES ********"
# general tools (35.8 MB)
sudo apt-get install -y build-essential cmake git pkg-config
# if you want to get OpenCV working in python or python3 (208 MB)
sudo apt-get install -y python3-dev python3-numpy python3-pip
# image formats (0.9 MB)
sudo apt-get install -y libjpeg-dev libpng-dev
# video formats (32.1 MB)
sudo apt-get install -y libavcodec-dev libavformat-dev
sudo apt-get install -y libswscale-dev libdc1394-22-dev
# video back engine (0.6 MB)
sudo apt-get install-y libv4l-dev v4l-utils
# the GTK+2 GUI (175 MB)
sudo apt-get install -y  libgtk2.0-dev libcanberra-gtk* libgtk-3-dev
# parallel framework (2.7 MB)
sudo apt-get install -y libtbb2 libtbb-dev


echo "********STAGE 3: DOWNLOAD OPENCV********"
cd ~
git clone --depth=1 https://github.com/opencv/opencv.git
cd opencv
mkdir build
cd build

echo "********STAGE 4: BUILD OPENCV********"
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D ENABLE_NEON=ON \
-D BUILD_ZLIB=ON \
-D BUILD_OPENMP=ON \
-D BUILD_TIFF=OFF \
-D BUILD_OPENJPEG=OFF \
-D BUILD_JASPER=OFF \
-D BUILD_OPENEXR=OFF \
-D BUILD_WEBP=OFF \
-D BUILD_TBB=ON \
-D BUILD_IPP_IW=OFF \
-D BUILD_ITT=OFF \
-D WITH_OPENMP=ON \
-D WITH_OPENCL=OFF \
-D WITH_AVFOUNDATION=OFF \
-D WITH_CAP_IOS=OFF \
-D WITH_CAROTENE=OFF \
-D WITH_CPUFEATURES=OFF \
-D WITH_EIGEN=OFF \
-D WITH_GSTREAMER=ON \
-D WITH_GTK=ON \
-D WITH_IPP=OFF \
-D WITH_HALIDE=OFF \
-D WITH_VULKAN=OFF \
-D WITH_INF_ENGINE=OFF \
-D WITH_NGRAPH=OFF \
-D WITH_JASPER=OFF \
-D WITH_OPENJPEG=OFF \
-D WITH_WEBP=OFF \
-D WITH_OPENEXR=OFF \
-D WITH_TIFF=OFF \
-D WITH_OPENVX=OFF \
-D WITH_GDCM=OFF \
-D WITH_TBB=ON \
-D WITH_HPX=OFF \
-D WITH_EIGEN=OFF \
-D WITH_V4L=ON \
-D WITH_LIBV4L=ON \
-D WITH_VTK=OFF \
-D WITH_QT=OFF \
-D BUILD_opencv_python3=ON \
-D BUILD_opencv_java=OFF \
-D BUILD_opencv_gapi=OFF \
-D BUILD_opencv_objc=OFF \
-D BUILD_opencv_js=OFF \
-D BUILD_opencv_ts=OFF \
-D BUILD_opencv_dnn=OFF \
-D BUILD_opencv_calib3d=OFF \
-D BUILD_opencv_objdetect=OFF \
-D BUILD_opencv_stitching=OFF \
-D BUILD_opencv_ml=OFF \
-D BUILD_opencv_world=OFF \
-D BUILD_EXAMPLES=OFF \
-D PYTHON3_PACKAGES_PATH=/usr/lib/python3/dist-packages \
-D OPENCV_ENABLE_NONFREE=OFF \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=OFF ..


echo "********STAGE 5: COMPILE OPENCV ********"
make -j$(nproc)

echo "********STAGE 6: INSTALL OPENCV ********"
sudo make install
sudo ldconfig
sudo apt-get update

echo "********STAGE 7: REMOVE OPENCV FOLDER ********"
cd ~
$ sudo rm -rf opencv