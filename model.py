
data = '/content/Asans - Sheet1 (1).csv'

import re
from textblob import TextBlob
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from gensim.parsing.preprocessing import remove_stopwords

benefits = []
asan = []

import csv

with open(data,'r') as file:
  reader = csv.reader(file)
  for row in reader:
    benefits.append(row[3])
    asan.append(row[1])

input_1=[]
output=[]
data = []

for i in range (len(benefits)):
  line = benefits[i]
  line = line.lower()
  line = re.sub(r'[^A-Za-z\n]+', ' ', line)
  line = remove_stopwords(line)
  input_1.append(line)
  data.append(line)
  line = asan[i]
  line = re.sub(r'[^A-Za-z0-9 ]+', ' ', line)
  line = line.replace(" ","")
  line = line.replace("(","")
  line = line.replace(")","")
  line = line.replace(".","")
  line = line.replace("/","")
  output.append(line)

from keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
from keras.utils import np_utils
from tensorflow import keras
import keras.backend as K
import numpy as np

oov_token = "<OOV>"
embed_size = 20

tokenizer = Tokenizer(oov_token=oov_token)
tokenizer.fit_on_texts(data)
word_index = tokenizer.word_index
sequence = tokenizer.texts_to_sequences(data)

print(len(word_index))

vocab_size = len(word_index)

index_to_word_map = {}
word_to_index_map = {}
for word,index in word_index.items():
  index_to_word_map[index] = word
  word_to_index_map[word]=index

print('Vocabulary Sample:', list(word_index.items()))
len(sequence)

tokenizer2 = Tokenizer(oov_token=oov_token)
tokenizer2.fit_on_texts(output)
word_index2 = tokenizer2.word_index
sequence2 = tokenizer2.texts_to_sequences(output)

vocab_size2 = len(word_index2)

index_to_word_map2 = {}
for word,index in word_index2.items():
  index_to_word_map2[index] = word

index_to_word_map2[3]

benefits = []
asan = []

for i in range (1,len(sequence)):
  benefits.append(sequence[i])
for i in range (1,len(sequence2)):
  asan.append(sequence2[i])

len(asan)

asan = np.asarray(asan)
np.shape(asan)

y = asan - 3
y = tf.keras.utils.to_categorical(y,226)

np.shape(y)

benefits = pad_sequences(benefits,50,padding='post',truncating='pre')

benefits = np.array(benefits)
np.shape(benefits)

fields = ['Index','Word']
row = []
rows= []
for i in range(1,1425):
  row.append(i)
  row.append(index_to_word_map[i])
  rows.append(row)
  row=[]

with open('/content/map.csv', 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)

import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense, Embedding, Lambda, Flatten, Reshape
import tensorflow as tf

model = Sequential()
model.add(Embedding(vocab_size+1,embed_size,input_length=50))
model.add(Lambda(lambda x: K.mean(x, axis=1), output_shape=(embed_size,)))
model.add(Dense(vocab_size2-2, activation='softmax'))
model.compile(loss=tf.keras.losses.CategoricalCrossentropy(), optimizer='adam',metrics=['accuracy'])
print(model.summary())

history = model.fit(benefits,y,epochs=1000,batch_size=32)

import matplotlib.pyplot as plt
loss_train = history.history['loss']
plt.plot(loss_train, 'g', label='Training loss')
plt.title('Training loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

accuracy = 0
for i in range(0,226):
  y = model.predict(benefits[i])
  z = np.sum(y,axis=0)
  z = z/50
  max=0
  for i in range(226):
    if z[i]>max:
      max = z[i]
      max_i = i
  if max_i+3==asan[i]:
    accuracy = accuracy+1


max=0
max_i=0
for i in range(226):
  if z[i]>max:
    max=z[i]
    max_i=i
print(max)
print(max_i)

model.save('/content/weight.h5')

