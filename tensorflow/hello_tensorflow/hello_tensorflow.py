#-------------------------------------------------------------------------------
# Example from: https://www.tensorflow.org/install/install_mac
#-------------------------------------------------------------------------------
# Python

# From Hands-On Machine Learning with Scikit-Learn & TensorFlow
import tensorflow as tf


hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

# From the pre-work from googles machine learning crash course
# uses nicer syntax
#
# https://colab.research.google.com/notebooks/mlcc/hello_world.ipynb?hl=en#scrollTo=cH-YtyZs7Gcg

# c = tf.constant('Hello, world!')
# 
# with tf.Session() as sess:
#     print sess.run(c)
