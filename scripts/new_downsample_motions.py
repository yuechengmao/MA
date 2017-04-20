#!/usr/bin/env python
import os
import cv2
import numpy
from PIL import Image

hostname = 'cheng'
path = '/Users/' + hostname + '/Desktop/new_data/motion'

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

print "on processing..."
for motion_num in range(1, 51):
    for i in range(fcount(path + str(motion_num) + '/imgs/')):
        im = cv2.imread(path + str(motion_num) + '/imgs/image' + str(i) + '.png', -1)

        crop_img = im[0:350, 330:580] # Crop from x, y, w, h -> 100, 200, 300, 400
        # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
        #im_new = cv2.pyrDown(im)
        #im_new = cv2.cvtColor(im_new, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(path + str(motion_num) + '/imgs/image' + str(i) + '.png', crop_img)
        print path + str(motion_num) + '/imgs/image' + str(i) + '.png'

print 'current image resolution (height, width, number of channel):', crop_img.shape
print "DONE"
