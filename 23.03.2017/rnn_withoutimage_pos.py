import tensorflow as tf
import numpy as np 

from numpy import genfromtxt

import matplotlib.pyplot as plt


train_label = genfromtxt('./train.txt', delimiter=',')
valid_label = genfromtxt('./validation.txt', delimiter=',')
train_pos = genfromtxt('./train_pos.txt', delimiter=',')
valid_pos = genfromtxt('./validation_pos.txt', delimiter=',')

train_pos = train_pos/320.0
valid_pos = valid_pos/320.0

# Parameters
learning_rate = 0.00105
training_iters = 575
batch_size = 100

n_hidden = 32 #20
num_cell_layer = 2
n_classes = 3

data_cnt = np.arange(0, 57500)
np.random.shuffle(data_cnt)
current_cnt = 0

def get_next_batch(batch_size):
    global current_cnt, data_cnt
    if current_cnt + batch_size>=57500:
        current_cnt = 0
        np.random.shuffle(data_cnt)
    #cnt = np.random.random_integers(0, 50000, batch_size)
    cnt = data_cnt[current_cnt:current_cnt + batch_size]
    current_cnt += batch_size
    data_batch = train_label[cnt, 8:11]
    param_batch = train_label[cnt, 0:8]
    param_batch = np.concatenate((param_batch,train_pos[cnt, 0:2]),axis=1)

    param_batch = param_batch.reshape(batch_size,10,1)

    return param_batch, data_batch


def get_test_batch():
    global valid_pos
    data_batch = valid_label[:, 8:11]
    param_batch = valid_label[:, 0:8]

    param_batch = np.concatenate((param_batch,valid_pos[:, 0:2]),axis=1)
    #param_batch[:,9]=1
    #print param_batch
    #np.savetxt('param_batch.csv',param_batch,fmt='%.8f',delimiter=',')
    #input()
    param_batch = param_batch.reshape(-1,10,1)

    return param_batch, data_batch

def get_train_batch():
    data_batch = train_label[:, 8:11]
    param_batch = train_label[:, 0:8]
    param_batch = np.concatenate((param_batch,train_pos[:, 0:2]),axis=1)
    param_batch = param_batch.reshape(-1,10,1)

    return param_batch, data_batch

# Inputs
x = tf.placeholder('float', [None, 10, 1])
y = tf.placeholder("float", [None, n_classes])

# Weights and Biases
weights = {

    'out': tf.Variable(tf.truncated_normal([n_hidden, n_classes]))
}
biases = {
    'out': tf.Variable(tf.truncated_normal([n_classes]))
}

lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden)

#init_state = tf.nn.rnn_cell.LSTMStateTuple(tf.zeros([100,20]), tf.zeros([100,20]))

#tf.nn.rnn_cell.DropoutWrapper(lstm_cell, input_keep_prob=0.85, output_keep_prob=0.95)
#print lstm_cell.state_size
#lstm_cell = tf.nn.rnn_cell.MultiRNNCell([lstm_cell]*num_cell_layer)
#print lstm_cell.state_size
outputs, states = tf.nn.dynamic_rnn(lstm_cell, x, dtype=tf.float32)
#print states
#input()

outputs = tf.transpose(outputs, [1, 0, 2])


y_pred = tf.matmul(outputs[-1], weights['out']) + biases['out']

cost_l1 = tf.reduce_mean(tf.abs(tf.subtract(y_pred, y)))
cost = tf.reduce_mean(tf.squared_difference(y_pred, y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    #summary_writer = tf.summary.FileWriter('./log/', graph=tf.get_default_graph())
    if learning_rate < 0.01:
        saver.restore(sess, "./model/rnn_withoutimage_pos.ckpt")
        print("Model restored!")
    for num_epoch in range(100):
        loss = 0
        '''
        for i in range(training_iters):
            batch_x, batch_y = get_next_batch(batch_size)
            _,c,stat = sess.run([optimizer,cost_l1,states], feed_dict={x: batch_x, y: batch_y})
            loss += c

            if i % 100 == 0:
                print 'iter:', (i), ' mean difference: ', [c]
            #summary_writer.add_summary(summary)
        saver.save(sess, "./model/rnn_withoutimage_pos.ckpt")
        print("Model saved!")
        '''
        batch_x, batch_y = get_test_batch()
        test_c, value = sess.run([cost_l1,weights['out']], feed_dict={x: batch_x, y: batch_y})
        batch_x, batch_y = get_train_batch()
        train_c = sess.run(cost_l1, feed_dict={x: batch_x, y: batch_y})
        print 'LOSS: ', train_c, 'TEST LOSS:', test_c
        #print value
        #if learning_rate > 0.0001:
            #learning_rate /= 3
        print 'next learning rate: ', learning_rate

        
