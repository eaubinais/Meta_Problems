import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Warmup_Battleship_generator


def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    return sum(map(sum,G))/(R*C)

if __name__ == "__main__":
    Warmup_Battleship_generator.evaluate(getHitProbability, True)
