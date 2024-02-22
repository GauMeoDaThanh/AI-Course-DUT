import heapq

class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def __lt__(self, other):
        return self.value < other.value

def update_frontier(frontier, new_node):
    for idx, n in enumerate(frontier):
        if n == new_node:
            if frontier[idx].value > new_node.value:
                frontier[idx] = new_node
                heapq.heapify(frontier)

def GBF_search(initial_state, goalTest):
    frontier = []
    explored = []
    heapq.heapify(frontier)
    heapq.heappush(frontier, initial_state)
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        if state.name == goalTest.name:
            return explored
        for neighbor in state.children:
            if neighbor not in (frontier + explored):
                heapq.heappush(frontier, neighbor)
            elif neighbor in frontier:
                update_frontier(frontier=frontier, new_node=neighbor)
    return False

if __name__ == "__main__":
    A = Node("A", 6)
    B = Node("B", 3)
    C = Node("C", 4)
    D = Node("D", 5)
    E = Node("E", 3)
    F = Node("F", 1)
    G = Node("G", 6)
    H = Node("H", 2)
    I = Node("I", 5)
    J = Node("J", 4)
    K = Node("K", 2)
    L = Node("L", 0)
    M = Node("M", 4)
    N = Node("N", 0)
    O = Node("O", 4)

    A.addChild(B)
    A.addChild(C)
    A.addChild(C)
    B.addChild(E)
    B.addChild(F)
    C.addChild(G)
    C.addChild(H)
    D.addChild(I)
    D.addChild(J)
    F.addChild(K)
    F.addChild(L)
    F.addChild(M)
    H.addChild(N)
    H.addChild(O)

    result = GBF_search(A, L)
    if result:
        s = 'explored: '
        for i in result:
            s += i.name + " "
        print(s)
    else:
        print('404 not Found!')