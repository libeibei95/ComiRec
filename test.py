import tensorflow as tf

def calc_mean_variance():
    img = tf.Variable(tf.random_normal([4, 3, 3]))
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        print(sess.run(tf.matrix_diag_part(img)))

calc_mean_variance()

