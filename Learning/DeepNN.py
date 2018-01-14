import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from random import randint
from matplotlib import pyplot as plt

mnist = input_data.read_data_sets("/tmp/data", one_hot= True)

nodes_hl1=500
nodes_hl2=500
nodes_hl3=500

n_classes=14
batch_size=100

x= tf.placeholder(tf.float32)
y= tf.placeholder(tf.float32)

def neural_network_model(data):


	hidden_layer_1= {'weights': tf.Variable(tf.random_normal([784,nodes_hl1])),
	'biases':tf.Variable(tf.random_normal([nodes_hl1]))}

	hidden_layer_2= {'weights': tf.Variable(tf.random_normal([nodes_hl1,nodes_hl2])),
	'biases':tf.Variable(tf.random_normal([nodes_hl2]))}

	hidden_layer_3= {'weights': tf.Variable(tf.random_normal([nodes_hl2,nodes_hl3])),
	'biases':tf.Variable(tf.random_normal([nodes_hl3]))}

	output_layer= {'weights': tf.Variable(tf.random_normal([nodes_hl3,n_classes])),
	'biases':tf.Variable(tf.random_normal([n_classes]))}

	# (input_data * weights) + biases
	l1= tf.add(tf.matmul(data, hidden_layer_1['weights']), hidden_layer_1['biases'])
	l1= tf.nn.relu(l1)

	l2= tf.add(tf.matmul(l1, hidden_layer_2['weights']), hidden_layer_2['biases'])
	l2= tf.nn.relu(l2)

	l3= tf.add(tf.matmul(l2, hidden_layer_3['weights']), hidden_layer_3['biases'])
	l3 = tf.nn.relu(l3)

	output= tf.add(tf.matmul(l3, output_layer['weights']),output_layer['biases'])

	return output

def train_neural_network(X):
	prediction= neural_network_model(X)
	
	cost= tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits= prediction,labels= y))

	optimizer= tf.train.AdamOptimizer().minimize(cost)

	n_epochs= 8
	with tf.Session() as sess:
		sess.run(tf.initialize_all_variables())
 
		for epoch in range(n_epochs):
			epoch_cost= 0
			for _ in range(int(mnist.train.num_examples/batch_size)):
				epoch_x, epoch_y= mnist.train.next_batch(batch_size)
				_, c= sess.run([optimizer, cost], feed_dict = { x : epoch_x, y : epoch_y }) 
				epoch_cost = epoch_cost + c
			print('epoch ',epoch,' complete out of ', n_epochs, ' loss:',epoch_cost)

		correct= tf.equal(tf.argmax(prediction,1), tf.argmax(y,1))
		accuracy= tf.reduce_mean(tf.cast(correct,'float'))
		print(sess.run(prediction))
		print('Accuracy ', accuracy.eval({x:mnist.test.images, y:mnist.test.labels}))

train_neural_network(x)
