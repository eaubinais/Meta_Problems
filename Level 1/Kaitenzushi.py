import os
import sys
from collections import deque
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level1_Kaitenzushi_generator


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    recent: deque[int] = deque()
    seen: set[int] = set()
    count = 0

    for dish in D:
        if dish not in seen:
            count += 1
            recent.append(dish)
            seen.add(dish)
            if len(recent) > K:
                removed = recent.popleft()
                seen.remove(removed)

    return count

if __name__ == "__main__":
    Level1_Kaitenzushi_generator.evaluate(getMaximumEatenDishCount, True)
