class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Create head and tail
head = None
tail = None

# Create 10 nodes with values from 1 to 10
for i in range(1, 11):
    new_node = Node(i)
    
    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        new_node.prev = tail
        tail = new_node  # Update tail

# ✅ Forward Traversal
print("Forward Traversal:")
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next

# ✅ Backward Traversal
print("\nBackward Traversal:")
temp = tail
while temp:
    print(temp.data, end=" ")
    temp = temp.prev