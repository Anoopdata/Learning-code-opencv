#Create Video From Images Or NumPy Array Using Python OpenCV | OpenCV Tutorial
#Video From NumPy Array
"""import numpy as np
import cv2
import os
 
width = 1280
height = 720
channel = 3
 
fps = 30
sec = 5
 
# Syntax: VideoWriter_fourcc(c1, c2, c3, c4) # Concatenates 4 chars to a fourcc code
#  cv2.VideoWriter_fourcc('M','J','P','G') or cv2.VideoWriter_fourcc(*'MJPG)
 
fourcc = cv2.VideoWriter_fourcc(*'MP42') # FourCC is a 4-byte code used to specify the video codec.
# A video codec is software or hardware that compresses and decompresses digital video. 
# In the context of video compression, codec is a portmanteau of encoder and decoder, 
# while a device that only compresses is typically called an encoder, and one that only 
# decompresses is a decoder. Source - Wikipedia
 
#Syntax: cv2.VideoWriter( filename, fourcc, fps, frameSize )
video = cv2.VideoWriter('test.mp4', fourcc, float(fps), (width, height))
 
for frame_count in range(fps*sec):
    img = np.random.randint(0,255, (height, width, channel), dtype = np.uint8)
    video.write(img)"""
 
# video.release()

#Video from Images

import numpy as np
import cv2
import os
 
width = 1280
hieght = 720
channel = 3
 
fps = 10
sec = 5
 
fourcc = cv2.VideoWriter_fourcc(*'MP42')
 
video = cv2.VideoWriter('image_to_video.avi', fourcc, float(fps), (width, hieght))
 
directry = r'/home/intozi/Downloads/Intozi_code/video_to_image'
 
img_name_list = os.listdir(directry)
 
for frame_count in range(fps*sec):
    
    img_name = np.random.choice(img_name_list)
    img_path = os.path.join(directry, img_name)
    img = cv2.imread(img_path)
    img_resize = cv2.resize(img, (width, hieght))
     
video.write(img_resize)  

video.release()