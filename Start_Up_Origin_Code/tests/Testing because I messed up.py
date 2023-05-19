import random
import numpy as np
import pandas as pd
import tensorflow as tf
import datetime
filepath = tf.keras.utils.get_file('shakespeare.txt',
        'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(filepath, 'rb').read().decode(encoding='utf-8')





text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()
characters = sorted(set(text))

char_to_index = dict((c, i) for i, c in enumerate(characters))
index_to_char = dict((i, c) for i, c in enumerate(characters))




SEQ_LENGTH = 40
STEP_SIZE = 3

sentences = []
next_char = []

for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i: i + SEQ_LENGTH])
    next_char.append(text[i + SEQ_LENGTH])


x = np.zeros((len(sentences), SEQ_LENGTH,
              len(characters)), dtype=np.bool)
y = np.zeros((len(sentences),
              len(characters)), dtype=np.bool)

for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_to_index[char]] = 1
    y[i, char_to_index[next_char[i]]] = 1


import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.layers import Activation, Dense, LSTM

model = Sequential()
model.add(LSTM(128,
               input_shape=(SEQ_LENGTH,
                            len(characters))))
model.add(Dense(len(characters)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(learning_rate=0.01))

model.fit(x, y, batch_size=256, epochs=4)


def sample(preds, temperature=1.0):
        preds = np.asarray(preds).astype('float64')
        preds = np.log(preds) / temperature
        exp_preds = np.exp(preds)
        preds = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(1, preds, 1)
        return np.argmax(probas)


def generate_text(length, temperature):
        start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
        generated = ''
        sentence = text[start_index: start_index + SEQ_LENGTH]
        generated += sentence
        for i in range(length):
                x_predictions = np.zeros((1, SEQ_LENGTH, len(characters)))
                for t, char in enumerate(sentence):
                        x_predictions[0, t, char_to_index[char]] = 1

                predictions = model.predict(x_predictions, verbose=0)[0]
                next_index = sample(predictions,
                                    temperature)
                next_character = index_to_char[next_index]

                generated += next_character
                sentence = sentence[1:] + next_character
        return generated


print(generate_text(300, 0.2))
print(generate_text(300, 0.4))
print(generate_text(300, 0.5))
print(generate_text(300, 0.6))
print(generate_text(300, 0.4))
print(generate_text(300, 0.3))

current_time1 = datetime.datetime.now()
current_time2 = str(current_time1)[:19]
SavePath1 = """D:\ShakeBot Testing"""
Filename = "\Test Shakes "
#SavePath2 = SavePath1 + Filename + current_time2 + ".xlsx"
SavePath2 = r'D:\ShakeBot Testing\ShaKeBotTest1.xlsx'
    #wb = xlsxwriter.Workbook(SavePath2)

s1 = pd.DataFrame()
s2 = pd.DataFrame()
s3 = pd.DataFrame()

##Set 9

x1 = generate_text(300, 0.2)
s1['Start'] = str(x1).T
x2 = generate_text(300, 0.3)
s1['Middle'] = x2.values
x3 =  generate_text(300, 0.2)
s1['End'] = x3.values



x1 = generate_text(300, 0.4)
s2['Start'] = str(x1)
x2 = generate_text(300, 0.4)
s2['Middle'] = str(x2)
x3 =  generate_text(300, 0.4)
s2['End'] = str(x3)




x1 = generate_text(300, 0.2)
print('Testing why Excel is not working')
print(x1)
s3['Start'] = str(x1)
x2 = generate_text(300, 0.5)
print(x2)
s3['Middle'] = str(x2)
x3 =  generate_text(300, 0.3)
print(x3)
s3['End'] = str(x3)



with pd.ExcelWriter(SavePath2) as writer:
    s1.to_excel(writer, sheet_name="Story 1")
    s2.to_excel(writer, sheet_name="Story 2")
    s3.to_excel(writer, sheet_name="Story 3")
    writer.close()




