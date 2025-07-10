class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Manually creating a circular linked list for traversal
    def create_list(self, elements):
        if not elements:
            return
        self.head = Node(elements[0])
        temp = self.head
        for data in elements[1:]:
            new_node = Node(data)
            temp.next = new_node
            temp = new_node
        temp.next = self.head  # Making the list circular

    # Traverse the list
    def traverse(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(head)")

# Example usage
cll = CircularLinkedList()
cll.create_list([10, 20, 30, 40])
cll.traverse()