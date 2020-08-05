#!/usr/bin/python3

class Node:
    """Node class for each node of linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append node at the end of the list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Append node at the begun of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        """Insert after given node new node"""
        if not prev_node:
            print("Previos Node does not exist.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        """Print the linked list"""
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def delete_node(self, key):
        """Deletes node by key"""
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
        """Deletes node at position"""
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
        """Gives linked list len iterative"""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def len_recursive(self, node):
        """Gives linked list len recursive"""
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        """Swap two nodes based on them keys"""
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
        current_1.next, current_2.next = current_2.next, current_1.next

    def reverse_iterative(self):
        """Reverse linked list iterative"""
        prev = None
        current = self.head
        nxt = None

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def reverse_recursive(self):
        """Reverse linked list recursive"""
        def _reverse_recursive(current, prev):
            if not current:
                return prev

            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            return _reverse_recursive(current, prev)
        self.head = _reverse_recursive(current=self.head, prev=None)

    def merge_sorted(self, llist):
        """Merge two sorted linked list"""
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        # init the linked list in s
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def remove_duplicates(self):
        """Removes duplicate node from linked list"""
        current = self.head
        prev = None
        dup_values = dict()

        while current:
            if current.data in dup_values:
                # remove the current node
                prev.next = current.next
                current = None
            else:
                # have not encontured element before
                dup_values[current.data] = 1
                prev = current
            current = prev.next


"""llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append("1")
llist_1.append("5")
llist_1.append("7")
llist_1.append("9")
llist_1.append("10")
llist_1.append("12")
llist_1.append("14")


llist_2.append("2")
llist_2.append("3")
llist_2.append("4")
llist_2.append("6")
llist_2.append("8")

print("list self:")
llist_1.print_list()
print("list 2")
llist_2.print_list()
print()
llist_1.merge_sorted(llist_2)
llist_1.print_list()"""

llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)

print("Original Linked List")
llist.print_list()
print("Linked List After Removing Duplicates")
llist.remove_duplicates()
llist.print_list()


#llist.prepend("7")
#llist.insert_after_node(llist.head.next.next, "D")
#print(llist.len_iterative())
#print(llist.len_recursive(llist.head))
#llist.delete_node("B")
#llist.delete_node("D")
#llist.delete_node_at_pos(2)
#llist.print_list()
#print(llist.len_iterative())
#print(llist.len_recursive(llist.head))
#llist.swap_nodes("B", "C")
#print("Swapping nodes B and C that are not head nodes")
#llist.print_list()

#llist.swap_nodes("A", "B")
#print("Swapping nodes A and B where key_1 is head node")
#llist.print_list()

#llist.swap_nodes("D", "B")
#print("Swapping nodes D and B where key_2 is head node")
#llist.print_list()
#print()
#llist.reverse_iterative()
#llist.print_list()
#print()
#llist.reverse_recursive()
#print()
#llist.print_list()
