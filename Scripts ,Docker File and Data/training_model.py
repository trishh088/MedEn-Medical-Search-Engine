# Databricks notebook source
pip install --upgrade gensim 

# COMMAND ----------


import pandas as pd
import numpy as np
import string 	# used for pre-processing
import re 		# used for pre-processing
import nltk 	# the Natural Language Toolkit, used for pre-processing
import numpy as np 	#used for managing NaNs
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords    # used for preprocessing
from nltk.stem import WordNetLemmatizer   # used for preprocessing
from sklearn.model_selection import train_test_split
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
import gensim
# import gensim.models import Word2Vec
# import gensim.models import FastTest
import pickle

# COMMAND ----------

def model_train(x, vector_size, window_size, model):
    if model=='Skipgram':
        skipgram = Word2Vec(x, vector_size=vector_size, window=window_size, min_count=2, sg=1) 
        skipgram.save('/dbfs/mnt/data/data/output/model_Skipgram.bin')
        return skipgram
    elif model=='Fasttext':
        fast_text= FastText(x, vector_size=vector_size, window=window_size, min_count=2, workers=5, min_n=1, max_n=2, sg=1)
        with open('/dbfs/mnt/data/data/output/model_Fasttext1.bin', 'wb') as f_out:
            pickle.dump(fast_text, f_out)
            f_out.close()
            fast_text.save('/dbfs/mnt/data/data/output/model_Fasttext.bin')
        return fast_text
