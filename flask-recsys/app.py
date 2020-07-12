from flask import Flask, request, Response, jsonify
# import scipy
# import sklearn
import pandas as pd
# import numpy as np
# import random
# import boto3

# from scipy.sparse import csr_matrix
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from scipy.sparse.linalg import svds
# from sklearn.preprocessing import MinMaxScaler

import joblib
# import pickle

from utils import *

app = Flask(__name__)
file_name = "sim-mat.joblib"

@app.route('/',methods=["POST","GET"])
def rec_messages():
    df = pd.read_csv("messages_data/users.csv")
    return 'Hey, we have Flask in a Docker container!'

@app.route("/carsDemo",methods=["POST"])
def get_rec_cars():
    data = request.get_json(silent=True, force=True)

    pivot_norm = joblib.load("pivot-norm.joblib")
    item_sim_df = joblib.load(file_name)

    items_df = pd.read_csv("car-items.csv")

    topn = data["num_recs"]
    item_id = data["item_id"]

    sim_items, sim_score = get_item(pivot_norm,item_sim_df,item_id,topn)
    item_names = [get_name(items_df,item) for item in sim_items]
    response = {
        "items": item_names,
        "scores": sim_score
    }

    return jsonify(response)

# @app.route("/carsDemoOld",methods=["POST"])
# def get_rec_cars_old():

#     min_interactions = 5
#     sample = 50000

#     data = request.get_json(silent=True, force=True)
#     item_id = data["item_id"]
#     topn = data["num_recs"]

#     items_df = pd.read_csv("cars_data/car-items.csv")
#     interactions_df = pd.read_csv("cars_data/interactions_personalize.csv")
#     interactions_df["CLICK"] = np.ones(interactions_df.values.shape[0])
#     interactions_sample = interactions_df.sample(n=sample)
    
#     # Filter users with more than 5 interactions
#     users_interactions_count = interactions_sample.groupby(["USER_ID","ITEM_ID"]).size().groupby("USER_ID").size()
#     users_filtered = users_interactions_count[users_interactions_count >= min_interactions].reset_index()[["USER_ID"]]
#     interactions_from_selected_users_df = interactions_sample.merge(users_filtered,how = 'right',left_on = 'USER_ID',right_on = 'USER_ID')

#     interactions_full_df = interactions_from_selected_users_df.groupby(['USER_ID', 'ITEM_ID'])['CLICK'].sum().reset_index()

#     # # Split 
#     interactions_train_df, interactions_test_df = train_test_split(interactions_full_df,stratify=interactions_full_df['USER_ID'], test_size=0.20,random_state=42)
#     # # Matriz de usuarios-item ()
#     pivot_mat = interactions_train_df.pivot(index='ITEM_ID',columns='USER_ID',values='CLICK').fillna(0)
#     # print(pivot_mat)
#     pivot_norm = pivot_mat.apply(lambda x: (x-np.mean(x))/(np.max(x)-np.min(x)), axis=1)
#     # print(pivot_norm)
#     # # matriz de similitud
#     item_sim_df = pd.DataFrame(cosine_similarity(pivot_norm, pivot_norm), index=pivot_norm.index, columns=pivot_norm.index)
#     # print(item_sim_df)
#     sim_items,sim_score = get_item(pivot_norm,item_sim_df,item_id,topn)
#     item_names = [get_name(items_df,item) for item in sim_items]
#     response = {
#         "items": item_names,
#         "scores": sim_score
#     }
#     return response




# @app.route('/procesar', methods=["POST"])
# def name():
#     data = request.get_json(silent=True, force=True)
#     full_name = "Tu nombre completo es{} {}".format(data["nombre"],data["apellido"])
#     return (full_name,200)


# @app.route('/servicios', methods=["POST"])
# def services():
#     s3 = boto3.client("s3")
#     data = request.get_json(silent=True, force=True)
#     if data["service"] == "s3":
#         try:
#             response = s3.list_objects(
#                 Bucket=data["bucket"],
#                 Prefix=data["prefix"]
#             )
#         except:
#             return ("Servicio no accesible",400)

#         if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
#             archivo = response["Contents"][0]["Key"]
#             return (archivo,200)
#         elif response["HTTPStatusCode"] == 500:
#             return ("Bucket no accesible",400)
#         else:
#             return("Nada",400)    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=4000)

