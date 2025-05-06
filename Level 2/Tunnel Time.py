import os
import sys
from typing import List

from numpy import argsort

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level2_Tunnel_Time_generator


def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
    total_time_tunnels = sum(B) - sum(A)
    idx: List[int] = list(argsort(A))

    if K % total_time_tunnels == 0:
        return C * ((K // total_time_tunnels) - 1) + B[idx[-1]]

    n_turns: int = K // total_time_tunnels
    k: int = K % total_time_tunnels

    for j in idx:
        if k <= B[j] - A[j]:
            return C * n_turns + A[j] + k
        k -= (B[j] - A[j])

    #Should never reach here
    return -1

if __name__ == "__main__":
    Level2_Tunnel_Time_generator.evaluate(getSecondsElapsed, True)
