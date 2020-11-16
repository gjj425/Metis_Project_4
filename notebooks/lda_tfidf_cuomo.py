import pickle
import pandas as pd


infile = open('/Users/gavin/Documents/Metis/Coursework/Project_4/notebooks/lda_tfidf.pkl', 'rb')
lda_tfidf= pickle.load(infile)

infile = open('/Users/gavin/Documents/Metis/Coursework/Project_4/notebooks/dtm_tfidf.pkl', 'rb')
dtm_tfidf= pickle.load(infile)

infile = open('/Users/gavin/Documents/Metis/Coursework/Project_4/notebooks/tf_idf_vectorizer.pkl', 'rb')
tf_vectorizer= pickle.load(infile)

import pyLDAvis
import pyLDAvis.sklearn

visualization = pyLDAvis.sklearn.prepare(lda_tfidf, dtm_tfidf, tf_vectorizer)

pyLDAvis.save_html(visualization, '/Users/gavin/Documents/Metis/Coursework/Project_4/notebooks/LDA_Visualization.html')