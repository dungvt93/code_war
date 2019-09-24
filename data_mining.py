import tensorflow as tf
import numpy as np
import sys
class Datamining:
    def __init__(self, train_set):
        self.X  = tf.placeholder(tf.float32, shape=(None,))
        self.Y = tf.placeholder(tf.float32,shape=(None,))
        self.W = tf.Variable(np.random.randn(), name="W")
        self.b = tf.Variable(np.random.randn(), name="b")
        self.output = tf.add(tf.multiply(self.X, self.W), self.b)
        # self.output = tf.layers.dense(self.X,units=2)
        # cost = tf.reduce_mean(tf.square(tf.subtract(self.Y, self.output)))
        cost = tf.reduce_mean(tf.square(tf.subtract(self.Y, self.output)))
        op = tf.train.AdamOptimizer()
        train_op = op.minimize(cost)
        config = tf.ConfigProto()
        self.session = tf.Session(config=config)
        self.session.run(tf.global_variables_initializer())
        for i in range(10000):
            loss = self.session.run([cost,train_op],feed_dict={self.X:train_set[:,0],self.Y:train_set[:,1]})
            # sys.stdout.write(str(loss))

    def predict(self, x):

        output, W, b =  self.session.run([self.output,self.W,self.b],feed_dict={self.X:[x]})
        print(W)
        print(b)
        return output



example_train_set = [(1,5),(2,8),(-1,-1),(5,17),(6,20)]
example_train_set = np.array(example_train_set)

model = Datamining(example_train_set)
print(model.predict(3))
