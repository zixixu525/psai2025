class Node:
    def __init__(self,parent,name,cost):
        self.name=name
        self.parent=parent
        self.cost=cost
    def describe(self):
        return f"Node(name={self.name}, parent={self.parent}, cost={self.cost})"

nodeA = Node(None, "A", 0)   
nodeB = Node("A", "B", 0)
nodeC = Node("B", "C", 0)
nodeD = Node("C", "D", 0)

nodes = [nodeA, nodeB, nodeC, nodeD]

class chain:
    def __init__(self, nodes):
        self.nodes = nodes

    def describe(self):
        return " -> ".join(node.name for node in self.nodes)

print(chain(nodes).describe())

