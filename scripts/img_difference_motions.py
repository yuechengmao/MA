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
    im0 = cv2.imread(path + str(motion_num) + '/imgs1/cam1_1' + '.jpg', 0)
    im0 = im0/255.0
    for i in range(1, fcount(path + str(motion_num) + '/imgs1/') + 1):
        im = cv2.imread(path + str(motion_num) + '/imgs1/cam1_' + str(i+100) + '.jpg', 0)
        im = im/255.0
        im_new = im - im0

        im0 = im
        numpy.savetxt('/Users/' + hostname + '/Desktop' + '/motion1/cam1_' + str(i) + '.csv', im_new, delimiter=',')
        print path + str(motion_num) + '/imgs1/cam1_' + str(i) + '.csv'
        raw_input('press enter')
    im0 = cv2.imread(path + str(motion_num) + '/imgs2/cam2_1' + '.jpg', -1)
    for i in range(1, fcount(path + str(motion_num) + '/imgs2/') + 1):
        im = cv2.imread(path + str(motion_num) + '/imgs2/cam2_' + str(i) + '.jpg', -1)
        im_new = im - im0
        im0 = im
        cv2.imwrite(path + str(motion_num) + '/imgs2/cam2_' + str(i) + '.jpg', im_new)
        print path + str(motion_num) + '/imgs2/cam2_' + str(i) + '.jpg'
    im0 = cv2.imread(path + str(motion_num) + '/imgs3/cam3_1' + '.jpg', -1)
    for i in range(1, fcount(path + str(motion_num) + '/imgs3/') + 1):
        im = cv2.imread(path + str(motion_num) + '/imgs3/cam3_' + str(i) + '.jpg', -1)
        im_new = im - im0
        im0 = im
        cv2.imwrite(path + str(motion_num) + '/imgs3/cam3_' + str(i) + '.jpg', im_new)
        print path + str(motion_num) + '/imgs3/cam3_' + str(i) + '.jpg'

print 'current image resolution (height, width, number of channel):', im_new.shape
print "DONE"
