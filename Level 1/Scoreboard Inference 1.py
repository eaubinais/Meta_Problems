import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level1_Scoreboard_Inference_1_generator


def getMinProblemCount(N: int, S: List[int]) -> int:
    val = max(S)
    if any(map(lambda x: x % 2 == 1, S)):
        return 1 + val // 2
    return val // 2

if __name__ == "__main__":
    Level1_Scoreboard_Inference_1_generator.evaluate(getMinProblemCount, True)
