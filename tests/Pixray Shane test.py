
#Below is the shakespear thing

import pandas as pd
import datetime
import os
import sys
#sys.path.append(r'C:\Users\sdono\OneDrive\Documents\PixRay')
#import module_of_interest

#import xlsxwriter
#import rhyme
import random
import numpy as np
import pixray

class ArtBot:
    def __init__(self, prompt):
        self.prompt = prompt
        #os.getcwd()
        pixray.run(self.prompt, outdir="outputs/hairout")



               



class PoemBot:



    PoetCount = 0
    def __init__(self, Poet, Lucidness, Size, Style, SEQ_LENGTH,STEP_SIZE):

      self.Poet = Poet
      self.Lucidness = Lucidness
      self.Size = Size
      self.Style = Style
     #self.text = ''
      self.SEQ_LENGTH = SEQ_LENGTH
      self.STEP_SIZE = STEP_SIZE
      self.sentences = []
      self.next_char = []
      # self.characters = ''
      # self.model = object
      # self.sample = object
      # self.index_to_char = object
      # self.char_to_index =  object
      # self.preds = object
      self.temperature =1.0
      self.length = 300
      PoemBot.PoetCount += 1


    #Somewhere this is needed
    # Source_Location(Poet, Style)

    def setupdata(self):

        import random
        import numpy as np
        import pandas as pd
        import tensorflow as tf
        import datetime
        filepath = tf.keras.utils.get_file('shakespeare.txt',
                'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
        self.text = open(filepath, 'rb').read().decode(encoding='utf-8')
        ##Set 2
        self.text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()
        self.characters = sorted(set(self.text))
        self.char_to_index = dict((c, i) for i, c in enumerate(self.characters))
        self.index_to_char = dict((i, c) for i, c in enumerate(self.characters))
#        return 0


    # def lowercaseApp(self):
        for i in range(0, len(self.text) - self.SEQ_LENGTH, self.STEP_SIZE):
            self.sentences.append(self.text[i: i + self.SEQ_LENGTH])
            self.next_char.append(self.text[i + self.SEQ_LENGTH])

  #  def ApplyDictionary(self):
        x = np.zeros((len(self.sentences), self.SEQ_LENGTH,
                      len(self.characters)), dtype=bool)
        y = np.zeros((len(self.sentences),
                      len(self.characters)), dtype=bool)

        for i, sentence in enumerate(self.sentences):
            for t, char in enumerate(sentence):
                x[i, t, self.char_to_index[char]] = 1
            y[i, self.char_to_index[self.next_char[i]]] = 1
            #PoemBot.model_Shake()

        import random
        import numpy as np
        import tensorflow as tf

    def model_Shake(self):
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.optimizers import RMSprop
        from tensorflow.keras.layers import Activation, Dense, LSTM

        self.model = Sequential()
        self.model.add(LSTM(128,
                       input_shape=(self.SEQ_LENGTH,
                                    len(self.characters)),name="Shakes"))
        self.model.add(Dense(len(self.characters),name="Shakes2"))
        self.model.add(Activation('softmax'))

        self.model.compile(loss='categorical_crossentropy',
                      optimizer=RMSprop(learning_rate=0.01))
        self.model.fit(x, y, batch_size=256, epochs=4)




    def learnIMDBwords(self,num_words = 10000, sequence_length = 300,  batch_size = 128):
        # New Added 12/16
        import numpy as np
        import sklearn
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix, accuracy_score, f1_score, \
            roc_curve
        from sklearn.preprocessing import LabelEncoder
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        from keras.models import Sequential
        from keras.callbacks import ReduceLROnPlateau, EarlyStopping
        from keras.layers import Activation, Dense, Dropout, Embedding, LSTM
        import re
        from IPython.display import display
        import os
        import string
        import time
        import random
        import matplotlib.pyplot as plt
        from tensorflow.keras.datasets import imdb
        self.num_words = num_words
        (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=5000)
        self.sequence_length = sequence_length
        self.batch_size = batch_size
        X_train_seq = pad_sequences(X_train, maxlen=sequence_length)
        X_test_seq = pad_sequences(X_test, maxlen=sequence_length)
        encoder = LabelEncoder()
        encoder.fit(y_train)
        y_train_transformed = encoder.transform(y_train).reshape(-1, 1)
        y_test_transformed = encoder.transform(y_test).reshape(-1, 1)
        e = Embedding(self.num_words, 10, input_length=sequence_length)
        #When I run them all together I should remove this
        self.model = Sequential()
        self.model.add(e)
        self.model.add(LSTM(128, dropout=0.25, recurrent_dropout=0.25,name="IMDB"))
        self.model.add(Dense(1, activation='sigmoid',name="IMDB2"))
        self.model.summary()
        self.model.compile(optimizer="adam", loss='binary_crossentropy', metrics=['accuracy'])
        early_stopper = EarlyStopping(monitor='val_acc', min_delta=0.0005, patience=3)
        reduce_lr = ReduceLROnPlateau(monitor='val_loss', patience=2, cooldown=0)
        callbacks = [reduce_lr, early_stopper]
        train_history = self.model.fit(X_train_seq, y_train_transformed, batch_size=batch_size, epochs=5,
                                  validation_split=0.1, verbose=1, callbacks=callbacks)
        score = self.model.evaluate(X_test_seq, y_test_transformed, batch_size=batch_size)
        y_pred = self.model.predict(X_test_seq)
        print("Accuracy: {:0.4}".format(score[1]))
        print("Loss:", score[0])
        print(' Accuracy: { :0.3 }'.format(100 * accuracy_score(y_test_transformed, 1 * (y_pred > 0.5))))
        print(' f1 score: {:0.3}'.format(100 * f1_score(y_test_transformed, 1 * (y_pred > 0.5))))
        print(' ROC AUC: {:0.3}'.format(roc_auc_score(y_test_transformed, y_pred)))
        print(classification_report(y_test_transformed, 1 * (y_pred > 0.5), digits=3))
        loss = train_history.history['loss']
        validation_loss = train_history.history['val_loss']
        accuracy = train_history.history['acc']
        val_accuracy = train_history.history['val_acc']
        fig = plt.gcf()
        fig.set_size_inches(18.5, 5.5)
        plt.subplot(1, 2, 1)
        plt.plot(loss)
        plt.plot(validation_loss)
        plt.legend(['loss', 'validation_loss'])
        plt.subplot(1, 2, 2)
        plt.plot(accuracy)
        plt.plot(val_accuracy)
        plt.legend(['accuracy', 'validation_accuracy'])
        plt.show()

        # load doc into memory

    def load_doc(self,filename):
        # open the file as read only
        file = open(filename, 'r')
        # read all text
        text = file.read()
        # close the file
        file.close()
        return text
    # turn a doc into clean tokens
    def clean_doc(self,doc):
        import string
        # replace '--' with a space ' '
        doc = doc.replace('--', ' ')
        # split into tokens by white space
        tokens = doc.split()
        # remove punctuation from each token
        table = str.maketrans('', '', string.punctuation)
        tokens = [w.translate(table) for w in tokens]
        # remove remaining tokens that are not alphabetic
        tokens = [word for word in tokens if word.isalpha()]
        # make lower case
        tokens = [word.lower() for word in tokens]
        return tokens
    # save tokens to file, one dialog per line
    def save_doc(self,lines, filename):
        data = '\n'.join(lines)
        file = open(filename, 'w')
        file.write(data)
        file.close()


    # load doc into memory
    def load_doc(self,filename):
        # open the file as read only
        file = open(filename, 'r')
        # read all text
        text = file.read()
        # close the file
        file.close()
        return text


    def GreekWords(self):
        import tensorflow
        # load document
        in_filename = 'republic_clean.txt'
        doc = PoemBot.load_doc(in_filename)
        print(doc[:200])

        # clean document
        tokens = PoemBot.clean_doc(doc)
        print(tokens[:200])
        print('Total Tokens: %d' % len(tokens))
        print('Unique Tokens: %d' % len(set(tokens)))

        # organize into sequences of tokens
        length = 50 + 1
        sequences = list()
        for i in range(length, len(tokens)):
            # select sequence of tokens
            seq = tokens[i - length:i]
            # convert into a line
            line = ' '.join(seq)
            # store
            sequences.append(line)
        print('Total Sequences: %d' % len(sequences))

        # save sequences to file
        out_filename = 'republic_sequences.txt'
        PoemBot.save_doc(sequences, out_filename)


    # load
        in_filename = 'republic_sequences.txt'
        doc = PoemBot.load_doc(in_filename)
        lines = doc.split('\n')

        # integer encode sequences of words
        tokenizer = tensorflow.Tokenizer()
        tokenizer.fit_on_texts(lines)
        sequences = tokenizer.texts_to_sequences(lines)

        # vocabulary size
        vocab_size = len(tokenizer.word_index) + 1

        # separate into input and output
        sequences = array(sequences)
        X, y = sequences[:, :-1], sequences[:, -1]
        y = to_categorical(y, num_classes=vocab_size)
        seq_length = X.shape[1]

        #self.model = Sequential()
        self.model.add(Embedding(vocab_size, 50, input_length=seq_length))
        self.model.add(LSTM(100, return_sequences=True,name="Greek1"))
        self.model.add(LSTM(100),name="Greek2")
        self.model.add(Dense(100, activation='relu',name="Greek3"))
        self.model.add(Dense(vocab_size, activation='softmax',name="Greek4"))
        print(self.model.summary())

    ##Set 7
    def sample(self, preds):
        self.preds = preds
        #self.temperature = temperature
        self.preds = np.asarray(self.preds).astype('float64')
        self.preds = np.log(self.preds) / self.temperature
        exp_preds = np.exp(self.preds)
        self.preds = exp_preds / np.sum(exp_preds)
        probas = np.random.multinomial(1, self.preds, 1)
        return np.argmax(probas)

        ##Set 8
    def generate_text(self, length, temperature):
        self.temperature = temperature
        start_index = random.randint(0, len( self.text) - self.SEQ_LENGTH - 1)
        generated = ''
        sentence = self.text[start_index: start_index + self.SEQ_LENGTH]
        generated += sentence
        for i in range(length):
            x_predictions = np.zeros((1, self.SEQ_LENGTH, len(self.characters)))
            for t, char in enumerate(sentence):
                x_predictions[0, t, self.char_to_index[char]] = 1
            predictions = self.model.predict(x_predictions, verbose=0)[0]
            next_index = PoemBot.sample(self,predictions)
            next_character = self.index_to_char[next_index]

            generated += next_character
            sentence = sentence[1:] + next_character
        return generated


    def SaveModel4Later(self):
        from numpy import loadtxt
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense
        self.model.save("model.h5")
        print("Saved model to disk")



        # dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")
        # # split into input (X) and output (Y) variables
        # X = dataset[:, 0:8]
        # Y = dataset[:, 8]
        # # define model
        # model = Sequential()
        # model.add(Dense(12, input_dim=8, activation='relu'))
        # model.add(Dense(8, activation='relu'))
        # model.add(Dense(1, activation='sigmoid'))
        # # compile model
        # model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        # # Fit the model
        # model.fit(X, Y, epochs=150, batch_size=10, verbose=0)
        # # evaluate the model
        # scores = model.evaluate(X, Y, verbose=0)
        # print(self.model.metrics_names[1])
        # #save model and architecture to single file



    def MakeaRhyme(self):
        import rhyme
        print(rhyme.makeLimerick().lower())
        print("Beware of the devil.")
        for word in rhyme.getRhymes("DEVIL"):
            print("He will make you " + word.lower() + '.')


    def ReloadModel(self):
        from tensorflow.keras.models import load_model
        import tensorflow
        from numpy import loadtxt
        # load and evaluate a saved model
        # load model
        self.model = load_model('model.h5')

        filepath = tensorflow.keras.utils.get_file('shakespeare.txt',
                                           'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

        self.model.summary()
        self.text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()

        #print(self.model.metrics_names[1])

        # load dataset
        # dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")
        # # split into input (X) and output (Y) variables
        # X = dataset[:, 0:8]
        # Y = dataset[:, 8]
        # evaluate the model
        # score = model.evaluate(X, Y, verbose=0)

    def shakesbot(cls):
            current_time1 = datetime.datetime.now()
            current_time2 = str(current_time1)[:19]
            print (current_time2)
            SavePath1 = """D:\ShakeBot Testing"""
            Filename = "\Test Shakes v2 "
            #SavePath2 = SavePath1 + Filename + current_time2 + ".xlsx"
            SavePath2 = r'D:\ShakeBot Testing\ShaKeBotTest11 - 12-19-2022.xlsx'


            s1 = pd.DataFrame()
            s2 = pd.DataFrame()
            s3 = pd.DataFrame()

            ##Set 9
            x1 = PoemBot.generate_text(cls,300, 0.2)
            s1['Start'] = [x1]
            x2 = PoemBot.generate_text(cls, 300, 0.3)
            s1['Middle'] = [x2]
            x3 = PoemBot.generate_text(cls, 300, 0.2)
            s1['End'] = [str(x3)]

            x1 = PoemBot.generate_text(cls, 300, 0.4)
            s2['Start'] =  [x1]
            x2 = PoemBot.generate_text(cls, 300, 0.4)
            s2['Middle'] = [str(x2)]
            x3 = PoemBot.generate_text(cls, 300, 0.4)
            s2['End'] = [str(x3)]

           # PoemBot.learnIMDBwords(cls)
            x1 = PoemBot.generate_text(cls, 300, 0.2)
            print('Testing why Excel is not working')
            print(x1)
            s3['Start'] = [x1]
            x2 = PoemBot.generate_text(cls, 300, 0.5)
            print(x2)
            s3['Middle'] = [str(x2)]
            x3 = PoemBot.generate_text(cls, 300, 0.3)
            print(x3)
            s3['End'] = [str(x3)]
            print(s3.values)

            with pd.ExcelWriter(SavePath2) as writer:
                s1.to_excel(writer, sheet_name="Story 1")
                s2.to_excel(writer, sheet_name="Story 2")
                s3.to_excel(writer, sheet_name="Story 3")


            return SavePath2


def shakesbot_DA(cls):

    current_time1 = datetime.datetime.now()
    current_time2 = str(current_time1)[:19]
    print(current_time2)
    SavePath1 = """D:\ShakeBot Testing"""
    Filename = "\Test Shakes v2 "
    # SavePath2 = SavePath1 + Filename + current_time2 + ".xlsx"
    SavePath2 = r'D:\ShakeBot Testing\ShaKeBotTest11 - 12-19-2022.xlsx'

    s1 = pd.DataFrame()
    s2 = pd.DataFrame()
    s3 = pd.DataFrame()

    ##Set 9
    x0 = PoemBot.generate_text(cls, 300, 0.2)
    s3['Start'] = [x0]
    # PoemBot.learnIMDBwords(cls)
    x1 = PoemBot.generate_text(cls, 300, 0.6)
   # print(x1)
    s3['Middle1'] = [x1]
    x2 = PoemBot.generate_text(cls, 300, 0.4)
   # print(x2)
    s3['Middle2'] = [str(x2)]
    x3 = PoemBot.generate_text(cls, 300, 0.2)
   # print(x3)
    s3['End'] = [str(x3)]
   # print(s3.values)

    with pd.ExcelWriter(SavePath2) as writer:
       # s1.to_excel(writer, sheet_name="Story 1")
      #  s2.to_excel(writer, sheet_name="Story 2")
        s3.to_excel(writer, sheet_name="Story 3")

    return x0


#Come up with user inputs for app
if __name__ == '__main__':

    PoemRun = True
    if PoemRun == True:
        Reset_Text = 1
        if Reset_Text == 0:
            x = PoemBot(1, 1, 1, 1, 40, 3)
            x.setupdata()

        else:
            x = PoemBot(1, 1, 1, 1, 40, 3)
            x.ReloadModel()

        x.SaveModel4Later()
        x.setupdata()
        print(x.shakesbot())

        #y = PoemBot(1, 1, 1, 1, 40, 3)
        #y.MakeaRhyme()
        #y.learnIMDBwords()
        #y.learnIMDBwords()

    else:
        prompts = "suicide at the brooklyn bridge | film noir"
        z = ArtBot(prompts)

    random.seed(10)



#print(generate_text(300, 0.6))
#print(generate_text(300, 0.7))
#print(generate_text(300, 0.8))
#
#
# def SaveModel4Later:
#     # MLP for Pima Indians Dataset saved to single file
#     from numpy import loadtxt
#     from tensorflow.keras.models import Sequential
#     from tensorflow.keras.layers import Dense
#     # load pima indians dataset
#     dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")
#     # split into input (X) and output (Y) variables
#     X = dataset[:, 0:8]
#     Y = dataset[:, 8]
#     # define model
#     model = Sequential()
#     model.add(Dense(12, input_dim=8, activation='relu'))
#     model.add(Dense(8, activation='relu'))
#     model.add(Dense(1, activation='sigmoid'))
#     # compile model
#     model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#     # Fit the model
#     model.fit(X, Y, epochs=150, batch_size=10, verbose=0)
#     # evaluate the model
#     scores = model.evaluate(X, Y, verbose=0)
#     print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
#     # save model and architecture to single file
#     model.save("model.h5")
#     print("Saved model to disk")
#
#
# def ReloadModel(self):
#     # load and evaluate a saved model
#     # load model
#     model = load_model('model.h5')
#     # summarize model.
#     model.summary()
#     # load dataset
#     dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")
#     # split into input (X) and output (Y) variables
#     X = dataset[:, 0:8]
#     Y = dataset[:, 8]
#     # evaluate the model
#     score = model.evaluate(X, Y, verbose=0)
#     print("%s: %.2f%%" % (model.metrics_names[1], score[1] * 100))













