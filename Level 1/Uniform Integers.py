import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level1_Uniform_Integers_generator


def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    base = 1
    to_add = 1
    val = 0

    while base <= B:
      if base >= A:
        val += 1

      if base%10==9:
        base =  base + to_add + 1
        to_add = 10*to_add+1
      else:
        base += to_add

    return val

if __name__ == "__main__":
    Level1_Uniform_Integers_generator.evaluate(getUniformIntegerCountInInterval, True)
