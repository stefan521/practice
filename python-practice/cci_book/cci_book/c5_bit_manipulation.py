import math
from numpy import uint16


def binary_str(num: uint16) -> str:
    return bin(num)[2:].zfill(16)


def insert_bits(bits_n: str, bits_m: str, i: int, j: int) -> str:
    """
    Problem 5.1
    Insert bits_m into bits_n such that bits_m starts at j and end at i
    n = 10000000000 m = 1011 i = 2 j = 6
    result = 10001001100
    """
    assert 0 <= j < 16 and 0 <= i < 16
    assert j - i == len(bits_m)

    binary_n = uint16(int(bits_n, 2))
    binary_m = uint16(int(bits_m, 2))

    left = int(math.pow(2, j) - 1)
    right = int(math.pow(2, i) - 1)
    bit_mask = ~(uint16(left - right))

    masked_n = binary_n & bit_mask
    shifted_m = binary_m << i

    return binary_str(masked_n | shifted_m)


def float_to_binary(num: float) -> str:
    """
    Problem 5.2
    Return the 32 bit binary representation of num.
    """
    exponent_bias = 127
    max_iter = 23
    whole = math.floor(num)
    decimal = num - whole

    whole_bin = bin(whole)[2:]
    exponent = len(whole_bin) - 1
    mantissa_whole = whole_bin[1:]
    mantissa_decimal = ""

    for i in range(0, max_iter):
        decimal *= 2

        if decimal == 0:
            break

        if decimal >= 1:
            decimal -= 1
            mantissa_decimal += "1"
        else:
            mantissa_decimal += "0"

    sign_bit = "0" if num >= 0 else "1"
    exponent_str = bin(exponent_bias + exponent)[2:].ljust(8, "0")
    mantissa = f"{mantissa_whole}{mantissa_decimal}".ljust(23, "0")[:23]

    return sign_bit + exponent_str + mantissa


def flip_zero(binary_num: str) -> int:
    """
    Problem 5.3
    Flip exactly one zero to get the greatest number of consecutive ones.
    """
    possibilities = [binary_num]
    max_ones = 1

    for i in range(0, len(binary_num)):
        if binary_num[i] == "0":
            rest = "" if i == len(binary_num) else binary_num[i+1:len(binary_num)]
            possibilities.append(binary_num[0:i] + "1" + rest)

    for num in possibilities:
        max_ones_length = max([len(sequence_ones) for sequence_ones in num.split("0")])
        max_ones = max_ones_length if max_ones_length > max_ones else max_ones

    return max_ones

# TODO 5.4


def bit_diff(binary_a: str, binary_b: str) -> int:
    """
    Problem 5.6
    How many bits to flip to convert binary_a to binary_b
    """
    a = int(binary_a, 2)
    b = int(binary_b, 2)

    diff = a ^ b

    return diff.bit_count()


# TODO 5.7

# TODO 5.8
