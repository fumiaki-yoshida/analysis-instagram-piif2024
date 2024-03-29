import re
import pandas as pd


def _split_label_names(label_names: str):
    return label_names.split("/")


def _label_is_in_columns(columns: list, label: str):
    return label in columns


def _add_new_labels(columns: list, label: str):
    if _label_is_in_columns(columns, label):
        return columns
    else:
        return columns + [label]


def _remove_category_number(label):
    return re.sub("([a-z]+)_[0-9]", r"\1", label)


def prepare_feature_list(row):
    label_list = _split_label_names(row["label_names"])
    category = _remove_category_number(row["category"])
    feature_list = []
    for label in label_list:
        new_fearure = category + "_" + label
        feature_list.append(new_fearure)
    return feature_list


def make_feature_dict(df: pd.DataFrame):
    feature_dict = {}
    for index, row in df.iterrows():
        feature_list = prepare_feature_list(row)
        feature_dict[index] = feature_list
    return feature_dict


def convert_feature_dict2feature_DataFrame(feature_dictionary):
    feature_series = pd.Series(feature_dictionary)
    return pd.get_dummies(feature_series.explode()).groupby(level=0).sum()


class RecognizedData:
    def __init__(self, path):
        self.df = pd.read_csv(path)
