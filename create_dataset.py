import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer


with open('processed_texts.csv', 'r', encoding='UTF-8') as file:
    train_data = [line.strip('\n') for line in file]

print('Number of training sentences: ', len(train_data))

max_words = 50000 # Max size of the dictionary
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(train_data)
sequences = tokenizer.texts_to_sequences(train_data)

# Flatten the list of lists resulting from the tokenization. This will reduce the list
# to one dimension, allowing us to apply the sliding window technique to predict the next word
text = [item for sublist in sequences for item in sublist]
vocab_size = len(tokenizer.word_index)

# Training on 19 words to predict the 20th
sentence_len = 20
pred_len = 1
train_len = sentence_len - pred_len
seq = []
# Sliding window to generate train data
for i in range(len(text)-sentence_len):
    seq.append(text[i:i+sentence_len])
# Reverse dictionary to decode tokenized sequences back to words
reverse_word_map = dict(map(reversed, tokenizer.word_index.items()))

# Each row in seq is a 20 word long window. We append he first 19 words as the input to predict the 20th word
trainX = []
trainy = []
for i in seq:
    trainX.append(i[:train_len])
    trainy.append(i[-1])

np.savetxt( 'dataset_input.csv', np.array(trainX))
np.savetxt( 'dataset_output.csv', np.array(trainy))

print("vocab size:", vocab_size)