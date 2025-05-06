import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level2_DirectorOfPhotography_generator


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    prefix_P = [0] * (N + 1)
    prefix_B = [0] * (N + 1)

    for i in range(N):
        prefix_P[i + 1] = prefix_P[i] + (1 if C[i] == 'P' else 0)
        prefix_B[i + 1] = prefix_B[i] + (1 if C[i] == 'B' else 0)

    def count_in_range(prefix: List[int], l: int, r: int) -> int:
        l = max(0, l)
        r = min(N, r)
        if l >= r:
            return 0
        return prefix[r] - prefix[l]

    val = 0
    for j in range(N):
        if C[j] != 'A':
            continue
        p_minus = count_in_range(prefix_P, j - Y, j - X + 1)
        b_plus  = count_in_range(prefix_B, j + X, j + Y + 1)

        b_minus = count_in_range(prefix_B, j - Y, j - X + 1)
        p_plus  = count_in_range(prefix_P, j + X, j + Y + 1)

        val += p_minus * b_plus + b_minus * p_plus

    return val

if __name__ == "__main__":
    Level2_DirectorOfPhotography_generator.evaluate(getArtisticPhotographCount, True)
