from node import Node


def BFS(initial_state, goal):
    frontier = [initial_state]
    explored = []
    while frontier:
        state = frontier.pop(0)
        explored.append(state)
        if goal == state.name:
            return explored
        for child in state.children:
            if child not in (explored and frontier):
                frontier.append(child)
    return False

if __name__ == "__main__":
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")
    node_g = Node("G")
    node_h = Node("H")
    node_i = Node("I")
    node_j = Node("J")
    node_k = Node("K")
    node_l = Node("L")
    node_m = Node("M")
    node_n = Node("N")
    node_o = Node("O")
    node_a.add_children([node_b, node_c])
    node_b.add_children([node_d, node_e])
    node_c.add_children([node_f, node_g])
    node_d.add_children([node_h, node_i])
    node_e.add_children([node_j, node_k])
    node_f.add_children([node_l, node_m])
    node_g.add_children([node_n, node_o])

    result = BFS(node_a, "H")
    if result:
        s = "explored: "
        for i in result:
            s += i.name + " "
            print(s)
    else:
        print("404 not found")