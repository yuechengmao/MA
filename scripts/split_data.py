#!/usr/bin/env python

import numpy as np
import os
import shutil
import glob
import linecache

numberOfmotions = 51
hostname = 'cheng'

srcPath = '/Users/' + hostname + '/Desktop/data/'

dstPath = '/Users/' + hostname + '/Desktop/tensorflow/data_set/'
trainPath = dstPath + 'training_set/'
validationPath = dstPath + 'validation_set/'
testPath = dstPath + 'test_set/'
def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

print "on processing..."
os.makedirs(dstPath)
os.makedirs(trainPath)
os.makedirs(validationPath)
os.makedirs(testPath)
#destination txt path
train_txt = open(dstPath + 'train.txt', 'w+')
validation_txt = open(dstPath + 'validation.txt', 'w+')
test_txt = open(dstPath + 'test.txt', 'w+')

for motion_cnt in range(1, 51):
    #cam1
    img_cnt = np.arange(1, fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs1/') + 1)
    np.random.shuffle(img_cnt)
    training_img = img_cnt[0:300]
    validation_img = img_cnt[300:390]
    test_img = img_cnt[390:]

    start_img_cnt = fcount(trainPath)
    for i in range(len(training_img)):
        shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(training_img[i]) + '.jpg', trainPath + 'image' + str(i + start_img_cnt + 1) + '.jpg')
        line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data1.txt', training_img[i])
        train_txt.write(line)

        print 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(training_img[i]) + '.jpg'
        print line
    start_img_cnt = fcount(validationPath)
    for i in range(len(validation_img)):
        shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(validation_img[i]) + '.jpg', validationPath + 'image' + str(i + start_img_cnt + 1) + '.jpg')
        line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data1.txt', validation_img[i])
        validation_txt.write(line)

        print 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(validation_img[i]) + '.jpg'
        print line
    start_img_cnt = fcount(testPath)
    for i in range(len(test_img)):
        shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(test_img[i]) + '.jpg', testPath + 'image' + str(i + start_img_cnt + 1) + '.jpg')
        line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data1.txt', test_img[i])
        test_txt.write(line)

        print 'motion' + str(motion_cnt) + '/imgs1/' + 'cam1_' + str(test_img[i]) + '.jpg'
        print line

    #cam2
    img_cnt = np.arange(1, fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs2/') + 1)
    np.random.shuffle(img_cnt)
    training_img = img_cnt[0:300]
    validation_img = img_cnt[300:390]
    test_img = img_cnt[390:]

    start_img_cnt = fcount(trainPath)
    for i in range(len(training_img)):
        shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(training_img[i]) + '.jpg', trainPath + 'image' + str(i + start_img_cnt + 1) + '.jpg')
        line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data2.txt', training_img[i])
        train_txt.write(line)

        print 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(training_img[i]) + '.jpg'
        print line
    start_img_cnt = fcount(validationPath)
    for i in range(len(validation_img)):
        shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(validation_img[i]) + '.jpg', validationPath + 'image' + str(i + start_img_cnt + 1) + '.jpg')
        line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data2.txt', validation_img[i])
        validation_txt.write(line)

        print 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(validation_img[i]) + '.jpg'
        print line
    start_img_cnt = fcount(testPath)
    for i in range(len(test_img)):
        shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(test_img[i]) + '.jpg', testPath + 'image' + str(i + start_img_cnt + 1) + '.jpg')
        line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data2.txt', test_img[i])
        test_txt.write(line)

        print 'motion' + str(motion_cnt) + '/imgs2/' + 'cam2_' + str(test_img[i]) + '.jpg'
        print line
    #cam3
    img_cnt = np.arange(1, fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs3/') + 1)
    np.random.shuffle(img_cnt)
    training_img = img_cnt[0:300]
    validation_img = img_cnt[300:390]
    test_img = img_cnt[390:]

    start_img_cnt = fcount(trainPath)
    for i in range(len(training_img)):
        shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(training_img[i]) + '.jpg', trainPath + 'image' + str(i + start_img_cnt + 1) + '.jpg')
        line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data3.txt', training_img[i])
        train_txt.write(line)

        print 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(training_img[i]) + '.jpg'
        print line
    start_img_cnt = fcount(validationPath)
    for i in range(len(validation_img)):
        shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(validation_img[i]) + '.jpg', validationPath + 'image' + str(i + start_img_cnt + 1) + '.jpg')
        line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data3.txt', validation_img[i])
        validation_txt.write(line)

        print 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(validation_img[i]) + '.jpg'
        print line
    start_img_cnt = fcount(testPath)
    for i in range(len(test_img)):
        shutil.copy(srcPath + 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(test_img[i]) + '.jpg', testPath + 'image' + str(i + start_img_cnt + 1) + '.jpg')
        line = linecache.getline(srcPath + 'motion' + str(motion_cnt) +'/data3.txt', test_img[i])
        test_txt.write(line)

        print 'motion' + str(motion_cnt) + '/imgs3/' + 'cam3_' + str(test_img[i]) + '.jpg'
        print line


train_txt.close()
validation_txt.close()
test_txt.close()

print 'DONE'

