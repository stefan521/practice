from array_algo import *


def test_contains_unique_characters_built_in_func():
    assert not contains_unique_characters_built_in_func("falsee")
    assert not contains_unique_characters_built_in_func("cc")
    assert contains_unique_characters_built_in_func("dog")
    assert contains_unique_characters_built_in_func("")
    assert contains_unique_characters_built_in_func("iytu123")


def test_contains_unique_dict():
    assert not contains_unique_characters_dict("falsee")
    assert not contains_unique_characters_dict("cc")
    assert contains_unique_characters_dict("dog")
    assert contains_unique_characters_dict("")
    assert contains_unique_characters_dict("iytu123")


def test_contains_unique_characters_stupid_slow():
    assert not contains_unique_characters_stupid_slow("falsee")
    assert not contains_unique_characters_stupid_slow("cc")
    assert contains_unique_characters_stupid_slow("dog")
    assert contains_unique_characters_stupid_slow("")
    assert contains_unique_characters_stupid_slow("iytu123")


def test_contains_unique_characters_sorting():
    assert not contains_unique_characters_sorting("falsee")
    assert not contains_unique_characters_sorting("cc")
    assert contains_unique_characters_sorting("dog")
    assert contains_unique_characters_sorting("")
    assert contains_unique_characters_sorting("iytu123")
