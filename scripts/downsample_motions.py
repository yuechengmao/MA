#!/usr/bin/env python
import os
import cv2
import numpy

hostname = 'cheng'
path = '/Users/' + hostname + '/Desktop/data/motion'

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

print "on processing..."
for motion_num in range(1, 51):
    for i in range(1, fcount(path + str(motion_num) + '/imgs1/') + 1):
        im = cv2.imread(path + str(motion_num) + '/imgs1/cam1_' + str(i) + '.jpg', -1)
        im_new = cv2.pyrDown(im)
        im_new = cv2.cvtColor(im_new, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(path + str(motion_num) + '/imgs1/cam1_' + str(i) + '.jpg', im_new)
        print path + str(motion_num) + '/imgs1/cam1_' + str(i) + '.jpg'

    for i in range(1, fcount(path + str(motion_num) + '/imgs2/') + 1):
        im = cv2.imread(path + str(motion_num) + '/imgs2/cam2_' + str(i) + '.jpg', -1)
        im_new = cv2.pyrDown(im)
        im_new = cv2.cvtColor(im_new, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(path + str(motion_num) + '/imgs2/cam2_' + str(i) + '.jpg', im_new)
        print path + str(motion_num) + '/imgs2/cam2_' + str(i) + '.jpg'

    for i in range(1, fcount(path + str(motion_num) + '/imgs3/') + 1):
        im = cv2.imread(path + str(motion_num) + '/imgs3/cam3_' + str(i) + '.jpg', -1)
        im_new = cv2.pyrDown(im)
        im_new = cv2.cvtColor(im_new, cv2.COLOR_RGB2GRAY)
        cv2.imwrite(path + str(motion_num) + '/imgs3/cam3_' + str(i) + '.jpg', im_new)
        print path + str(motion_num) + '/imgs3/cam3_' + str(i) + '.jpg'

print 'current image resolution (height, width, number of channel):', im_new.shape
print "DONE"
