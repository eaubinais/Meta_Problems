import os
import sys
from typing import List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level3_Slippery_Trip_generator


def getMaxCollectableCoins(R: int, C: int, G: List[List[str]]) -> int:
    def LineType(L: List[str]) -> List[str]:
        return list(set(L))

    def FullLineValue(L: List[str], C: int) -> Tuple[int, int]:
        """
        Returns the value (a, b) of a line that has all 4 elements. See next function for a definition of value.
        """
        extended_line = L + L
        m = 0
        j = 0

        while j < C:
            if L[j] != '>':
                j+=1
                continue
            base_j = j
            val = 0
            for i in range(1, C):
                if extended_line[j+i] == 'v':
                    base_j = j+i #It is useless to test all ">" before this point as they would give less coins.
                    break
                elif extended_line[j+i] == '*':
                    val += 1
            if val > m:
                m = val
            j = base_j+1
        return (-1, 1 if m == 0 else m)



    def LineValue(L: List[str], C: int, t: List[str]) -> Tuple[int, int]:
        """
        Returns a couple (a, b) where a represents the value earned if we stay on line L
        and b is the value earned if we keep going.
        A value of -1 represents that we cannot perform the action.

        """
        #Only one element --> easy to check
        if len(t) == 1:
            if '>' in t:
                return (0, -1)
            else:
                return (-1, int('*' in t))
        #Everything is there, then compute value of full line
        if len(t) == 4:
            return FullLineValue(L, C)
        if len(t) == 2:
            if '*' not in t:
                return (-1, 0)
            if '>' in t:
                return (L.count('*') ,1)
            else:
                return (-1, 1)

        # if len(t) == 3:
        if '*' not in t:
            return (-1, 0)
        elif 'v' not in t:
            return (L.count('*'), 1)
        elif '>' not in t:
            return (-1, 1)
        else:
            return FullLineValue(L, C)

    downwards = 0
    max_stay = 0

    for L in G:
        stay, downward = LineValue(L, C, LineType(L))

        if stay >= 0:
            max_stay = max(max_stay, downwards + stay)
        if downward >= 0:
            downwards += downward
        else:
            return max_stay


    return max(downwards, max_stay)

if __name__ == "__main__":
    Level3_Slippery_Trip_generator.evaluate(getMaxCollectableCoins, True)
