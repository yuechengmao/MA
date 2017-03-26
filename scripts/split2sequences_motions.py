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
dstPath = '/Users/' + hostname + '/Desktop/sequence_motions/data/'

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

print "on processing..."
os.makedirs(dstPath)

seq_cnt = 0
curruent_cnt = 0
seq_length = 10
for motion_cnt in range(1, 51):
    #cam1
    curruent_cnt += 1
    os.makedirs(dstPath + str(curruent_cnt))
    seq_cnt = 0
    cnt = 0
    data = genfromtxt(srcPath + 'motion' + str(motion_cnt) + '/data1.txt', delimiter=',')
    #first 9 sequences
    for k in range(1, 10):
        seq_1_9 = np.zeros((10,11))
        for m in range(k):
            seq_1_9[m+(10-k),:] = data[m,:]
        seq_cnt += 1
        np.savetxt(dstPath + str(curruent_cnt) + '/seq_label' + str(seq_cnt) + '.csv', seq_1_9, fmt='%.8f', delimiter=',')

    i = 0
    while i < fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs1/'):
        cnt += 1
        if cnt == seq_length:
            seq_cnt += 1
            np.savetxt(dstPath + str(curruent_cnt) + '/seq_label' + str(seq_cnt) + '.csv', data[i - seq_length + 1:i + 1,:], fmt='%.8f', delimiter=',')
            print dstPath + str(curruent_cnt) + '/seq_label' + str(seq_cnt) + '.csv'
            cnt = 0
            i -= seq_length
            i += 1
        i += 1
    #cam2
    curruent_cnt += 1
    os.makedirs(dstPath + str(curruent_cnt))
    seq_cnt = 0
    cnt = 0
    data = genfromtxt(srcPath + 'motion' + str(motion_cnt) + '/data2.txt', delimiter=',')
    #first 9 sequences
    for k in range(1, 10):
        seq_1_9 = np.zeros((10,11))
        for m in range(k):
            seq_1_9[m+(10-k),:] = data[m,:]
        seq_cnt += 1
        np.savetxt(dstPath + str(curruent_cnt) + '/seq_label' + str(seq_cnt) + '.csv', seq_1_9, fmt='%.8f', delimiter=',')

    i = 0
    while i < fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs2/'):
        cnt += 1
        if cnt == seq_length:
            seq_cnt += 1
            np.savetxt(dstPath + str(curruent_cnt) + '/seq_label' + str(seq_cnt) + '.csv', data[i - seq_length + 1:i + 1,:], fmt='%.8f', delimiter=',')
            print dstPath + str(curruent_cnt) + '/seq_label' + str(seq_cnt) + '.csv'
            cnt = 0
            i -= seq_length
            i += 1
        i += 1
    #cam3
    curruent_cnt += 1
    os.makedirs(dstPath + str(curruent_cnt))
    seq_cnt = 0
    cnt = 0
    data = genfromtxt(srcPath + 'motion' + str(motion_cnt) + '/data3.txt', delimiter=',')
    #first 9 sequences
    for k in range(1, 10):
        seq_1_9 = np.zeros((10,11))
        for m in range(k):
            seq_1_9[m+(10-k),:] = data[m,:]
        seq_cnt += 1
        np.savetxt(dstPath + str(curruent_cnt) + '/seq_label' + str(seq_cnt) + '.csv', seq_1_9, fmt='%.8f', delimiter=',')

    i = 0
    while i < fcount(srcPath + 'motion' + str(motion_cnt) + '/imgs3/'):
        cnt += 1
        if cnt == seq_length:
            seq_cnt += 1
            np.savetxt(dstPath + str(curruent_cnt) + '/seq_label' + str(seq_cnt) + '.csv', data[i - seq_length + 1:i + 1,:], fmt='%.8f', delimiter=',')
            print dstPath + str(curruent_cnt) + '/seq_label' + str(seq_cnt) + '.csv'
            cnt = 0
            i -= seq_length
            i += 1
        i += 1

print 'DONE'

