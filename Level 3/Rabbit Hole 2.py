import os
import sys
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level3_Rabbit_Hole_2_generator


class Page:
    def __init__(self):
        self.id = 0
        self.cluster_id = 0
        self.children: List[int] = []
        self.max_visitable = 0

    def add_child(self, page: int):
        self.children.append(page)

def internal_loop(available_links: List[int], pages: List[Page], current_page: int, stack: List[int]):
    recurse = False
    while len(available_links) > 0:
        next_page = available_links[-1]
        if pages[next_page].id == 0:
            ## Recursivly execute on next_page
            stack.append(-current_page)
            stack.append(next_page)
            recurse = True
            break

        if pages[next_page].id > 0:
            pages[current_page].cluster_id = min(pages[current_page].cluster_id, pages[next_page].id)

        del available_links[-1]
    return recurse

def getMaxVisitableWebpages(N: int, M: int, A: List[int], B: List[int]) -> int:
    #Based on Tarjan's Algorithm
    # https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
    scc_id: int = 1
    pages = [Page() for _ in range(N + 1)]

    stack: List[int]        = []
    page_history: List[int] = []

    unvisited_links: List[List[int]] = []

    ## Create adjacency list
    for i in range(M):
        pages[A[i]].add_child(B[i])

    ## Copy of adjacency lists.
    for i in range(N + 1):
        unvisited_links.append(list(pages[i].children))


    for page in range(1, N + 1):
        ## Skip if node already visited
        if pages[page].id != 0:
            continue

        ## Non-recursive Tarjan's SCC Algorithm
        stack.append(page)
        while len(stack) > 0:
            current_page = stack.pop()
            recurse = False

            ## First time seeing current_page
            if current_page > 0:
                pages[current_page].id = scc_id
                pages[current_page].cluster_id = scc_id
                scc_id += 1

                page_history.append(current_page)

                available_links = unvisited_links[current_page]
                recurse = recurse or internal_loop(available_links, pages, current_page, stack)
            else:
                current_page = -current_page
                available_links = unvisited_links[current_page]
                next_page = available_links[-1]

                pages[current_page].cluster_id = min(pages[current_page].cluster_id, pages[next_page].cluster_id)
                del available_links[-1]

                recurse = recurse or internal_loop(available_links, pages, current_page, stack)



            if recurse: continue

            ## A Strongly Connected Component Identified
            if pages[current_page].cluster_id == pages[current_page].id:
                prev_page = page_history.pop()
                pages[prev_page].id *= -pages[current_page].id
                scc = [prev_page]
                scc_size = 1

                while prev_page != current_page:
                    prev_page = page_history.pop()
                    pages[prev_page].id *= -pages[current_page].id
                    scc.append(prev_page)
                    scc_size += 1

                scc_links: set[int] = set()
                for page in scc:
                    scc_links.update(pages[page].children)

                scc_links.difference_update(scc)
                max_visitable_from_this_scc = scc_size + max([0] + [pages[page].max_visitable for page in scc_links])

                for page in scc:
                    pages[page].max_visitable = max_visitable_from_this_scc

    return max((page.max_visitable for page in pages))



if __name__ == "__main__":
    Level3_Rabbit_Hole_2_generator.evaluate(getMaxVisitableWebpages, True)
