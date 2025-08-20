nodes = {}  # create an empty dictionary

# Create 10 nodes
for i in range(1, 11):
    nodes[i] = {
        "data": i,
        "prev": i - 1 if i > 1 else None,   # previous node
        "next": i + 1 if i < 10 else None   # next node
    }

# Print all nodes
for i in range(1, 11):
    print("Node", i, ":", nodes[i])