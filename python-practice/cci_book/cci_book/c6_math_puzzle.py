from dataclasses import dataclass


@dataclass
class Pill:
    weight: int


class Bottle:
    _pill_weight: int

    def __init__(self, pill_weight):
        self._pill_weight = pill_weight

    def remove_pill(self) -> Pill:
        return Pill(self._pill_weight)


def guess_bottle(bottles: list[Bottle]) -> int:
    """
    Problem 6.1
    Guess the heavy bottle given 20 bottles.
    """
    assert len(bottles) == 20

    sum_1_to_20 = 210

    weight = 0

    for i in range(0, len(bottles)):
        weight += bottles[i].remove_pill().weight * (i + 1)

    weight -= sum_1_to_20

    return round(weight * 10) - 1
