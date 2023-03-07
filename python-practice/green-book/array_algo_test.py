from array_algo import *


# ----- Q1 -----
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


# ----- Q2 -----
def test_strings_contain_same_letter_dict():
    assert strings_contain_same_letter_dict("", "")
    assert strings_contain_same_letter_dict("dog", "dog")
    assert strings_contain_same_letter_dict("parrot", "parort")
    assert not strings_contain_same_letter_dict("cat", "pig")
    assert not strings_contain_same_letter_dict("", "lizard")


# ----- Q3 -----
def test_url_safe_string():
    assert url_safe_string("") == ""
    assert url_safe_string("John Wick") == "John%20Wick"
    assert url_safe_string("all plants need water") == "all%20plants%20need%20water"
    assert url_safe_string("          pasta with garlic and oil    ") == "pasta%20with%20garlic%20and%20oil"
    assert url_safe_string(" Bikes And Cars       And  Boats ") == "Bikes%20And%20Cars%20And%20Boats"


# ----- Q4 -----
def test_is_palindrome_permutation():
    assert is_palindrome_permutation("")
    assert is_palindrome_permutation("civic")
    assert is_palindrome_permutation("ciivc")
    assert is_palindrome_permutation("mom")
    assert is_palindrome_permutation("oom")
    assert not is_palindrome_permutation("dog")
    assert not is_palindrome_permutation("pears")


# ----- Q5 -----
def test_one_edit_away():
    assert one_edit_away("", "")
    assert one_edit_away("pie", "pie")
    assert one_edit_away("pie", "piee")
    assert one_edit_away("pye", "pie")
    assert one_edit_away("elephant", "elepant")
    assert one_edit_away("elepant", "elephant")
    assert one_edit_away("lephant", "elephant")
    assert one_edit_away("elephant", "elephan")
    assert one_edit_away("elephant", "elephan")
    assert not one_edit_away("", "plant")
    assert not one_edit_away("tree", "")
    assert not one_edit_away("phone", "telephone")


#  ----- Q6 -----
def test_compress_string():
    assert compress_string("") == ""
    assert compress_string("parrot") == "par2ot"
    assert compress_string("dog") == "dog"
    assert compress_string("success") == "suc2es2"
    assert compress_string("ffrrrrroggg") == "f2r5og3"


# ----- Q7 -----
def test_rotate_image_size0():
    image = []
    expected = []
    assert rotate_image(image) == expected


def test_rotate_image_size2():
    image = [
        [1, 2],
        [3, 4]
    ]
    expected = [
        [3, 1],
        [4, 2]
    ]
    assert rotate_image(image) == expected
