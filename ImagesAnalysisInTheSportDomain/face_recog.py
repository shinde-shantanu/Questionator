import os
import pickle
import cv2
import sys
import face_recognition
import operator
import pandas as pd

from google_images_download import google_images_download
import pandas as pd
from keras.models import load_model
import keras

#Download training images

df = pd.read_csv("footballers.csv")
i = 0
for index, row in df.iterrows():
	name = row['Name']
	response = google_images_download.googleimagesdownload()
	absolute_image_paths = response.download({'keywords': name + ' face', 'limit': 15, 'extract_metadata': True, 'format': 'jpg', 'output_directory':'downloads2'})
	print(i)
	i += 1



#Train
df = pd.read_csv("footballers.csv")
X = []
y = []
i = 1
e = 0

for folder in os.listdir(os.getcwd()+'/downloads2/'):
	name = folder
	found = False
	temp = name.rsplit(' ', 1)[0]
	
	for index, row in df.iterrows():
		if(index == 50):
			break
		if(temp == row['Name']):
			found = True
			break
	if(not found):
		continue
	i += 1
	print(i)
	for filename in os.listdir(os.getcwd()+'/downloads2/' + folder + '/'):
		
		try:
			print('Training ' + name + ' - ' + filename)    
			imgg2 = cv2.imread(os.getcwd()+'/downloads2/'+folder+'/'+filename)
			imgg = cv2.cvtColor(imgg2, cv2.COLOR_BGR2RGB)
			boxes = face_recognition.face_locations(imgg,
				model="hog")
			encodings = face_recognition.face_encodings(imgg, boxes)
			for encoding in encodings:
				X.append(encoding)
				y.append(name)
		except Exception as e1:
			e += 1
			print(e1)
			print(e)
print(y)

print(len(X))


#save pickle files
data = {"X": X, "y": y}
f = open('/content/drive/My Drive/colab/sport_tp/face recog/data3.pickle', "wb")
f.write(pickle.dumps(data))
f.close()


#download test images
df = pd.read_csv("footballers.csv")
i = 0
for index, row in df.iterrows():
	name = row['Name']
	response = google_images_download.googleimagesdownload()
	absolute_image_paths = response.download({'keywords': name, 'limit': 2, 'extract_metadata': True, 'format': 'jpg', 'output_directory':'test'})
	print(i)
	i += 1


#testing
i = 0
e = 0
right = 0
wrong = 0
data = pickle.loads(open('/content/drive/My Drive/colab/sport_tp/face recog/data3.pickle', "rb").read())
X = data['X']
y = data['y']
print(len(y))

for folder in os.listdir(os.getcwd()+'/test/'):
	name = folder
	found = False
	
	
	for index, row in df.iterrows():
		if(index == 50):
			break
		if(name == row['Name']):
			found = True
			break
	if(not found):
		continue
	print(i)
	i += 1
	for filename in os.listdir(os.getcwd()+'/test/' + folder + '/'):
		try:
			print('-----------------------------------')
			imgg2 = cv2.imread(os.getcwd()+'/test/'+folder+'/'+filename)
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
				print(predictedName + '-' + name)
				if(predictedName.rsplit(' ', 1)[0] == name):
					right += 1
					print('RIGHT')
				else:
					wrong += 1
					print('WRONG')
				print('acc = %s' %((right)/(right+wrong)))
		except Exception as e1:
			print(e1)
			e += 1
			print('error')
			print(e)


print('%s' %((right)/(right+wrong)))



pre_model = keras.applications.vgg19.VGG19(include_top=False, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)
model = load_model('model1.h5')