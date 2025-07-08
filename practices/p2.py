import math
import random
class Node:
    def __init__(self,parent,name,cost):
        self.name=name
        self.parent=parent
        self.cost=cost if cost is not None else random.random()
    def describe(self):
        return f"Node(name={self.name}, parent={self.parent}, cost={self.cost})"

nodeA = Node(None, "A", cost=random.random())   
nodeB = Node("A", "B", cost=random.random())
nodeC = Node("B", "C", cost=random.random())
nodeD = Node("C", "D", cost=random.random())
print(nodeA.cost)

def find_lowest_cost_node(nodes):
    lowest = nodes[0]
    for node in nodes:
        if node.cost < lowest.cost:
            lowest = node
    return lowest

lowest_nodes=[find_lowest_cost_node([nodeA, nodeB, nodeC, nodeD])]
for node in lowest_nodes:
    print(f"{node.name} has the lowest cost: {node.cost}")