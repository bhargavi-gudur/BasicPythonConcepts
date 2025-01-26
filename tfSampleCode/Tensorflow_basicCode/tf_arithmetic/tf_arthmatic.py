#tensor flow arithmetic 
import tensorflow as tf

#define constant
a = tf.constant(4)
b = tf.constant(2)

#perform basic  arithmetic operations
add = tf.add(a,b)
sub = tf.subtract(a,b)
div = tf.divide(a,b)
mul = tf.multiply(a,b)
# print arithmetic opeartions
tf.print(f"addition of two numbers is-> {add}")
tf.print(f"subraction of two number is ->{sub}")
tf.print(f"multiplication of two number is ->{mul}")
tf.print(f"division of two number is ->{div}")
