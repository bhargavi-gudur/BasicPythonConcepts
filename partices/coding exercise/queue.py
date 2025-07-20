queue = []  # empty queue

# Enqueue (add to back)
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue now:", queue)

# Dequeue (remove from front)
first = queue.pop(0)
print("Removed:", first)

# Peek front item
print("Front item now:", queue[0])

# Final queue
print("Final queue:", queue)