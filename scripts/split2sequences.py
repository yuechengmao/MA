#!/usr/bin/env python

import numpy as np
import os
import shutil
import glob
from scipy.misc import imread, imsave, imresize
from numpy import genfromtxt

numberOfmotions = 51
hostname = 'cheng'

srcPath = '/Users/' + hostname + '/Desktop/data/'

dstPath = '/Users/' + hostname + '/Desktop/tensorflow/sequences/'
trainPath = dstPath + 'train/'
testPath = dstPath + 'test/'

img_height = 30
img_width = 40

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

print "on processing..."
os.makedirs(dstPath)
os.makedirs(trainPath)
os.makedirs(testPath)
seq_cnt = 0
test_cnt = 0
for motion_cnt in range(1, 51):
    #cam1
    seq_length = np.random.random_integers(20)
    cnt = 0
    images = np.empty([0, img_height * img_width])
    data = genfromtxt(srcPath + 'motion' + str(motion_cnt) + '/data1.txt', delimiter=',')
    for i in range(fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs1/')):
        img = imread(srcPath + 'motion' + str(motion_cnt) + '/imgs1/cam1_' + str(i + 1) + '.jpg')
        img = img.flatten()
        img = np.expand_dims(img, axis=0)
        images = np.append(images, img, axis=0)
        cnt += 1
        print srcPath + 'motion' + str(motion_cnt) + '/imgs1/cam1_' + str(i + 1) + '.jpg'
        if cnt == seq_length:
            if motion_cnt == 8 or motion_cnt == 18 or motion_cnt == 28 or motion_cnt == 38 or motion_cnt == 48:
                test_cnt += 1
                np.savetxt(testPath + 'seq_img' + str(test_cnt) + '.csv', images, fmt='%.1f', delimiter=',')
                print 'Test image:' + 'seq_img' + str(test_cnt) + '.csv' + ', length:',images.shape[0]
                np.savetxt(testPath + 'seq_data' + str(test_cnt) + '.csv', data[i - seq_length + 1:i + 1,:], fmt='%.8f', delimiter=',')
                print 'Test data:' + 'seq_data' + str(test_cnt) + '.csv' + ', length:', i - seq_length + 1, '-', i + 1
            else:
                seq_cnt += 1
                np.savetxt(trainPath + 'seq_img' + str(seq_cnt) + '.csv', images, fmt='%.1f', delimiter=',')
                print 'Train image:' + 'seq_img' + str(seq_cnt) + '.csv' + ', length:',images.shape[0]
                np.savetxt(trainPath + 'seq_data' + str(seq_cnt) + '.csv', data[i - seq_length + 1:i + 1,:], fmt='%.8f', delimiter=',')
                print 'Train data:' + 'seq_data' + str(seq_cnt) + '.csv' + ', length:', i - seq_length + 1, '-', i + 1

            images = np.empty([0, img_height * img_width])
            seq_length = np.random.random_integers(20)
            if i + seq_length >= fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs1/'):
                seq_length = fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs1/') - i - 1
            cnt = 0

    #cam2
    seq_length = np.random.random_integers(20)
    cnt = 0
    images = np.empty([0, img_height * img_width])
    data = genfromtxt(srcPath + 'motion' + str(motion_cnt) + '/data2.txt', delimiter=',')
    for i in range(fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs2/')):
        img = imread(srcPath + 'motion' + str(motion_cnt) + '/imgs2/cam2_' + str(i + 1) + '.jpg')
        img = img.flatten()
        img = np.expand_dims(img, axis=0)
        images = np.append(images, img, axis=0)
        cnt += 1
        print srcPath + 'motion' + str(motion_cnt) + '/imgs2/cam2_' + str(i + 1) + '.jpg'
        if cnt == seq_length:
            if motion_cnt == 8 or motion_cnt == 18 or motion_cnt == 28 or motion_cnt == 38 or motion_cnt == 48:
                test_cnt += 1
                np.savetxt(testPath + 'seq_img' + str(test_cnt) + '.csv', images, fmt='%.1f', delimiter=',')
                print 'Test image:' + 'seq_img' + str(test_cnt) + '.csv' + ', length:',images.shape[0]
                np.savetxt(testPath + 'seq_data' + str(test_cnt) + '.csv', data[i - seq_length + 1:i + 1,:], fmt='%.8f', delimiter=',')
                print 'Test data:' + 'seq_data' + str(test_cnt) + '.csv' + ', length:', i - seq_length + 1, '-', i + 1
            else:
                seq_cnt += 1
                np.savetxt(trainPath + 'seq_img' + str(seq_cnt) + '.csv', images, fmt='%.1f', delimiter=',')
                print 'Train image:' + 'seq_img' + str(seq_cnt) + '.csv' + ', length:',images.shape[0]
                np.savetxt(trainPath + 'seq_data' + str(seq_cnt) + '.csv', data[i - seq_length + 1:i + 1,:], fmt='%.8f', delimiter=',')
                print 'Train data:' + 'seq_data' + str(seq_cnt) + '.csv' + ', length:', i - seq_length + 1, '-', i + 1

            images = np.empty([0, img_height * img_width])
            seq_length = np.random.random_integers(20)
            if i + seq_length >= fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs2/'):
                seq_length = fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs2/') - i - 1
            cnt = 0
    #cam3
    seq_length = np.random.random_integers(20)
    cnt = 0
    images = np.empty([0, img_height * img_width])
    data = genfromtxt(srcPath + 'motion' + str(motion_cnt) + '/data3.txt', delimiter=',')
    for i in range(fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs3/')):
        img = imread(srcPath + 'motion' + str(motion_cnt) + '/imgs3/cam3_' + str(i + 1) + '.jpg')
        img = img.flatten()
        img = np.expand_dims(img, axis=0)
        images = np.append(images, img, axis=0)
        cnt += 1
        print srcPath + 'motion' + str(motion_cnt) + '/imgs3/cam3_' + str(i + 1) + '.jpg'
        if cnt == seq_length:
            if motion_cnt == 8 or motion_cnt == 18 or motion_cnt == 28 or motion_cnt == 38 or motion_cnt == 48:
                test_cnt += 1
                np.savetxt(testPath + 'seq_img' + str(test_cnt) + '.csv', images, fmt='%.1f', delimiter=',')
                print 'Test image:' + 'seq_img' + str(test_cnt) + '.csv' + ', length:',images.shape[0]
                np.savetxt(testPath + 'seq_data' + str(test_cnt) + '.csv', data[i - seq_length + 1:i + 1,:], fmt='%.8f', delimiter=',')
                print 'Test data:' + 'seq_data' + str(test_cnt) + '.csv' + ', length:', i - seq_length + 1, '-', i + 1
            else:
                seq_cnt += 1
                np.savetxt(trainPath + 'seq_img' + str(seq_cnt) + '.csv', images, fmt='%.1f', delimiter=',')
                print 'Train image:' + 'seq_img' + str(seq_cnt) + '.csv' + ', length:',images.shape[0]
                np.savetxt(trainPath + 'seq_data' + str(seq_cnt) + '.csv', data[i - seq_length + 1:i + 1,:], fmt='%.8f', delimiter=',')
                print 'Train data:' + 'seq_data' + str(seq_cnt) + '.csv' + ', length:', i - seq_length + 1, '-', i + 1

            images = np.empty([0, img_height * img_width])
            seq_length = np.random.random_integers(20)
            if i + seq_length >= fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs3/'):
                seq_length = fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs3/') - i - 1
            cnt = 0
    #raw_input('press enter')




print 'DONE'

