import os
import sys
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List, Set, Tuple

from sortedcontainers import SortedList

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level4_Mathematical_Art_generator


def merge_segments(segments: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    merged: List[Tuple[int, int]] = []
    segments.sort()
    for start, end in segments:
        if not merged or merged[-1][1] < start:
            merged.append((start, end))
        else:
            last = merged.pop()
            merged.append((last[0], max(last[1], end)))
    return merged


def getPlusSignCount(N: int, L: List[int], D: str) -> int:
    Vmap: defaultdict[int, List[Tuple[int, int]]] = defaultdict(list)
    Hmap: defaultdict[int, List[Tuple[int, int]]] = defaultdict(list)

    x, y = 0, 0
    for i in range(N):
        length, direction = L[i], D[i]
        if direction == 'U':
            Vmap[x].append((y, y + length))
            y += length
        elif direction == 'D':
            Vmap[x].append((y - length, y))
            y -= length
        elif direction == 'R':
            Hmap[y].append((x, x + length))
            x += length
        elif direction == 'L':
            Hmap[y].append((x - length, x))
            x -= length

    for x in Vmap:
        Vmap[x] = merge_segments(Vmap[x])
    for y in Hmap:
        Hmap[y] = merge_segments(Hmap[y])

    Openevents: defaultdict[int, List[int]] = defaultdict(list)
    Closeevents: defaultdict[int, List[int]] = defaultdict(list)
    Queryevent: defaultdict[int, List[Tuple[int, int]]] = defaultdict(list)

    xs: Set[int] = set()

    for y, spans in Hmap.items():
        for x1, x2 in spans:
            Openevents[x1].append(y)
            Closeevents[x2].append(y)
            xs.update([x1, x2])
    for x, spans in Vmap.items():
        xs.add(x)
        for y1, y2 in spans:
            Queryevent[x].append((y1, y2))

    result = 0
    active = SortedList()
    xs_ = sorted(list(xs))

    for x in xs_:
        for y in Closeevents[x]:
            active.remove(y)  # type: ignore
        for y1, y2 in Queryevent[x]:
            lo = bisect_right(active, y1)
            hi = bisect_left(active, y2)
            result += max(0, hi - lo)
        for y in Openevents[x]:
            active.add(y)  # type: ignore

    return result

if __name__ == "__main__":
    Level4_Mathematical_Art_generator.evaluate(getPlusSignCount, True)
