import os
import sys
from typing import Dict, List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level2_Rotary_Lock_2_generator


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    d: Dict[Tuple[int, int], int] = {(1,1) : 0}

    for j in range(M):
        new_d: Dict[Tuple[int, int], int] = {}
        for a,b in d:
            k1 = (a, C[j])
            rk1 = (C[j], a) #Equivalent

            cost1 = min(abs(b-C[j]), N-abs(b-C[j]))

            if k1 in new_d:
                new_d[k1] = min(new_d[k1], d[(a,b)] + cost1)
            elif rk1 in new_d:
                new_d[rk1] = min(new_d[rk1], d[(a,b)] + cost1)
            elif k1 in d:
                new_d[k1] = min(d[k1], d[(a,b)] + cost1)
            elif rk1 in d:
                new_d[k1] = min(d[rk1], d[(a,b)] + cost1)
            else:
                new_d[k1] = d[(a,b)] + cost1

            k2 = (C[j], b)
            rk2 = (b, C[j])

            cost2 = min(abs(a-C[j]), N-abs(a-C[j]))

            if k2 in new_d:
                new_d[k2] = min(new_d[k2], d[(a,b)] + cost2)
            elif rk2 in new_d:
                new_d[rk2] = min(new_d[rk2], d[(a,b)] + cost2)
            elif k2 in d:
                new_d[k2] = min(d[k2], d[(a,b)] + cost2)
            elif rk2 in d:
                new_d[k2] = min(d[rk2], d[(a,b)] + cost2)
            else:
                new_d[k2] = d[(a,b)] + cost2
        d = new_d
    return min(d.values())

if __name__ == "__main__":
    Level2_Rotary_Lock_2_generator.evaluate(getMinCodeEntryTime, True)
