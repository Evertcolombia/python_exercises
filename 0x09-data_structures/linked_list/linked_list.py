#!/usr/bin/python3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previos Node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete_node(self, key):
        current = self.head
        # if key is in head.data
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return

        prev.next = current.next
        current = None

    def delete_node_at_pos(self, pos):
        if self.head:
            current = self.head
            # if pos is head
            if pos == 0:
                self.head = current.next
                self.head = None
                return

            prev = None
            count = 0
            while current and count != pos:
                prev = current
                current = current.next
                count += 1

            if current is None:
                return
            prev.next = current.next
            current = None

    def len_iterative(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        current_1 = self.head
        while current_1 and current_1.data != key_1:
            prev_1 = current_1
            current_1 = current_1.next

        prev_2 = None
        current_2 = self.head
        while current_2 and current_2.data != key_2:
            prev_2 = current_2
            current_2 = current_2.next

        if not current_1 or not current_2:
            return
        if prev_1:
            prev_1.next = current_2
        else:
            self.head = current_2
        if prev_2:
            prev_2.next = current_1
        else:
            self.head = current_1

        current_1.next = current_2.next
        current_2.next = current_1.next

    def reverse_iterative(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.prepend("D")

llist.insert_after_node(llist.head.next.next, "E")
#print(llist.len_iterative())
#print(llist.len_recursive(llist.head))
#llist.delete_node("B")
#llist.delete_node("D")
#llist.delete_node_at_pos(2)
llist.print_list()
#print(llist.len_iterative())
#print(llist.len_recursive(llist.head))
llist.swap_nodes("B", "C")
print("Swapping nodes B and C that are not head nodes")
llist.print_list()

llist.swap_nodes("A", "B")
print("Swapping nodes A and B where key_1 is head node")
llist.print_list()

llist.swap_nodes("D", "B")
print("Swapping nodes D and B where key_2 is head node")
llist.print_list()
