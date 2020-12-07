import os
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import tifffile
import cv2
from libtiff import TIFF
root = r'F:/weixindownload'
val_path = os.path.join(root, 'nanjing.tif')
#img = cv2.imread("nanjing.tif",2)
#with open(root,"wb") as f:

tif = TIFF.open('nanjing.tif',mode='r')
img = tif.read_image()
for x in range(img.shape[0]):
    for y in range(img.shape[1]):
        if img[x,y]<0:
            img[x,y]=0
        else:
            img[x,y] = img[x,y] * 255.0
           # print(img[x,y])

#print(img)
print(img.shape)
img = img.astype(np.uint8)
# print(img)
print(img.dtype)
print(img.min())
print(img.max())
cv2.namedWindow("Image",0)
#cv2.resizeWindow('Image')
cv2.imshow("Image",img)
cv2.waitKey(0)
#释放窗口
cv2.destroyAllWindows() 
