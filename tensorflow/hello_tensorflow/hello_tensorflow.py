#-------------------------------------------------------------------------------
# Example from: https://www.tensorflow.org/install/install_mac
#-------------------------------------------------------------------------------
# Python
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
