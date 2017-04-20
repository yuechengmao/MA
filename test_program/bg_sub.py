import tensorflow as tf
import numpy as np 
import random
from scipy.misc import imread
import cv2

img = np.empty((0, 350, 250), dtype=np.float32)
for i in range(0,10):
	img = img.astype(np.float32)
	frame = cv2.imread('./new_data/motion1/imgs/image' + str(i) + '.png', 0)
	img = np.append(img, np.expand_dims(frame,axis=0), axis=0)
	img_mean = np.mean(img, axis=0)
	img_mean = img_mean.astype(np.uint8)

cv2.imshow('image',img_mean)


cv2.destroyAllWindows()