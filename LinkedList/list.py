class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# creating and traversing
n1 = Node("eggs")
n2 = Node("ham")
n3 = Node("spam")
n1.next = n2
n2.next = n3

print(n1.data, 'n1111111')
print(n2.data, 'n2222222')
print(n1.next.data, 'still n2 data from first node')

# traversal of the linked list means visiting all the nodes
current = n1
while current:
    print(current.data, 'current data')
    current = current.next

# a better and more efficient way


def iter(self):
    current = self.head
    while current:
        val = current.data
        current = current.next
        yield val

# for word in words.iter():
#   print(word)


# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

# appending items to a list
# appending to the end of the list
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        # encapsulate the data in a Node
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
