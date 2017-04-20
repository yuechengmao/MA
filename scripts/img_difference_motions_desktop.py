#!/usr/bin/env python
import os
import cv2
import numpy
import shutil

hostname = 'cheng'

shutil.copytree('/Users/' + hostname + '/Desktop/data', '/Users/' + hostname + '/Desktop/data_diffimg')



dstpath = '/Users/' + hostname + '/Desktop/data_diffimg/motion'
def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

print "on processing..."

for motion_num in range(1, 51):
    im0 = cv2.imread(dstpath + str(motion_num) + '/imgs1/cam1_1' + '.jpg', -1)
    im0 = im0/1.0
    for i in range(1, fcount(dstpath + str(motion_num) + '/imgs1/') + 1):
        im = cv2.imread(dstpath + str(motion_num) + '/imgs1/cam1_' + str(i) + '.jpg', -1)
        im = im/1.0
        im_new = im - im0
        im_new[im_new<0] = 0
        im0 = im
        cv2.imwrite(dstpath + str(motion_num) + '/imgs1/cam1_' + str(i) + '.jpg', im_new)
        print dstpath + str(motion_num) + '/imgs1/cam1_' + str(i) + '.jpg'

    im0 = cv2.imread(dstpath + str(motion_num) + '/imgs2/cam2_1' + '.jpg', -1)
    im0 = im0/1.0
    for i in range(1, fcount(dstpath + str(motion_num) + '/imgs2/') + 1):
        im = cv2.imread(dstpath + str(motion_num) + '/imgs2/cam2_' + str(i) + '.jpg', -1)
        im = im/1.0
        im_new = im - im0
        im_new[im_new<0] = 0
        im0 = im
        cv2.imwrite(dstpath + str(motion_num) + '/imgs2/cam2_' + str(i) + '.jpg', im_new)
        print dstpath + str(motion_num) + '/imgs2/cam2_' + str(i) + '.jpg'

    im0 = cv2.imread(dstpath + str(motion_num) + '/imgs3/cam3_1' + '.jpg', -1)
    im0 = im0/1.0
    for i in range(1, fcount(dstpath + str(motion_num) + '/imgs3/') + 1):
        im = cv2.imread(dstpath + str(motion_num) + '/imgs3/cam3_' + str(i) + '.jpg', -1)
        im = im/1.0
        im_new = im - im0
        im_new[im_new<0] = 0
        im0 = im
        cv2.imwrite(dstpath + str(motion_num) + '/imgs3/cam3_' + str(i) + '.jpg', im_new)
        print dstpath + str(motion_num) + '/imgs3/cam3_' + str(i) + '.jpg'

print 'current image resolution (height, width, number of channel):', im_new.shape
print "DONE"
