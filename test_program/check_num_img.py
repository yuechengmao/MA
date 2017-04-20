
import numpy as np 
import os

def fcount(path):
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1
    return count

for i in range(1, 51):
    print i, '  ', fcount('/Users/cheng/Desktop/new_data/motion' + str(i) + '/imgs/')