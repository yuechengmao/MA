#!/usr/bin/env python

import numpy as np
import os
import shutil
import glob

numberOfmotions = 51
hostname = 'cheng'

srcPath1 = '/Users/' + hostname + '/Desktop/pc1/'
srcPath2 = '/Users/' + hostname + '/Desktop/pc2/'
dstPath1 = '/Users/' + hostname + '/Desktop/new/'

print "on processing..."


os.makedirs(dstPath1)
os.makedirs(dstPath1 + 'data')
for i in range(1, numberOfmotions):
	os.makedirs(dstPath1 + 'data/motion' + str(i))

for i in range(1, numberOfmotions):
    shutil.copytree(srcPath1 + 'data/motion' + str(i) + '/imgs1', dstPath1 + 'data/motion' + str(i) + '/imgs1')
    print srcPath1 + 'data/motion' + str(i) + '/imgs1'
    shutil.copytree(srcPath1 + 'data/motion' + str(i) + '/imgs2', dstPath1 + 'data/motion' + str(i) + '/imgs2')
    print srcPath1 + 'data/motion' + str(i) + '/imgs2'
    shutil.copytree(srcPath2 + 'data/motion' + str(i) + '/imgs3', dstPath1 + 'data/motion' + str(i) + '/imgs3')
    print srcPath2 + 'data/motion' + str(i) + '/imgs3'
    shutil.copy(srcPath1 + 'data/motion' + str(i) + '/data1.txt', dstPath1 + 'data/motion' + str(i))
    print srcPath1 + 'data/motion' + str(i) + '/data1.txt'
    shutil.copy(srcPath1 + 'data/motion' + str(i) + '/data2.txt', dstPath1 + 'data/motion' + str(i))
    print srcPath1 + 'data/motion' + str(i) + '/data2.txt'
    shutil.copy(srcPath2 + 'data/motion' + str(i) + '/data3.txt', dstPath1 + 'data/motion' + str(i))
    print srcPath2 + 'data/motion' + str(i) + '/data3.txt'
#####################

'''

numberOftextfile = (numberOfmotions - 1)*3 + 1

srcPath = '/Users/' + hostname + '/Desktop/data/'
dstPath = '/Users/' + hostname + '/Desktop/cross_validation/data/'

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count


os.makedirs(dstPath)
os.makedirs(dstPath + 'imgs')

data_cnt = 0
image_cnt = 0
dataFiles = []

for i in range(1, numberOfmotions):
    data_cnt = data_cnt + 1
    shutil.copy(srcPath + 'motion' + str(i) + '/data1.txt', dstPath + 'data' + str(data_cnt) + '.txt')
    data_cnt = data_cnt + 1
    shutil.copy(srcPath + 'motion' + str(i) + '/data2.txt', dstPath + 'data' + str(data_cnt) + '.txt')
    data_cnt = data_cnt + 1
    shutil.copy(srcPath + 'motion' + str(i) + '/data3.txt', dstPath + 'data' + str(data_cnt) + '.txt')

    for img_cnt in range(1, fcount(srcPath + 'motion' + str(i) + '/imgs1') + 1):
        image_cnt = image_cnt + 1
        shutil.copy(srcPath + 'motion' + str(i) + '/imgs1/cam1_' + str(img_cnt)  + '.jpg', dstPath + 'imgs/image' + str(image_cnt) + '.jpg')
    for img_cnt in range(1, fcount(srcPath + 'motion' + str(i) + '/imgs2') + 1):
        image_cnt = image_cnt + 1
        shutil.copy(srcPath + 'motion' + str(i) + '/imgs2/cam2_' + str(img_cnt)  + '.jpg', dstPath + 'imgs/image' + str(image_cnt) + '.jpg')
    for img_cnt in range(1, fcount(srcPath + 'motion' + str(i) + '/imgs3') + 1):
        image_cnt = image_cnt + 1
        shutil.copy(srcPath + 'motion' + str(i) + '/imgs3/cam3_' + str(img_cnt)  + '.jpg', dstPath + 'imgs/image' + str(image_cnt) + '.jpg')

for i in range(1, numberOftextfile):
    dataFiles.append(dstPath + 'data' + str(i) + '.txt')

with open(dstPath + 'data.txt', 'wb+') as outfile:
    for f in dataFiles:
        with open(f, 'rb') as infile:
            outfile.write(infile.read())

for i in range(1, numberOftextfile):
    os.remove(dataFiles[i-1])

outfile.close()
counter = 0
with open(dstPath + 'datawithpath.txt', 'wb+') as file1:
    with open(dstPath + 'data.txt', 'rb+') as file2:
        for line in file2:
            counter = counter + 1
            newline = dstPath + 'imgs/image' + str(counter) + '.jpg,' + line
            file1.write(newline)

#shutil.rmtree('/home/' + hostname + '/Desktop/new')
'''
print "DONE"

