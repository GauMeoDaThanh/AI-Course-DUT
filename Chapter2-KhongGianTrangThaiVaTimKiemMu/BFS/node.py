class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_children(self, list_element):
        for _ in list_element:
            self.children.append(_)