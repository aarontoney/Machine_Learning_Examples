#-------------------------------------------------------------------------------
# Author: Aaron Toney
# 
# Description: Simplest possible use of TesnsorFlow - using it to create a graph
#              storing algerbraic operations. 
# 
# Got the idea from: I would not have thought of using tensor flow this way. Got
#                    the ideas Pg 234 of Hands-On Machine Learning with 
#                    Scikit-Learn & TensorFlow
#
#                   +-------------+             Tensor flow is building a graph
#                   |      +      |             that looks something like the 
#                   +-------------+             following - then executing it. 
#                    /           \
#             +------+           +------+
#             |  *   |           |  *   |
#             +------+           +------+
#              /    \             /    \
#         +-----+  +-----+   +-----+  +-----+
#         |  a  |  |  a  |   |  b  |  |  b  |
#         +-----+  +-----+   +-----+  +-----+
#
#-------------------------------------------------------------------------------

# Python
import tensorflow as tf

# Given: a^2 + b^2 = c^2

a = tf.Variable( 2, name="a" )
b = tf.Variable( 5, name="b" )

with tf.Session() as sess:
    a.initializer.run()
    b.initializer.run()

    f = tf.sqrt( tf.to_float(a*a + b*b ))

    result = f.eval()
    print(result)

