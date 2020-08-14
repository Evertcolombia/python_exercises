#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append node at the end of list"""
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head

            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        """Prepend node at begun of the list"""
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def print_list(self):
        """Prin double linked list"""
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def add_after_node(self, key, data):
        """Add node after node with key"""
        current = self.head
        while current:
            if current.next is None and current.data == key:
                self.append(data)
                return
            elif current.data == key:
                new_node = Node(data)
                nxt = current.next
                current.next = new_node
                new_node.next = nxt
                new_node.prev = current
                nxt.prev = new_node
                return
            current = current.next

    def add_before_node(self, key, data):
        """Add new node before node with key"""
        current = self.head
        while current:
            if current.prev is None and current.data == key:
                self.prepend(data)
                return
            elif current.data == key:
                new_node = Node(data)
                prev = current.prev
                prev.next = new_node
                current.prex = new_node
                new_node.next = current
                new_node.prev = prev
                return
            current = current.next

    def delete(self, key):
        """Deletes Node from list"""
        current = self.head
        while current:
            if current.data == key and current == self.head:
                if not current.next:
                    current = None
                    self.head = None
                    return
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return
            elif current.data == key:
                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next


"""dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

dllist.add_after_node(3,6)
dllist.add_before_node(4,9)

dllist.print_list()"""

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.delete(1)
dllist.delete(6)
dllist.delete(4)

dllist.delete(3)
dllist.print_list()
