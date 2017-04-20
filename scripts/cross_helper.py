
import numpy as np 



data_cnt = np.arange(1, 151)
np.random.shuffle(data_cnt)

np.savetxt('cross.txt', data_cnt, fmt='%d', delimiter=',')

