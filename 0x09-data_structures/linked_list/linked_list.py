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

    def print_nth_from_last(self, n):
        """Print node data that matches from last"""
        total_len = self.len_iterative()
        current = self.head
        print(total_len)
        while current:
            if total_len == n:
                print(current.data)
                return current.data
            total_len -= 1
            current = current.next

        if current is None:
            return

    def print_nth_from_last2(self, n):
        """Return node data from node  in n from the final"""
        p = self.head
        q = self.head
        count = 0

        # make q point n nodes beyond the head
        while q:
            count += 1
            if count >= n:
                break
            q = q.next

        if not q:
            print(str(n) + "Is greater than the numbers in the list.")
            return

        while p and q.next:
            p = p.next
            q = q.next
        return p.data

    def count_occurences_iterative(self, data):
        """Count occurences of the data in a linked list"""
        count = 0
        current = self.head

        while current:
            if current.data == data:
                count += 1
            current = current.next
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0

        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        """Rotate a linked list from the follow node in k"""
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

    def is_palindrome_string(self):
        """True is a linked list is palindrome"""
        st = ""
        current = self.head

        while current:
            st += current.data
            current = current.next

        # st[::-1] reverse the string
        return st == st[::-1]

    def is_palindrome_stack(self):
        """True is a list is palindrome"""
        current = self.head
        stack = []

        while current:
            stack.append(current.data)
            current = current.next
        current = self.head
        while current:
            data = stack.pop()
            if current.data != data:
                return False
            current = current.next
        return True

    def is_palindrome_two_pointers(self):
        """True if a list is palindrome"""
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]

            count = 1
            while count <= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return False

    def move_tail_to_head(self):
        """Move tail node to head"""
        if self.head and self.head.next:
            current = self.head
            prev = None

            while current.next:
                prev = current
                current = current.next
            current.next = self.head
            prev.next = None
            self.head = current

    def sum_two_list(self, llist):
        """Sum the data of two linked list"""
        p = self.head
        q = llist.head

        sum_list = LinkedList()

        residual = 0
        while q or p:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data

            sum = i + j + residual
            num = sum % 10
            if sum >= 10:
                residual = sum // 10
            else:
                residual = 0
            sum_list.append(num)
            if p:
                p = p.next
            if q:
                q = q.next

        return sum_list


llist = LinkedList()
llist.append(5)
llist.append(6)
llist.append(3)

llist_2 = LinkedList()
llist_2.append(8)
llist_2.append(4)
llist_2.append(2)

result = llist.sum_two_list(llist_2)
result.print_list()
"""
llist = LinkedList()
llist.append("R")
llist.append("A")
llist.append("D")
llist.append("A")
llist.append("R")

llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")

print(llist.is_palindrome_string())
print(llist.is_palindrome_stack())
print(llist.is_palindrome_two_pointers())
print(llist_2.is_palindrome_string())
print(llist_2.is_palindrome_stack())
print(llist_2.is_palindrome_two_pointers())

print("before")
llist.print_list()
llist.move_tail_to_head()
print("after")
llist.print_list()"""
"""
llist_2 = LinkedList()
llist_2.append(1)
llist_2.append(2)
llist_2.append(1)
llist_2.append(3)
llist_2.append(1)
llist_2.append(4)
llist_2.append(1)
print(llist_2.count_occurences_iterative(1))
print()
print(llist_2.count_occurences_recursive(llist_2.head, 1))
print()
llist_2.print_list()
print()
llist_2.rotate(3)
llist_2.print_list()
"""
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
"""
llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)
llist.append(7)
llist.append(9)

print("Original Linked List")
llist.print_list()
print("Linked List After Removing Duplicates")
llist.remove_duplicates()
llist.print_list()
print()
data = llist.print_nth_from_last2(2)
print(data)
"""

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
