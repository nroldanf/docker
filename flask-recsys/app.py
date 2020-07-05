from flask import Flask
import scipy
import sklearn
import pandas as pd
import numpy as np
import random

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse.linalg import svds
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def rec_messages():
    df = pd.read_csv("data/users.csv")
    return 'Hey, we have Flask in a Docker container!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4000)