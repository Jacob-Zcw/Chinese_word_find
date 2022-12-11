import os
import copy
import pandas as pd

def fileSplit(filename):
    if len(os.listdir("./data")) != 0:
        return
    
    raw_data = pd.read_csv(filename)
    
    reviews = copy.deepcopy(raw_data["review"])
    
    for i in range(reviews.shape[0]):
        with open("./data/review_" + str(i) + ".txt", "w", encoding = "utf-8") as f:
            f.write(str(reviews[i]))

