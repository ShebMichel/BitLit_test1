# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:52:18 2018

@author: 22029152
"""
import numpy as np

parameters_poems = np.load('model_poems.npy')[()]
embedding_weights_poems = parameters_poems['embedding_weights']
gru_weights_poems = parameters_poems['gru_weights']
fc_weights_poems = parameters_poems['fc_weights']
char2idx_poems = parameters_poems['char2idx']
idx2char_poems = parameters_poems['idx2char']
max_length_poems = parameters_poems['max_length']
embedding_dim_poems = parameters_poems['embedding_dim']
units_poems = parameters_poems['units'] 
BATCH_SIZE_poems = parameters_poems['BATCH_SIZE']
BUFFER_SIZE_poems = parameters_poems['BUFFER_SIZE']

vocab_size_poems = len(dict(idx2char_poems))

# Load hyperparameters and layers' weights previously saved
parameters_rhymes = np.load('model_rhymes.npy')[()]
embedding_weights_rhymes = parameters_rhymes['embedding_weights']
gru_weights_rhymes = parameters_rhymes['gru_weights']
fc_weights_rhymes = parameters_rhymes['fc_weights']
word2idx_rhymes = parameters_rhymes['word2idx']
idx2word_rhymes = parameters_rhymes['idx2word']
max_length_rhymes = parameters_rhymes['max_length'] 
embedding_dim_rhymes = parameters_rhymes['embedding_dim']  
units_rhymes = parameters_rhymes['units']
BATCH_SIZE_rhymes = parameters_rhymes['BATCH_SIZE']
BUFFER_SIZE_rhymes = parameters_rhymes['BUFFER_SIZE']

vocab_size_rhymes = len(dict(idx2word_rhymes))
