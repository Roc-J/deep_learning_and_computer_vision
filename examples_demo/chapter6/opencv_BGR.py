#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
图像的表示
在python-opencv中，最常见的就是RGB三通道，但是在Opencv中，默认的图像表示却是相反的
图像用python的array表示，在opencv和matplotlib中显示的是不一样有

'''
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]]
], dtype=np.uint8)


plt.imsave('img_pyplot.jpg', img)
cv2.imwrite('img_cv2.jpg', img)