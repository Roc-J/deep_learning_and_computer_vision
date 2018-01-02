
# coding: utf-8

# ## 制作延时摄影视频的小例子
# 
# 视频中　从视频设备采集图片或者视频，或读取视频文件并从中采样。
# 
# 比较重要的有两个模块，一个是VideoCapture，用于获取相机设备并捕获图像和视频，或从文件中捕获，还有另外一个是VideoWriter，用于生成视频。

# In[6]:


import cv2
import time

interval = 2
num_frame = 30
out_fps = 24


# In[7]:


# VideoCapture(0)表示打开默认的相机
cap = cv2.VideoCapture(0)

size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))


# In[8]:


# 保存视频编码
video = cv2.VideoWriter("time_lapse.avi", cv2.cv.CV_FOURCC('M','P','4','2'),out_fps, size)


# In[9]:


for i in range(42):
    cap.read()
    
try:
    for i in range(num_frame):
        _, frame = cap.read()
        video.write(frame)
        print('Frame {} is captured.'.format(i))
        time.sleep(interval)
except KeyboardInterrupt:
    print('stopped! {}/{} frames captured!'.format(i, num_frame))
    
video.release()
cap.release()

