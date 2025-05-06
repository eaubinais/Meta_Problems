import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from utils import Level1_Cafetaria_generator


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    val = 0
    sortedS = sorted(S)

    for j in range(1,M):
        free_seats = sortedS[j]-sortedS[j-1] - 1
        authorized_seats = max(0,(free_seats - K)//(K+1))
        val += authorized_seats
    val += max(0, (sortedS[0]-1)//(K+1))
    val += max(0, (N-sortedS[-1])//(K+1))

    return val

if __name__ == "__main__":
    Level1_Cafetaria_generator.evaluate(getMaxAdditionalDinersCount, True)
