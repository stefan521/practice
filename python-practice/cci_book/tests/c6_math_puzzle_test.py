from cci_book.c6_math_puzzle import Bottle, guess_bottle


def test_guess_bottle_0():
    bottles = [
        Bottle(pill_weight=1.1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1)
    ]

    assert guess_bottle(bottles) == 0


def test_guess_bottle_1():
    bottles = [
        Bottle(pill_weight=1), Bottle(pill_weight=1.1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1)
    ]

    assert guess_bottle(bottles) == 1


def test_guess_bottle_2():
    bottles = [
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1.1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1)
    ]

    assert guess_bottle(bottles) == 2


def test_guess_bottle_19():
    bottles = [
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1),
        Bottle(pill_weight=1), Bottle(pill_weight=1.1)
    ]

    assert guess_bottle(bottles) == 19
