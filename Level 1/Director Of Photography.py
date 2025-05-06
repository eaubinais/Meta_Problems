import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from itertools import product

from utils import Level1_DirectorOfPhotography_generator


def within(what: int, a: int, b: int) -> int:
    if a <= b:
        return what >= a and what <= b
    return within(what, b, a)


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here
    ps: List[int] = []
    as_: List[int] = []
    bs: List[int] = []
    for i, c in enumerate(C):
        if c == 'P':
           ps.append(i)
        elif c == 'A':
           as_.append(i)
        elif c == 'B':
           bs.append(i)
    val = sum(int(within(abs(p-a), X, Y) and within(abs(a-b), X, Y) and within(a, p, b))
              for p, a, b in product(ps, as_, bs)
              )
    return val

if __name__ == "__main__":
    Level1_DirectorOfPhotography_generator.evaluate(getArtisticPhotographCount, True)
