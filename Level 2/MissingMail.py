import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level2_Missing_Mail_generator


def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    max_expected_profit: List[float] = [0]*(N+1)
    V_ = [0] + V
    for i in range(1, N+1):
        value, proba_of_being_there = 0, 1
        max_expected_profit[i] = -float('inf')
        for j in range(i-1, -1, -1):
            max_expected_profit[i] = max(max_expected_profit[i], max_expected_profit[j] + V_[i] + value - C)
            proba_of_being_there *= 1-S
            value += V_[j]*proba_of_being_there

    return max(max_expected_profit)

if __name__ == "__main__":
    Level2_Missing_Mail_generator.evaluate(getMaxExpectedProfit, True)
