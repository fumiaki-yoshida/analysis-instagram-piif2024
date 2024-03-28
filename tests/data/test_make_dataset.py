import pandas as pd
import numpy as np
from src.project.data import make_dataset


column_list = [
    "createdat",
    "source",
    "category",
    "label_names",
    "tags",
    "image_url",
    "weburl",
    "name",
    "id",
    "gender",
]


def test_split_labels():
    assert make_dataset._split_label_names("エコバッグ/キャンバス") == ["エコバッグ", "キャンバス"]
    assert make_dataset._split_label_names("エコバッグ") == ["エコバッグ"]


def test_label_is_in_columns():
    dummy_columns = ["bag_エコバッグ", "bag_キャンパス"]
    assert make_dataset._label_is_in_columns(dummy_columns, "bag_エコバッグ")
    assert not make_dataset._label_is_in_columns(dummy_columns, "bag_クリア")


def test_add_new_labels():
    dummy_columns = ["bag_エコバッグ", "bag_キャンパス"]
    assert make_dataset._add_new_labels(dummy_columns, "bag_エコバッグ") == dummy_columns
    assert make_dataset._add_new_labels(dummy_columns, "bag_キャンパス") == dummy_columns
    assert make_dataset._add_new_labels(dummy_columns, "bag_クリア") == [
        "bag_エコバッグ",
        "bag_キャンパス",
        "bag_クリア",
    ]


def test_remove_category_number():
    assert make_dataset._remove_category_number("top_1") == "top"
    assert make_dataset._remove_category_number("top_2") == "top"
    assert make_dataset._remove_category_number("bottoms_3") == "bottoms"
    assert make_dataset._remove_category_number("bottoms_10") != "bottoms"


def test_prepare_feature_list():
    row = {"label_list": "ギンガムチェック/グレー", "category": "tops_1"}
    assert ["tops_ギンガムチェック", "tops_グレー"] == make_dataset.prepare_feature_list(row)


def test_feature_dict2featureDataFrame():
    dammy_df = pd.DataFrame(columns=['a', 'b', 'c'],
                            data=np.array([
                                [1,1,1],
                                [0,1,1],
                                [0,0,1]
                                      ]))
    feature_dict={0:["a","b","c"],1:["b","c"],2:["c"]}
    assert dammy_df.equals(make_dataset.convert_feature_dict2feature_DataFrame(feature_dict))