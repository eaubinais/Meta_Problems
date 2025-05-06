import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level2_Hops_generator


def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    return N - min(P)

if __name__ == "__main__":
    Level2_Hops_generator.evaluate(getSecondsRequired, True)
