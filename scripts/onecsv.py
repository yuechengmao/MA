#!/usr/bin/env python
from PIL import Image
import numpy
import itertools
import os

hostname = 'cheng'
dstPath = '/Users/' + hostname + '/Desktop/data1/imgs'
dataPath = '/Users/' + hostname + '/Desktop/data1/'

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count


img_cnt = 0
with open(dataPath + 'data.csv', 'w+') as imgfile:
    with open(dataPath + 'data.txt', 'rb+') as file1:
        for line in file1:
            img_cnt = img_cnt + 1
            im = Image.open(dstPath + '/image' + str(img_cnt) + '.jpg')
            pixel_list = [im.getdata()]
            img = list(itertools.chain(*pixel_list))
            imgfile.write(','.join('%s' % x for x in img))
            imgfile.write(',')
            imgfile.write(line)
            print 'line', img_cnt, 'finished'
    file1.close()
imgfile.close()

