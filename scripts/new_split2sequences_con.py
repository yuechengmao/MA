#!/usr/bin/env python

import numpy as np
import os
import shutil
import glob
from scipy.misc import imread, imsave, imresize
from numpy import genfromtxt

numberOfmotions = 51
hostname = 'cheng'

srcPath = '/Users/' + hostname + '/Desktop/new_data/'

dstPath = '/Users/' + hostname + '/Desktop/new_tensorflow/sequences/'
trainPath = dstPath + 'train/'
testPath = dstPath + 'test/'

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

print "on processing..."
#os.makedirs(dstPath)
os.makedirs(trainPath)
os.makedirs(testPath)
seq_cnt = 0
test_cnt = 0
seq_length = 5
for motion_cnt in range(1, 51):
    #cam1
    #seq_length = np.random.random_integers(20)   
    cnt = 0

    data = genfromtxt(srcPath + 'motion' + str(motion_cnt) + '/data.txt', delimiter=',')
    i = 0
    while i < fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs/'):
        cnt += 1
        #print srcPath + 'motion' + str(motion_cnt) + '/imgs1/cam1_' + str(i + 1) + '.jpg'
        if cnt == seq_length:
            if motion_cnt == 2 or motion_cnt == 12 or motion_cnt == 22 or motion_cnt == 32 or motion_cnt == 42:
                test_cnt += 1

                np.savetxt(testPath + 'seq' + str(test_cnt) + '.csv', data[i - seq_length + 1:i + 1,:], fmt='%.8f', delimiter=',')
                print 'Test data:' + 'seq_data' + str(test_cnt) + '.csv' + ', length:', i - seq_length + 1, '-', i + 1
            else:
                seq_cnt += 1
                np.savetxt(trainPath + 'seq' + str(seq_cnt) + '.csv', data[i - seq_length + 1:i + 1,:], fmt='%.8f', delimiter=',')
                print 'Train data:' + 'seq_data' + str(seq_cnt) + '.csv' + ', image:', i + 1
                print ''

            cnt = 0
            i -= 4
        i += 1
   
print 'DONE'

