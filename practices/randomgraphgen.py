import random

def generate_random_graph_adjlist(n, p, min_deg):
    """
    Generate a random undirected graph as an adjacency list.
    
    Parameters:
    - n: number of nodes
    - p: probability of adding an edge between any pair
    - min_deg: minimum degree for each node

    Returns:
    - adjacency_list: dict mapping node -> set of neighbors
    """
    adjacency_list = {i: set() for i in range(n)}

    # Step 1: Randomly add edges with probability p
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:
                adjacency_list[i].add(j)
                adjacency_list[j].add(i)

    # Step 2: Ensure minimum degree
    for node in range(n):
        while len(adjacency_list[node]) < min_deg:
            # Choose a new node to connect
            possible_nodes = [x for x in range(n)
                              if x != node and x not in adjacency_list[node]]
            if not possible_nodes:
                break  # Fully connected for this node
            target = random.choice(possible_nodes)
            adjacency_list[node].add(target)
            adjacency_list[target].add(node)

    return adjacency_list

# Example usage
n = 10
p = 0.2
min_deg = 2

adjlist = generate_random_graph_adjlist(n, p, min_deg)

# Print the adjacency list nicely
for node, neighbors in adjlist.items():
    print(f"{node}: {sorted(neighbors)}")