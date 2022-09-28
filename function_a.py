#For detail Explanation watch prime video: video link 
#How to save image or NumPy array as image
#Save Numpy Array
 
import cv2
import numpy as np
import os
 
rand_array = np.random.randint(255, size = (300,600,3))
 
cv2.imwrite("rand_np_array.png", rand_array) # imwrite(filename, img[, params])
 
img = cv2.imread("rand_np_array.png")
cv2.imshow('image', img)
 
cv2.waitKey(0)
cv2.destroyAllWindows()

#save image
img_path = '/home/intozi/Downloads/pexels-ian-turnell-709552.jpg'
img = cv2.imread(img_path)
cv2.imshow('image',img)
cv2.imwrite("/home/intozi/Downloads/pexels-ian-turnell-709552.png",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#save images from video



video_path = r"/home/intozi/Downloads/Old Songs Mashup - 20 Songs On ONE CHORD - Siddharth Slathia - Pehchan Music (1).mp4"
 
os.mkdir("video_to_image2") # create directory
 
cap = cv2.VideoCapture(video_path) # capture video
 
img_count = 1
while cap.isOpened():
    ret, frame = cap.read() # read video frame
     
    if not ret:
        print("Unable to read frame")
        break
     
    is_img_write = cv2.imwrite(f"video_to_image2\image{img_count}.jpeg", frame)
     
    if is_img_write:
        print(f'image save at video_to_image2\image{img_count}.jpeg')
         
    cv2.imshow("video", frame )
     
    cv2.waitKey(25) & 0xff == ord('q')
    img_count += 1
     
cap.release()
cv2.destroyAllWindows()