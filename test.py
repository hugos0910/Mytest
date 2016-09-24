import tensorflow as tf
import numpy as np

x = tf.truncated_normal([1,5], stddev=0.1)
# x = tf.placeholder(tf.float32, [None, 784])


# init = tf.initialize_all_variables()

with tf.Session() as sess:
  print(sess.run(x))