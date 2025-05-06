import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level4_Conveyor_Chaos_generator


def getConveyorChaos(N: int, H: List[int], A: List[int], B: List[int]) -> int:
    raise NotImplementedError("You need to implement this function.")

if __name__ == "__main__":
    Level4_Conveyor_Chaos_generator.evaluate(getConveyorChaos, True)
