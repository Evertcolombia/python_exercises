class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        current = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while current.next != self.head:
                current = current.next
            current.next = new_node
        self.head = new_node

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            if current == self.head:
                break

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                current = self.head
                while current.next != self.head:
                    current = current.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    current.next = self.head.next
                    self.head = self.head.next
            else:
                current = self.head
                prev = None
                while current.next != self.head:
                    prev = current
                    current = current.next
                    if current.data == key:
                        prev.next = current.next
                        current = current.next


cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()
print()
cllist.remove("A")
cllist.remove("C")
cllist.print_list()
