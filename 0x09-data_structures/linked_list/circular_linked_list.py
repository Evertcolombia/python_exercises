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

    def remove(self, node):
        if self.head:
            if self.head.data == node:
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
                    if current.data == node:
                        prev.next = current.next
                        current = current.next

    def __len__(self):
        """Override len method for this class"""
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2
        count = 0

        prev = None
        current = self.head
        while current and count < mid:
            count += 1
            prev = current
            current = current.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while current.next != self.head:
            split_cllist.append(current.data)
            current = current.next
        split_cllist.append(current.data)

        self.print_list()
        print()
        split_cllist.print_list()

    def josephus_circle(self, step):
        current = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                current = current.next
                count += 1
            print('Kill ' + str(current.data))
            self.remove(current)
            current = current.next


cllist = CircularLinkedList()
"""cllist.append("C")
cllist.append("D")
cllist.prepend("B")
cllist.prepend("A")
cllist.print_list()
print()
cllist.remove("A")
cllist.remove("C")
cllist.print_list()"""

""""cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")
cllist.split_list()"""

cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)


cllist.josephus_circle(2)
cllist.print_list()
