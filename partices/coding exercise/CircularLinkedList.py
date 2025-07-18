nodes = {}

# Create 10 nodes with circular links
for i in range(1, 11):
    nodes[i] = {
        "data": i,
        "prev": 10 if i == 1 else i - 1,   # node before
        "next": 1 if i == 10 else i + 1    # node after
    }

# Print all nodes
for i in range(1, 11):
    print(f"Node {i}: {nodes[i]}")