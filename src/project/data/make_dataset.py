import pandas as pd

def _split_label_names(label_names:str):
    return label_names.split("/")


def _label_is_in_columns(columns:list, label:str):
    return label in columns


def _add_new_labels(columns:list, label:str):
    if _label_is_in_columns(columns,label):
        return columns
    else:
        return columns+[label]
    

class RecognizedData:
    def __init__(self,path):
        self.df = pd.read_csv(path)
