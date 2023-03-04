from array_algo import *


def test_contains_unique_characters1():
    assert not contains_unique_characters1("falsee")
    assert not contains_unique_characters1("cc")
    assert contains_unique_characters1("dog")
    assert contains_unique_characters1("")
    assert contains_unique_characters1("iytu123")


def test_contains_unique_characters2():
    assert not contains_unique_characters2("falsee")
    assert not contains_unique_characters2("cc")
    assert contains_unique_characters2("dog")
    assert contains_unique_characters2("")
    assert contains_unique_characters2("iytu123")


def test_contains_unique_characters_stupid_slow():
    assert not contains_unique_characters_stupid_slow("falsee")
    assert not contains_unique_characters_stupid_slow("cc")
    assert contains_unique_characters_stupid_slow("dog")
    assert contains_unique_characters_stupid_slow("")
    assert contains_unique_characters_stupid_slow("iytu123")