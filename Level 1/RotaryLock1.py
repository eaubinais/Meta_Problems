import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level1_Rotary_Lock_1_generator


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    val = 0
    C_: List[int] = [1,*C]

    for j in range(1,M+1):
        val += min(abs(C_[j-1]-C_[j]), N-abs(C_[j-1]-C_[j]))

    return val

if __name__ == "__main__":
    Level1_Rotary_Lock_1_generator.evaluate(getMinCodeEntryTime, True)
