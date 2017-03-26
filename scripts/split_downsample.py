#!/usr/bin/env python
import os
import cv2
import numpy

hostname = 'cheng'

srcTrain = '/Users/' + hostname + '/Desktop/tensorflow/data_set/train_set/'
srcValidation = '/Users/' + hostname + '/Desktop/tensorflow/data_set/validation_set/'
srcTest = '/Users/' + hostname + '/Desktop/tensorflow/data_set/test_set/'

trainPath = '/Users/' + hostname + '/Desktop/tensorflow/data_set/train_240x320/'
validationPath = '/Users/' + hostname + '/Desktop/tensorflow/data_set/validation_240x320/'
testPath = '/Users/' + hostname + '/Desktop/tensorflow/data_set/test_240x320/'

'''
srcTrain = trainPath
srcValidation = validationPath
srcTest = testPath
'''
def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

os.makedirs(trainPath)
os.makedirs(validationPath)
os.makedirs(testPath)

print "on processing..."

for i in range(1, fcount(srcTrain) + 1):
    im = cv2.imread(srcTrain + 'image' + str(i) + '.jpg', -1)
    im_new = cv2.pyrDown(im)
    cv2.imwrite(trainPath + 'image' + str(i) + '.jpg', im_new)
    print 'processing on image', str(i)

for i in range(1, fcount(srcValidation) + 1):
    im = cv2.imread(srcValidation+ 'image' + str(i) + '.jpg', -1)
    im_new = cv2.pyrDown(im)
    cv2.imwrite(validationPath + 'image' + str(i) + '.jpg', im_new)
    print 'processing on image', str(i)

for i in range(1, fcount(srcTest) + 1):
    im = cv2.imread(srcTest + 'image' + str(i) + '.jpg', -1)
    im_new = cv2.pyrDown(im)
    cv2.imwrite(testPath + 'image' + str(i) + '.jpg', im_new)
    print 'processing on image', str(i)

print 'current image resolution (height, width, number of channel):', im_new.shape
print "DONE"
