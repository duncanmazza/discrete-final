
import itertools
from enum import Enum
from typing import Dict, Set


class Fruits(Enum):
    Pear = 0
    Watermelon = 1
    Cherry = 2
    Apple = 3
    Banana = 4


happiness: Dict[Fruits, float] = {
    Fruits.Pear: 5,
    Fruits.Watermelon: 2,
    Fruits.Cherry: -4,
    Fruits.Apple: 10,
    Fruits.Banana: 1
}

cost: Dict[Fruits, float] = {
    Fruits.Pear: 1,
    Fruits.Watermelon: 7,
    Fruits.Cherry: 3,
    Fruits.Apple: 4,
    Fruits.Banana: 6
}


def s_to_selection(s: str) -> Set[Fruits]:
    ret = set()
    counter = 0
    for c in s:
        if c == '1':
            ret.add(Fruits(counter))
        counter += 1
    return ret


def objective(s: Set[Fruits]) -> float:
    o = 0
    for f in s:
        o += happiness[f] - cost[f]
    o -= (len(s) - 1) * 4
    return o


def max_objective():
    # from https://stackoverflow.com/questions/4928297/all-permutations-of-a-binary-sequence-x-bits-long
    all_options = ["".join(seq) for seq in itertools.product("01", repeat=5)]
    max_seen = -1
    best_seen = set()
    for option in all_options:
        set_s = s_to_selection(option)
        option_objective = objective(set_s)
        if option_objective > max_seen:
            max_seen = option_objective
            best_seen = set_s
    print(f"Solution: {best_seen} (objective={max_seen})")


if __name__ == "__main__":
    max_objective()