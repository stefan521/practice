from cci_book.c5_bit_manipulation import insert_bits, float_to_binary


def test_insert_bits_1():
    result = insert_bits(bits_n="0000010000000000", bits_m="1011", i=2, j=6)
    assert result == "0000010000101100"


def test_insert_bits_2():
    result = insert_bits(bits_n="0000010000000000", bits_m="1011", i=0, j=4)
    assert result == "0000010000001011"


def test_float_to_binary_1():
    assert float_to_binary(85.125) == "01000010101010100100000000000000"
