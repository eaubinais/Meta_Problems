import os
import sys
from typing import Dict, List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import Level3_Rabbit_Hole_2_generator


class Node:
    def __init__(self, value: int, idx: int):
        self.value = value
        self.idx: int = idx
        self.children: List[int] = []
        self.parents: List[int] = []

        # 0 - not visited
        # 1 - visited and simple node
        # 2 - visited and complex node
        # 3 - finished
        self.visited: int = 0

    def add_child(self, child_node_idx: int):
        self.children.append(child_node_idx)

    def add_parent(self, parent_node_idx: int):
        self.parents.append(parent_node_idx)

    def remove_child(self, child_node_idx: int):
        self.children.remove(child_node_idx)

    def remove_parent(self, parent_node_idx: int):
        self.parents.remove(parent_node_idx)

    def add_value(self, value: int):
        self.value += value

    @property
    def children_count(self) -> int:
        return len(self.children)

    @property
    def parents_count(self) -> int:
        return len(self.parents)

class Tree:
    def __init__(self, N: int):
        self.nodes: Dict[int, Node] = {i: Node(1, i) for i in range(N)}
        self.max_index: int = N - 1
        self.num_nodes: int = N

    def add_edge(self, parent_idx: int, child_idx: int):
        self.nodes[parent_idx].add_child(child_idx)
        self.nodes[child_idx].add_parent(parent_idx)

    def remove_edge(self, parent_idx: int, child_idx: int):
        self.nodes[parent_idx].remove_child(child_idx)
        self.nodes[child_idx].remove_parent(parent_idx)

    def remove_node(self, idx: int):
        for child in self.nodes[idx].children:
            self.nodes[child].remove_parent(idx)
        for parent in self.nodes[idx].parents:
            self.nodes[parent].remove_child(idx)
        del self.nodes[idx]
        self.num_nodes -= 1

    def add_node(self, value: int) -> int:
        new_node = Node(value, self.new_idx())
        self.nodes[new_node.idx] = new_node
        self.num_nodes += 1
        return new_node.idx

    def add_value(self, idx: int, value: int):
        self.nodes[idx].add_value(value)

    def new_idx(self) -> int:
        self.max_index += 1
        return self.max_index

    def merge(self, indexes: List[int]):
        if len(indexes) < 2:
            return

        root_node = self.nodes[indexes[0]]

        for idx in indexes[1:]:
            for parent in self.nodes[idx].parents:
                if parent not in indexes:
                    self.remove_edge(parent, idx)
                    root_node.add_parent(parent)
                    self.nodes[parent].add_child(root_node.idx)
            for child in self.nodes[idx].children:
                if child not in indexes:
                    self.remove_edge(idx, child)
                    root_node.add_child(child)
                    self.nodes[child].add_parent(root_node.idx)
        for idx in indexes[1:]:
            self.remove_node(idx)
        self.max_index = max(self.nodes.keys())
        root_node.add_value(len(indexes) - 1)


    def reset_visited(self):
        for node in self.nodes.values():
            node.visited = 0

    @property
    def indexes(self) -> List[int]:
        return list(self.nodes.keys())

    def first_0_child(self, index: int) -> int:
        for idx in self.nodes[index].children:
            if self.nodes[idx].visited == 0:
                return idx
        return -1

    def first_12_child(self, index: int) -> int:
        for idx in self.nodes[index].children:
            if self.nodes[idx].visited in [1, 2]:
                return idx
        return -1

def getMaxVisitableWebpages(N: int, M: int, A: List[int], B: List[int]) -> int:
    graph = Tree(N)
    for i in range(M):
        graph.add_edge(A[i]-1, B[i]-1)


    # Remove all cycles
    while True:
        for idx in graph.indexes:
            if graph.nodes[idx].visited != 0:
                continue

            node = graph.nodes[idx]
            path: List[int] = []

            cycle: List[int] = []

            while True:
                if node.children_count == 0:
                    node.visited = 3

                    if path == []:
                        break
                    node = graph.nodes[path.pop()]
                elif node.children_count == 1:
                    if graph.nodes[node.children[0]].visited == 0:
                        node.visited = 1
                        path.append(node.idx)
                        node = graph.nodes[node.children[0]]
                    elif graph.nodes[node.children[0]].visited in [1,2]:
                        #Cycle found
                        cycle = path[path.index(node.children[0]):]
                        cycle.append(node.idx)
                        break
                    elif graph.nodes[node.children[0]].visited == 3:
                        #End of path
                        node.visited = 3

                        if path == []:
                            break
                        node = graph.nodes[path.pop()]
                elif node.children_count > 1:
                    if graph.first_12_child(node.idx) != -1:
                        #Cycle found
                        cycle = path[path.index(graph.first_12_child(node.idx)):]
                        cycle.append(node.idx)
                        break
                    elif graph.first_0_child(node.idx) != -1:
                        #Path found
                        node.visited = 2
                        path.append(node.idx)
                        node = graph.nodes[graph.first_0_child(node.idx)]
                    else:
                        #End of path
                        node.visited = 3

                        if path == []:
                            break
                        node = graph.nodes[path.pop()]

            if cycle != []:
                graph.merge(cycle)
                graph.reset_visited()
                break
        else:
            break

    # Get the values
    graph.reset_visited()

    for idx in graph.indexes:
        if graph.nodes[idx].visited != 0:
            continue

        node = graph.nodes[idx]
        path = []

        while True:
            if node.children_count == 0:
                node.visited = 3

                if path == []:
                    break
                node = graph.nodes[path.pop()]
            elif node.children_count == 1:
                if graph.nodes[node.children[0]].visited == 0:
                    path.append(node.idx)
                    node = graph.nodes[node.children[0]]
                elif graph.nodes[node.children[0]].visited == 3:
                    node.visited = 3
                    node.add_value(graph.nodes[node.children[0]].value)

                    if path == []:
                        break
                    node = graph.nodes[path.pop()]
            elif node.children_count > 1:
                if graph.first_0_child(node.idx) != -1:
                    path.append(node.idx)
                    node = graph.nodes[graph.first_0_child(node.idx)]
                else:
                    node.visited = 3
                    node.add_value(max(graph.nodes[child].value for child in node.children))

                    if path == []:
                        break
                    node = graph.nodes[path.pop()]

    return max(node.value for node in graph.nodes.values())



if __name__ == "__main__":
    Level3_Rabbit_Hole_2_generator.evaluate(getMaxVisitableWebpages, False)
