import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level3_Rabbit_Hole_2_generator


def getRabbitHole(N: int, M: int, A: List[int], B: List[int]) -> int:
    raise NotImplementedError("This function is not implemented yet.")

if __name__ == "__main__":
    Level3_Rabbit_Hole_2_generator.evaluate(getRabbitHole, True)
