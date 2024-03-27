import pandas as pd
from src.project.data import make_dataset


column_list =['createdat', 'source', 'category',
              'label_names', 'tags', 'image_url',
              'weburl', 'name',"id","gender"]

def test_split_labels():
    assert make_dataset._split_label_names("エコバッグ/キャンバス") == ["エコバッグ","キャンバス"]
    assert make_dataset._split_label_names("エコバッグ") == ["エコバッグ"]


def test_label_is_in_columns():
    dummy_columns = ["bag_エコバッグ","bag_キャンパス"]
    assert make_dataset._label_is_in_columns(dummy_columns,"bag_エコバッグ")
    assert not make_dataset._label_is_in_columns(dummy_columns,"bag_クリア")


def test_add_new_labels():
    dummy_columns = ["bag_エコバッグ","bag_キャンパス"]
    assert make_dataset._add_new_labels(dummy_columns,"bag_エコバッグ") == dummy_columns
    assert make_dataset._add_new_labels(dummy_columns,"bag_キャンパス") == dummy_columns
    assert make_dataset._add_new_labels(dummy_columns,"bag_クリア") == ["bag_エコバッグ","bag_キャンパス","bag_クリア"]


def test_remove_category_number():
    assert make_dataset._remove_category_number("top_1")=="top"
    assert make_dataset._remove_category_number("top_2")=="top"
    assert make_dataset._remove_category_number("top_3")=="top"
