import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level1_Stack_Stabilization_1_generator


def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    val = 0

    for j in range(N-1,0,-1):
        if R[j] <= R[j-1]:
            R[j-1] = R[j]-1
            val += 1
        if R[j-1] <= 0:
            return -1
    return val


if __name__ == "__main__":
    Level1_Stack_Stabilization_1_generator.evaluate(getMinimumDeflatedDiscCount, True)
