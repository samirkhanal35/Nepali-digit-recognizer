def recognize(img):
	
	import os
	import tensorflow as tf
	from tensorflow import keras

	import cv2
	import glob
	import math
	import os
	import unicode as un
	#import image
	#from IPython import display
	from matplotlib import cm
	from matplotlib import gridspec
	from matplotlib import pyplot as plt
	import numpy as np
	import pandas as pd
	import seaborn as sns
	from sklearn import metrics
	from tensorflow.python.data import Dataset
	tf.logging.set_verbosity(tf.logging.ERROR)
	c = []
	def create_model():
		model = tf.keras.models.Sequential([
			keras.layers.Dense(1024, activation=tf.nn.relu, input_shape=(1024,)),
			#keras.layers.Dropout(0.2),
			keras.layers.Dense(512, activation=tf.nn.relu),
			keras.layers.Dense(100, activation=tf.nn.relu),
			keras.layers.Dense(10, activation=tf.nn.softmax)  ])
		
		model.compile(optimizer=tf.keras.optimizers.Adam(),
		 loss=tf.keras.losses.sparse_categorical_crossentropy,
		 metrics=['accuracy'])
		return model
		
	checkpoint_path = "training_1/cp.ckpt"
	checkpoint_dir = os.path.dirname(checkpoint_path)
	
	model = create_model()
	model.load_weights(checkpoint_path)
	
	b,g,r = cv2.split(img)
	img = cv2.merge((b,g,r))
	height = img.shape[0]
	width = img.shape[1]
	
	img1=np.zeros(shape=(1,1024),dtype='float64')
	k=0
	for i in range(0,height):
		for j in range(0,width):
			if img[i][j][0]>200:
				img1[0][k]=0
				k=k+1
			else:
				img1[0][k]=255
				k=k+1
				
	df3 =pd.DataFrame(np.random.randn(10, 5),columns=[1, 2,3,4,5])
	df=pd.DataFrame(np.array(img1),columns=[i for i in range(1,1025)])
	
	classes = model.predict_classes(df)
	c.append(un.unicode(classes))


	print(c)
