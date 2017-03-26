#!/usr/bin/env python

import numpy as np
import os
import shutil
import glob

numberOfmotions = 51
hostname = 'cheng'

print "on processing..."


numberOftextfile = (numberOfmotions - 1)*3 + 1

srcPath = '/Users/' + hostname + '/Desktop/data/'
dstPath = '/Users/' + hostname + '/Desktop/motions/'

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count
os.makedirs(dstPath)
motion_cnt = 0

for i in range(1, numberOfmotions):
    motion_cnt += 1
    os.makedirs(dstPath + str(motion_cnt))
    os.makedirs(dstPath + str(motion_cnt) + '/imgs')
    shutil.copy(srcPath + 'motion' + str(i) + '/data1.txt', dstPath + str(motion_cnt) + '/data' + '.txt')
    print srcPath + 'motion' + str(i) + '/data1.txt' + 'TO' + str(motion_cnt) + '/data' + '.txt'
    for img_cnt in range(1, fcount(srcPath + 'motion' + str(i) + '/imgs1') + 1):
        shutil.copy(srcPath + 'motion' + str(i) + '/imgs1/cam1_' + str(img_cnt)  + '.jpg', dstPath + str(motion_cnt) + '/imgs/image' + str(img_cnt) + '.jpg')

    motion_cnt += 1
    os.makedirs(dstPath + str(motion_cnt))
    os.makedirs(dstPath + str(motion_cnt) + '/imgs')
    shutil.copy(srcPath + 'motion' + str(i) + '/data2.txt', dstPath + str(motion_cnt) + '/data' + '.txt')
    print srcPath + 'motion' + str(i) + '/data2.txt' + 'TO' + str(motion_cnt) + '/data' + '.txt'
    for img_cnt in range(1, fcount(srcPath + 'motion' + str(i) + '/imgs2') + 1):
        shutil.copy(srcPath + 'motion' + str(i) + '/imgs2/cam2_' + str(img_cnt)  + '.jpg', dstPath + str(motion_cnt) + '/imgs/image' + str(img_cnt) + '.jpg')

    motion_cnt += 1
    os.makedirs(dstPath + str(motion_cnt))
    os.makedirs(dstPath + str(motion_cnt) + '/imgs')
    shutil.copy(srcPath + 'motion' + str(i) + '/data3.txt', dstPath + str(motion_cnt) + '/data' + '.txt')
    print srcPath + 'motion' + str(i) + '/data3.txt' + 'TO' + str(motion_cnt) + '/data' + '.txt'
    for img_cnt in range(1, fcount(srcPath + 'motion' + str(i) + '/imgs3') + 1):
        shutil.copy(srcPath + 'motion' + str(i) + '/imgs3/cam3_' + str(img_cnt)  + '.jpg', dstPath + str(motion_cnt) + '/imgs/image' + str(img_cnt) + '.jpg')

print "DONE"

