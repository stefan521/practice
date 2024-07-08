from cci_book.c5_bit_manipulation import (
    insert_bits,
    float_to_binary,
    flip_zero,
    bit_diff
)


def test_insert_bits_1():
    result = insert_bits(bits_n="0000010000000000", bits_m="1011", i=2, j=6)
    assert result == "0000010000101100"


def test_insert_bits_2():
    result = insert_bits(bits_n="0000010000000000", bits_m="1011", i=0, j=4)
    assert result == "0000010000001011"


def test_float_to_binary_1():
    assert float_to_binary(85.125) == "01000010101010100100000000000000"


def test_flip_zero():
    assert flip_zero("11011101111") == 8
    assert flip_zero("10011111110") == 8
    assert flip_zero("00000000000") == 1
    assert flip_zero("00001000000") == 2
    assert flip_zero("00001001100") == 3


def test_bit_diff():
    assert bit_diff("11101", "01111") == 2
    assert bit_diff("11100", "01111") == 3
    assert bit_diff("11111", "00000") == 5
    assert bit_diff("11111", "11111") == 0

