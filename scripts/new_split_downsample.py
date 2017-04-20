#!/usr/bin/env python
import os
import cv2
import numpy

hostname = 'cheng'

srcTrain = '/Users/' + hostname + '/Desktop/new_tensorflow/data_cropped/train_set/'
srcValidation = '/Users/' + hostname + '/Desktop/new_tensorflow/data_cropped/validation_set/'
srcTest = '/Users/' + hostname + '/Desktop/new_tensorflow/data_cropped/test_set/'

trainPath = '/Users/' + hostname + '/Desktop/new_tensorflow/data_cropped/train_small/'
validationPath = '/Users/' + hostname + '/Desktop/new_tensorflow/data_cropped/validation_small/'
testPath = '/Users/' + hostname + '/Desktop/new_tensorflow/data_cropped/test_small/'

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

for i in range(fcount(srcTrain)):
    im = cv2.imread(srcTrain + 'image' + str(i) + '.png', -1)
    im_new = cv2.pyrDown(im)
    cv2.imwrite(trainPath + 'image' + str(i) + '.png', im_new)
    print 'processing on image', str(i)

for i in range(fcount(srcValidation)):
    im = cv2.imread(srcValidation+ 'image' + str(i) + '.png', -1)
    im_new = cv2.pyrDown(im)
    cv2.imwrite(validationPath + 'image' + str(i) + '.png', im_new)
    print 'processing on image', str(i)

for i in range(fcount(srcTest)):
    im = cv2.imread(srcTest + 'image' + str(i) + '.png', -1)
    im_new = cv2.pyrDown(im)
    cv2.imwrite(testPath + 'image' + str(i) + '.png', im_new)
    print 'processing on image', str(i)

print 'current image resolution (height, width, number of channel):', im_new.shape
print "DONE"
