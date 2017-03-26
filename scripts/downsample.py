#!/usr/bin/env python
import os
import cv2
import numpy

hostname = 'cheng'
path = '/Users/' + hostname + '/Desktop/data/imgs'
dstPath = '/Users/' + hostname + '/Desktop/tensorflow/data/imgs_60x80'
os.makedirs(dstPath)
def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

print "on processing..."

for i in range(1, fcount(path) + 1):
    im = cv2.imread(path + '/image' + str(i) + '.jpg', -1)
    #im_new = cv2.pyrDown(im)
    im_new = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(path + '/image' + str(i) + '.jpg', im_new)
    print 'processing on image', str(i)
print 'current image resolution (height, width, number of channel):', im_new.shape
print "DONE"
