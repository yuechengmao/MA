#!/usr/bin/env python
import os
from scipy.misc import imread
import cv2
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt


hostname = 'cheng'
basePath = '/Users/' + hostname + '/Desktop/masked_data_diffimg/motion'


def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

for motion_cnt in range(1,51):
    path = basePath + str(motion_cnt) + '/imgs1/'
    position = np.empty([fcount(path),2])
    for img_cnt in range(1,fcount(path) + 1):
        img = imread(path + 'cam1_' + str(img_cnt) + '.png')
        print path + 'cam1_' + str(img_cnt) + '.png'
        non_zero_elements = np.argwhere(img)
        if non_zero_elements.shape[0] == 0:
            pos = np.array([0,0])
        else:
            pos = np.mean(non_zero_elements, axis=0)
        position[img_cnt-1] = pos
    np.savetxt(basePath + str(motion_cnt) + '/position1' + '.csv', position, delimiter=',')

    path = basePath + str(motion_cnt) + '/imgs2/'
    position = np.empty([fcount(path),2])
    for img_cnt in range(1,fcount(path) + 1):
        img = imread(path + 'cam2_' + str(img_cnt) + '.png')
        print path + 'cam2_' + str(img_cnt) + '.png'
        non_zero_elements = np.argwhere(img)
        if non_zero_elements.shape[0] == 0:
            pos = np.array([0,0])
        else:
            pos = np.mean(non_zero_elements, axis=0)
        position[img_cnt-1] = pos
    np.savetxt(basePath + str(motion_cnt) + '/position2' + '.csv', position, delimiter=',')

    path = basePath + str(motion_cnt) + '/imgs3/'
    position = np.empty([fcount(path),2])
    for img_cnt in range(1,fcount(path) + 1):
        img = imread(path + 'cam3_' + str(img_cnt) + '.png')
        print path + 'cam3_' + str(img_cnt) + '.png'
        non_zero_elements = np.argwhere(img)
        if non_zero_elements.shape[0] == 0:
            pos = np.array([0,0])
        else:
            pos = np.mean(non_zero_elements, axis=0)
        position[img_cnt-1] = pos
    np.savetxt(basePath + str(motion_cnt) + '/position3' + '.csv', position, delimiter=',')
