import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level2_Scoreboard_Inference_2_generator


def getMinProblemCount(N: int, S: List[int]) -> int:
    m = max(S)
    val = m//3
    mval = m%3

    mods = set(map(lambda x : x%3, S))

    if mods == {0}:
        return val
    if mval == 0:
        return val+1
    if mval == 1:
        if 2 not in mods:
           return val + 1
        if 1 in S or m-1 in S:
           return val + 2
        return val + 1

    if 1 not in mods:
        return val +1
    return val+2

if __name__ == "__main__":
    Level2_Scoreboard_Inference_2_generator.evaluate(getMinProblemCount, True)
