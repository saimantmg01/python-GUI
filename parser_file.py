import pandas as pd
from pprint import pprint

def csv_reader():
    df = pd.read_csv("Book.csv")
    #library = {'shelf1': {'Curious George':['monkey', 'Christopher'], 
    #                       'Henry and Mudge': ['About a boy and his dog', 'Bob'], 
    #                       'Diary of a wimpy kid': ['kid writes diary', 'Daniel'], 
    #                       'Bone': ['human bones', 'Michelle']
    #                       }
    #           }
    library = {}
    #get all unique keys in csv file
    keys = df["Dict_Key"].unique()
    #initialize the dicitonary with keys
    for key in keys:
        library[key] = {}
    for index,row in df.iterrows():
        value = [row["Description"], row["Author"]]
        library[row["Dict_Key"]][row["Name"]] = value
    #pprint(library)
    return library

    