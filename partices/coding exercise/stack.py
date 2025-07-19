stack = []  # empty stack

# Push items into the stack
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack now:", stack)

# Pop the top item
top = stack.pop()
print("Popped:", top)

# Peek at the top item
print("Top item now:", stack[-1])

# Print final stack
print("Final stack:", stack)