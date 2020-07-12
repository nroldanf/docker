import pandas as pd
import numpy as np


def get_item(pivot_norm,item_sim_df,item_id,topn):
    if item_id not in pivot_norm.index:
        return None, None
    else:
        sim_items = item_sim_df.sort_values(by=item_id, ascending=False).index[7:topn+7].tolist()
        sim_score = item_sim_df.sort_values(by=item_id, ascending=False).loc[:, item_id].tolist()[7:topn+7]
        return sim_items, sim_score

def get_name(items_df,item_id):
    lista = items_df[items_df["ITEM_ID"] == item_id].values[0].tolist()[1:]
    lista = [str(i) for i in lista]
    return " ".join(lista)

