# Single linked lists implementation

class Node:
    def __init__(self, value):
        self.info = value       # The value stored in the node
        self.link = None        # The link to the next node (points to none by default)

class SingleLinkedList:

    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty!")
            return
        else:
            print("List is :\t")
            p = self.start
            while p is not None:
                print(f"{p.info} -> ", end="")
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        num_nodes = 0
        while p is not None:
            num_nodes += 1
            p = p.link
        print(f"Number of nodes in the list is : {num_nodes}")
        return num_nodes

    def search(self, x):
        position = 0
        p = self.start
        while p is not None:
            if p.info == x:
                print(f"{x} is at position {position}")
                return True
            position += 1
            p = p.link
        else:
            print(f"{x} is not found in the list")
            return False

    def insert_in_begining(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insert_at_end(self, data):
        temp = Node(data)
        if self.start is None:
            self.start = temp
            return

        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

    def create_list(self):
        n = int(input("Enter the number of nodes : "))
        if n == 0:
            return
        for node in range(n):
            data = int(input("Enter the element to be inserted : "))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link

        if p is None:
            print(f"{x} not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_before(self, data, x):
        # If list is empty
        if self.start is None:
            print("List is empty")
            return

        # x is the first node, new node is to be inserted before first node
        if x == self.start.info:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        # find reference to predecesor of node containing x
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print(f"{x} not present in the list")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insert_at_position(self, data, k):
        if k == 0:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return

        p = self.start
        i = 0
        while i < k - 1 and p is not None:
            p = p.link

        if p is None:
            print(f"You can insert only up to position {i}")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def delete_node(self, x):
        if self.start is None:
            print("List is empty")
            return

        # Deletion of the first node
        if self.start.info == x:
            self.start = self.start.link
            return

        # Deletion in between or at the end of a list
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link

        if p.link is None:
            print(f"Element {x} not in list")
        else:
            p.link = p.link.link

    def delete_first_node(self):
        if self.start is None:
            return
        self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            return

        if self.start.link is None:
            self.start = None
            return

        p = self.start
        while p.link.link is not None:
            p = p.link
        p.link = None

    def reverse_list(self):
        if self.start is None:
            return

        if self.start.link is None:
            return

        prev_node = None
        cur_node = self.start
        while cur_node:
            nxt = cur_node.link
            cur_node.link = prev_node
            prev_node = cur_node
            cur_node = nxt

        self.start = prev_node

    def bubble_sort_exdata(self):
        end = None
        while self.start != end:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def bubble_sort_exlinks(self):
        end = None
        while self.start != end:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    p, q = q, p
                r = p
                p = p.link
            end = p

    def has_cycle(self):
        if self.start is None:
            return False

        fast = self.start.link
        slow = self.start

        while fast is not None and fast.link is not None and slow is not None:
            if fast == slow:
                return True
            fast = fast.link.link
            slow = slow.link

        return False

    def find_cycle(self):
        """Detects the cycle and returns the loop node"""
        if self.start is None or self.start.link is None:
            return

        slow = self.start
        fast = self.start

        slow = slow.link
        fast = fast.link.link

        while fast and fast.link:
            if slow is fast:
                break
            slow = slow.link
            fast = fast.link.link

        return fast

    def remove_cycle(self):

        # Detects the cycle and returns the cycle node
        if self.has_cycle():
            fast = self.find_cycle()
            slow = self.start

        # Move both pointers at the same speed
        while slow.link is not fast.link:
            slow = slow.link
            fast = fast.link

        # Remove the loop by disconecting the last node
        fast.link = None


    def insert_cycle(self, x):
        """Inserts a loop at the position x of the linked list"""

        if self.start is None:
            print("List is empty")
            return

        num_nodes = self.count_nodes()

        if x < num_nodes:
            if self.start.link is None:
                self.start.link = self.start
        else:
            print(f"Index out of range. You can insert a loop up to position {num_nodes - 1}")

        p = self.start

        # Traverse till the joint point x
        i = 0
        while i < x:
            p = p.link
            i += 1
        joint_node = p

        # Traverse till the end of the list
        while p.link is not None:
            p = p.link
        p.link = joint_node

    def merge2(self, list2):
        """Merges 2 sorted lists"""
        pass
    def _merge2(self, p1, p2):
        """Merges 2 sorted lists with the head pointers p1 and p2 accordingly"""
        merged_list = SingleLinkedList()
        merged_list.insert_at_end('dummy')

        while(1):
            if p1 is None:
                dummy_node.link = p2
                break

            elif p2 is None:
                dummy_node.link = p1
                break

            if p1.info <= p2.info:
                merged_list.insert_at_end(p1.info)
            elif p2.info <= p1.info:
                merged_list.insert_at_end(p2.info)

        merged_list.delete_first_node()
        return merged_list

    def merge_sort(self):
        if self.start in None or self.start.link is None:
            return


    def _merge_sort_rec(self, listStart):
        pass

    def _divide_list(selfself, p):
        pass

########################################################################################################################

my_list = SingleLinkedList()

my_list.create_list()

while True:
    print("1.Display list")
    print("2.Count the number of nodes")
    print("3.Search for an element")
    print("4.insert in empty list/Insert in beginning of the list")
    print("5.Insert a node at the end of the list")
    print("6.Insert a node after a specified node")
    print("7.Insert a node before a specified node")
    print("8.Insert a node at a given position")
    print("9.Delete first node")
    print("10.Delete last node")
    print("11.Delete any node")
    print("12.Reverse the list")
    print("13.Bubble sort by exchanging data")
    print("14.Bubble sort by exchanging links")
    print("15.Merge sort")
    print("16.Insert cycle")
    print("17.Detect cycle")
    print("18.Remove cycle")
    print("19.Quit")


    option = int(input("Enter your choice : "))

    if option == 1:
        my_list.display_list()
    elif option == 2:
        my_list.count_nodes()
    elif option == 3:
        data = int(input("Enter the element to be searched : "))
        my_list.search(data)
    elif option == 4:
        data = int(input("Enter the element to be inserted : "))
        my_list.insert_in_begining(data)
    elif option == 5:
        data = int(input("Enter the element to be inserted : "))
        my_list.insert_at_end(data)
    elif option == 6:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the position after which to insert : "))
        my_list.insert_after(data, x)
    elif option == 7:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the position before which to insert"))
        my_list.insert_before(data, x)
    elif option == 8:
        data = int(input("Enter the element to be inserted : "))
        x = int(input("Enter the position at which to insert : "))
        my_list.insert_at_position(data, x)
    elif option == 9:
        my_list.delete_first_node()
    elif option == 10:
        my_list.delete_last_node()
    elif option == 11:
        data = input("Enter the element to be deleted : ")
        my_list.delete_node(data)
    elif option == 12:
        my_list.reverse_list()
    elif option == 13:
        my_list.bubble_sort_exdata()
    elif option == 14:
        my_list.bubble_sort_exlinks()
    elif option == 15:
        my_list.merge_sort()
    elif option == 16:
        data = int(input("Enter th element at which the cycle has to be inserted : "))
        my_list.insert_cycle(data)
    elif option == 17:
        if my_list.has_cycle():
            print("List has a cycle")
        else:
            print("List does not have a cycle")
    elif option == 18:
        my_list.remove_cycle()
    elif option == 19:
        break
    else:
        print("Wrong option")
    print()
