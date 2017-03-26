#!/usr/bin/env python

import numpy as np
import os
import shutil
import glob
import linecache

numberOfmotions = 51
hostname = 'cheng'

srcPath = '/Users/' + hostname + '/Desktop/data/'
cntPath = '/Users/' + hostname + '/Desktop/data/'

dstPath = '/Users/' + hostname + '/Desktop/tensorflow/data_40x5x5/'
trainPath = dstPath + 'training_set_240x320_masked_diff/'
validationPath = dstPath + 'validation_set_240x320_masked_diff/'
testPath = dstPath + 'test_set_240x320_masked_diff/'
def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

print "on processing..."
#os.makedirs(dstPath)

#os.makedirs(trainPath)
#os.makedirs(validationPath)
#os.makedirs(testPath)
#destination txt path
train_txt = open(dstPath + 'train.txt', 'w+')
validation_txt = open(dstPath + 'validation.txt', 'w+')
test_txt = open(dstPath + 'test.txt', 'w+')
train_pos = open(dstPath + 'train_pos.txt', 'w+')
validation_pos = open(dstPath + 'validation_pos.txt', 'w+')
test_pos = open(dstPath + 'test_pos.txt', 'w+')
for motion_cnt in range(1, 51):

    if motion_cnt == 2 or motion_cnt == 12 or motion_cnt == 22 or motion_cnt == 32 or motion_cnt == 42:
        start_img_cnt = fcount(validationPath)
        for i in range(1, fcount(cntPath + 'motion' + str(motion_cnt) + '/imgs1/') + 1):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(i) + '.png', validationPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data1.txt', i)
            validation_txt.write(line)
            line_pos = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/position1.csv', i)
            validation_pos.write(line_pos)

            print 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(i) + '.png' + ' VALIDATION'
            print line
        start_img_cnt = fcount(validationPath)
        for i in range(1, fcount(cntPath + 'motion' + str(motion_cnt) + '/imgs2/') + 1):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(i) + '.png', validationPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data2.txt', i)
            validation_txt.write(line)
            line_pos = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/position2.csv', i)
            validation_pos.write(line_pos)

            print 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(i) + '.png' + ' VALIDATION'
            print line
        start_img_cnt = fcount(validationPath)
        for i in range(1, fcount(cntPath + 'motion' + str(motion_cnt) + '/imgs3/') + 1):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(i) + '.png', validationPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data3.txt', i)
            validation_txt.write(line)
            line_pos = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/position3.csv', i)
            validation_pos.write(line_pos)

            print 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(i) + '.png' + ' VALIDATION'
            print line
    elif motion_cnt == 8 or motion_cnt == 18 or motion_cnt == 28 or motion_cnt == 38 or motion_cnt == 48:
        start_img_cnt = fcount(testPath)
        for i in range(1, fcount(cntPath + 'motion' + str(motion_cnt) + '/imgs1/') + 1):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(i) + '.png', testPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data1.txt', i)
            test_txt.write(line)
            line_pos = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/position1.csv', i)
            test_pos.write(line_pos)

            print 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(i) + '.png' + ' TEST'
            print line
        start_img_cnt = fcount(testPath)
        for i in range(1, fcount(cntPath + 'motion' + str(motion_cnt) + '/imgs2/') + 1):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(i) + '.png', testPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data2.txt', i)
            test_txt.write(line)
            line_pos = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/position2.csv', i)
            test_pos.write(line_pos)

            print 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(i) + '.png' + ' TEST'
            print line
        start_img_cnt = fcount(testPath)
        for i in range(1, fcount(cntPath + 'motion' + str(motion_cnt) + '/imgs3/') + 1):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(i) + '.png', testPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data3.txt', i)
            test_txt.write(line)
            line_pos = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/position3.csv', i)
            test_pos.write(line_pos)

            print 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(i) + '.png' + ' TEST'
            print line
    else:
        start_img_cnt = fcount(trainPath)
        for i in range(1, fcount(cntPath + 'motion' + str(motion_cnt) + '/imgs1/') + 1):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(i) + '.png', trainPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data1.txt', i)
            train_txt.write(line)
            line_pos = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/position1.csv', i)
            train_pos.write(line_pos)

            print 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(i) + '.png' + ' TRAIN'
            print line
        start_img_cnt = fcount(trainPath)
        for i in range(1, fcount(cntPath + 'motion' + str(motion_cnt) + '/imgs2/') + 1):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(i) + '.png', trainPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data2.txt', i)
            train_txt.write(line)
            line_pos = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/position2.csv', i)
            train_pos.write(line_pos)

            print 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(i) + '.png' + ' TRAIN'
            print line
        start_img_cnt = fcount(trainPath)
        for i in range(1, fcount(cntPath + 'motion' + str(motion_cnt) + '/imgs3/') + 1):
            #shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(i) + '.png', trainPath + 'image' + str(i + start_img_cnt) + '.png')
            line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data3.txt', i)
            train_txt.write(line)
            line_pos = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/position3.csv', i)
            train_pos.write(line_pos)

            print 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(i) + '.png' + ' TRAIN'
            print line



train_txt.close()
validation_txt.close()
test_txt.close()

train_pos.close()
validation_pos.close()
test_pos.close()

print 'DONE'

