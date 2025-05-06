import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from utils import Warmup_ABCs_generator


def getSum(A: int, B: int, C: int) -> int:
    return A+B+C

if __name__ == "__main__":
    Warmup_ABCs_generator.evaluate(getSum, True)
