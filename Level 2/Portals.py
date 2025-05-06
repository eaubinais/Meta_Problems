import os
import sys
from itertools import product
from typing import List, Set, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level2_Portals_generator


def getStartPosition(R:int, C:int, G:List[List[str]]) -> Tuple[int, int]:
    for j, i in product(range(R), range(C)):
        if G[j][i] == 'S':
            return (j, i)
    #should never happen
    raise ValueError("Start position not found")

def getPositions(pos: str, R: int, C: int, G: List[List[str]]) -> Set[Tuple[int, int]]:
    return set(((j, i) for j, i in product(range(R), range(C)) if G[j][i] == pos))

def getNeighbors(position: Tuple[int, int], R: int, C: int, G: List[List[str]], seen: Set[Tuple[int, int]] = set()) -> Set[Tuple[int, int]]:
    neighbors: Set[Tuple[int, int]] = set()
    if position[0] > 0 and G[position[0]-1][position[1]] != '#' and (position[0]-1, position[1]) not in seen:
        neighbors.add((position[0]-1,position[1]))
    if position[0] < R-1 and G[position[0]+1][position[1]] != '#' and (position[0]+1, position[1]) not in seen:
        neighbors.add((position[0]+1,position[1]))
    if position[1] > 0 and G[position[0]][position[1]-1] != '#' and (position[0], position[1]-1) not in seen:
        neighbors.add((position[0],position[1]-1))
    if position[1] < C-1 and G[position[0]][position[1]+1] != '#' and (position[0], position[1]+1) not in seen:
        neighbors.add((position[0],position[1]+1))
    if G[position[0]][position[1]] not in ['#', '.', 'S', 'E']:
        new_pos = getPositions(G[position[0]][position[1]], R, C, G)
        neighbors.update(new_pos)
    return neighbors


def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    start_position = getPositions('S', R, C, G).pop()
    neighbors = getNeighbors(start_position, R, C, G, set())

    seen: Set[Tuple[int, int]] = set(neighbors)
    seen.add(start_position)

    val = 1

    while len(neighbors) > 0:
        new_neighbors: Set[Tuple[int, int]] = set()
        for neigh in neighbors:
            pos = G[neigh[0]][neigh[1]]
            if pos == 'E':
                return val
            neighbors_of_neigh = getNeighbors(neigh, R, C, G, seen)
            new_neighbors.update(neighbors_of_neigh - seen)

        neighbors = new_neighbors
        seen.update(neighbors)
        val += 1

    return -1

if __name__ == "__main__":
    Level2_Portals_generator.evaluate(getSecondsRequired, True)
