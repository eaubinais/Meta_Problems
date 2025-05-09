import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level3_Stack_Stabilization_2_generator

# There's a stack of inflatable discs, with the ith disc from the top having an initial radius of R_i inches.
# The stack is considered unstable if it includes at least one disc whose radius is larger than or equal to that of the disc directly under it. In other words, for the stack to be stable, each disc must have a strictly smaller radius than that of the disc directly under it.
# As long as the stack is unstable, you can repeatedly choose a disc and perform one of the following operations:
# Inflate the disc, increasing its radius by 1 inch. This operation takes A seconds and may be performed on discs of any radius.
# Deflate the disc, decreasing its radius by 1 inch. This operation takes B seconds and may only be performed if the resulting radius is a positive integer number of inches (that is, if the disc has a radius of at least 2 inches" before being deflated).
# Determine the minimum number of seconds needed in order to make the stack stable.
# Implement the above function in the function below
# The function signature is as follows:
# def getMinStabilization(N: int, R: List[int], A: int, B: int) -> int:


def getMinStabilization(N: int, R: List[int], A: int, B: int) -> int:
    ## Redefine Problem
    R_ = [r - i for i, r in enumerate(R)]

    ## Get Key Radii
    key_radii = {max(1, r) for r in R_}
    key_radii = list(key_radii)
    key_radii.sort()

    cost_for_radius = [0] * len(key_radii)
    for r in R_:
        for i, key_radius in enumerate(key_radii):
            delta = key_radius - r
            cost = 0

            if delta > 0:
                cost = delta * A
            else:
                cost = -delta * B

            if i == 0:
                cost_for_radius[0] += cost
            else:
                cost_for_radius[i] = min(cost_for_radius[i-1], cost_for_radius[i] + cost)

    return cost_for_radius[-1]


if __name__ == "__main__":
    Level3_Stack_Stabilization_2_generator.evaluate(getMinStabilization, True)
