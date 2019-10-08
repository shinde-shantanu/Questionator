import face_recognition
import cv2
import operator
from keras.models import load_model
import keras
from PIL import Image
import numpy as np
import heapq
import pandas as pd
import pickle
import os

import urllib.request
pre_model = keras.applications.vgg19.VGG19(include_top=False, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)

model = load_model(os.getcwd()+'/model1.h5')



key = ['badminton sport', ' baseball sport ', 'basketball sport', ' cricket',' field hockey', ' golf', 'playing soccer', ' sport volleyball', ' table tennis', ' tennis']


data = pickle.loads(open(os.getcwd()+'\\data3.pickle', "rb").read())
X = data['X']
y = data['y']


df = pd.read_csv("footballers.csv")


count = 0
yes = 'y'
while(yes == 'y'):
	print('-----------------------------------')
	count += 1
	url = input("Enter url:")
	import urllib
	urllib.request.urlretrieve(url, os.getcwd()+'/'+str(count)+".jpg")

	imgg2 = cv2.imread(os.getcwd()+'/'+str(count)+".jpg")
	imgg = cv2.cvtColor(imgg2, cv2.COLOR_BGR2RGB)
	boxes = face_recognition.face_locations(imgg,
		model="hog")
	encodings = face_recognition.face_encodings(imgg, boxes)
	for encoding in encodings:
		matches = face_recognition.compare_faces(X,
				encoding)
		matchCount = {}
		for inx, m in enumerate(matches):
			if(m):
				if(y[inx] not in matchCount):
					matchCount[y[inx]] = 1
				else:
					matchCount[y[inx]] += 1
		print(matchCount)
		if(not bool(matchCount)):
			continue
		predictedName = max(matchCount.items(), key=operator.itemgetter(1))[0]
		print('Person identified: '+predictedName)

		for index, row in df.iterrows():
			if(row['Name'] == predictedName.rsplit(' ', 1)[0]):
				print(row)

	img = Image.open(os.getcwd()+'/'+str(count)+".jpg")
	x = img.resize((224, 224))
	arr = np.array(x)
	arr2 = np.reshape(arr, (1, 224, 224, 3))
	arr2 = arr2 / 255

	arr3 = pre_model.predict(arr2)
	predd = model.predict(arr3)
	pred = predd[0].tolist()

	sortedd = heapq.nlargest(3, pred)
	g1 = pred.index(sortedd[0])
	g2 = pred.index(sortedd[1])
	g3 = pred.index(sortedd[2])
	print('Prediction 1: '+key[g1])
	print('Prediction 2 '+key[g2])
	print('Prediction 3: '+key[g3])

	yes = input("\nMore?(y/n): ")





