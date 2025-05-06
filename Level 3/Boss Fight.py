import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level3_Boss_Fight_generator


def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
    ## Precompute H_i*D_i for each warrior {i}
    HD = [h * d for h, d in zip(H, D)]

    max_damage = 0
    best_warrior = 0

    run = True
    while run:
        run = False
        next_best_warrior = 0

        for i in range(N):
            if i == best_warrior:
                continue

            damage = HD[best_warrior] + HD[i] + max(H[best_warrior] * D[i], H[i] * D[best_warrior])
            if damage > max_damage:
                run = True
                max_damage = damage
                next_best_warrior = i
        best_warrior = next_best_warrior
    return max_damage / B

if __name__ == "__main__":
    Level3_Boss_Fight_generator.evaluate(getMaxDamageDealt, True)
