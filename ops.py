#coding:utf-8
import math
import numpy as np 
import tensorflow as tf

def bn(x,is_train):
    return tf.layers.batch_normalization(x,epsilon=1e-5,momentum=0.5,
        training=is_train)
def conv2d(x,filters,kernel_size=3,strides=[1,1]):
    return tf.layers.conv2d(x,filters=filters,
             kernel_size=kernel_size,
             padding='same',
             strides=strides,
             kernel_initializer=tf.truncated_normal_initializer(stddev=0.02))
def deconv2d(x,filters,kernel_size=3,strides=[1,1],padding='same'):
    return tf.layers.conv2d_transpose(x,filters=filters,
             kernel_size=kernel_size,
             padding=padding,
             strides=strides,
             kernel_initializer=tf.truncated_normal_initializer(stddev=0.02))

