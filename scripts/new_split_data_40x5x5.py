#!/usr/bin/env python

import numpy as np
import os
import shutil
import glob
import linecache

numberOfmotions = 51
hostname = 'cheng'

srcPath = '/Users/' + hostname + '/Desktop/new_data/'

dstPath = '/Users/' + hostname + '/Desktop/new_tensorflow/data_cropped/'
trainPath = dstPath + 'train_set/'
validationPath = dstPath + 'validation_set/'
testPath = dstPath + 'test_set/'
def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

print "on processing..."
'''
os.makedirs(dstPath)
os.makedirs(trainPath)
os.makedirs(validationPath)
os.makedirs(testPath)
'''
#destination csv path
train_csv = open(dstPath + 'train.csv', 'w+')
validation_csv = open(dstPath + 'validation.csv', 'w+')
test_csv = open(dstPath + 'test.csv', 'w+')

for motion_cnt in range(1, 51):

    if motion_cnt == 2 or motion_cnt == 12 or motion_cnt == 22 or motion_cnt == 32 or motion_cnt == 42:
        start_img_cnt = fcount(validationPath)
        for i in range(fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs/')):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs/' + 'image' + str(i) + '.png', validationPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data.csv', i+1)
            validation_csv.write(line)

            print 'motion' + str(motion_cnt) + '/imgs/' + 'image' + str(i) + '.png' + ' VALIDATION'
            print line
    elif motion_cnt == 8 or motion_cnt == 18 or motion_cnt == 28 or motion_cnt == 38 or motion_cnt == 48:
        start_img_cnt = fcount(testPath)
        for i in range(fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs/')):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs/' + 'image' + str(i) + '.png', testPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data.csv', i+1)
            test_csv.write(line)

            print 'motion' + str(motion_cnt) + '/imgs/' + 'image' + str(i) + '.png' + ' TEST'
            print line
    else:
        start_img_cnt = fcount(trainPath)
        for i in range(fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs/')):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs/' + 'image' + str(i) + '.png', trainPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data.csv', i+1)
            train_csv.write(line)

            print 'motion' + str(motion_cnt) + '/imgs/' + 'image' + str(i) + '.png' + ' TRAIN'
            print line

train_csv.close()
validation_csv.close()
test_csv.close()


print 'DONE'

