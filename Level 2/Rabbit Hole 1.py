import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level2_Rabbit_Hole_1_generator


def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    L_: List[int] = [l - 1 for l in L]

    state = [0] * N  # 0: unvisited, 1: visiting, 2: visited
    dp = [0] * N     # dp[i] = max unique pages starting from i

    for i in range(N):
        if state[i] != 0:
            continue

        path: List[int] = []
        cur = i

        while True:
            if state[cur] == 0:
                path.append(cur)
                state[cur] = 1
                cur = L_[cur]
            elif state[cur] == 1:
                # Found a cycle
                cycle_start = cur
                cycle_len = 1
                idx = len(path) - 1
                while path[idx] != cycle_start:
                    cycle_len += 1
                    idx -= 1
                # Assign cycle length
                for j in range(idx, len(path)):
                    dp[path[j]] = cycle_len
                    state[path[j]] = 2
                # Assign tail lengths
                length = cycle_len
                for j in range(idx - 1, -1, -1):
                    length += 1
                    dp[path[j]] = length
                    state[path[j]] = 2
                break
            elif state[cur] == 2:
                # Followed into a known path
                length = dp[cur]
                for j in path[::-1]:
                    length += 1
                    dp[j] = length
                    state[j] = 2
                break

    return max(dp)

if __name__ == "__main__":
    Level2_Rabbit_Hole_1_generator.evaluate(getMaxVisitableWebpages, True)
