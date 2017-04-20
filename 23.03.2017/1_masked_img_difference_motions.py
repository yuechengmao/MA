#!/usr/bin/env python
import os
import cv2
import numpy as np
import shutil

hostname = 'cheng'

shutil.copytree('/Users/' + hostname + '/Desktop/data', '/Users/' + hostname + '/Desktop/masked_data_diffimg')



dstpath = '/Users/' + hostname + '/Desktop/masked_data_diffimg/motion'
def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

print "on processing..."

for motion_num in range(1, 51):

    fgbg = cv2.BackgroundSubtractorMOG()
    for i in range(1, fcount(dstpath + str(motion_num) + '/imgs1/') + 1):
        im = cv2.imread(dstpath + str(motion_num) + '/imgs1/cam1_' + str(i) + '.jpg', -1)
        fgmask = fgbg.apply(im,learningRate=0.03)
        #im_new = np.multiply(im,fgmask)
        cv2.imwrite(dstpath + str(motion_num) + '/imgs1/cam1_' + str(i) + '.png', fgmask)
        print dstpath + str(motion_num) + '/imgs1/cam1_' + str(i) + '.png'


    fgbg = cv2.BackgroundSubtractorMOG()
    for i in range(1, fcount(dstpath + str(motion_num) + '/imgs2/') + 1):
        im = cv2.imread(dstpath + str(motion_num) + '/imgs2/cam2_' + str(i) + '.jpg', -1)
        fgmask = fgbg.apply(im,learningRate=0.03)
        #im_new = np.multiply(im,fgmask)
        cv2.imwrite(dstpath + str(motion_num) + '/imgs2/cam2_' + str(i) + '.png', fgmask)
        print dstpath + str(motion_num) + '/imgs2/cam2_' + str(i) + '.png'


    fgbg = cv2.BackgroundSubtractorMOG()
    for i in range(1, fcount(dstpath + str(motion_num) + '/imgs3/') + 1):
        im = cv2.imread(dstpath + str(motion_num) + '/imgs3/cam3_' + str(i) + '.jpg', -1)
        fgmask = fgbg.apply(im,learningRate=0.03)
        #im_new = np.multiply(im,fgmask)
        cv2.imwrite(dstpath + str(motion_num) + '/imgs3/cam3_' + str(i) + '.png', fgmask)
        print dstpath + str(motion_num) + '/imgs3/cam3_' + str(i) + '.png'


print "DONE"
