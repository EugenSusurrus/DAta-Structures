"""
In case of doubly linked lists there are two references associated with each node. One of the references points
to the next node and one points to the previous node. Advantage of this data structure is that we can traverse in
both the directions and for deletion we don't need to have explicit access to the previous node.

NULL<-1<->2<->3->NULL

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def display_list(self):
        if self.head is None:
            print("NULL")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" <-> ")
                n = n.next


    def count_nodes(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        print(f"Number of nodes : {count}")
        return count


    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            cur = self.head
            new_node = Node(data)
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur


    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            cur = self.head
            new_node = Node(data)
            cur.prev = new_node
            new_node.next = cur
            self.head = new_node


    def insert_after(self, data, x):
        cur = self.head

        # Get the node with the data x
        while cur is not None:
            if cur.data == x:
                break
            cur = cur.next

        if cur is None:
            print(f"Element {x} not present in the list")
        elif cur.next is None and cur.data == x:
            self.append(data)
        else:
            new_node = Node(data)
            new_node.next = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next.prev = new_node


    def insert_before(self, data, x):
        cur = self.head

        while cur is not None:
            if cur.data == x:
                break
            cur = cur.next

        if cur is None:
            print(f"Element {x} ot found in the list")
        elif cur.prev is None and cur.data == x:
            self.prepend(data)
        else:
            new_node = Node(data)
            new_node.prev = cur.prev
            cur.prev = new_node
            new_node.next = new_node.prev.next
            new_node.prev.next = new_node


    def insert_at_position(self, data, k):
        cur = self.head
        cur_pos = 0
        while cur is not None and cur_pos <k:
            cur = cur.next
            cur_pos += 1

        if cur is None:
            print("List is empty or index is out of range")
            return

        if cur_pos == 0 and cur is not None:
            self.prepend(data)
        else:
            new_node = Node(data)
            new_node.prev = cur.prev
            cur.prev = new_node
            new_node.next = new_node.prev.next
            new_node.prev.next = new_node


    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.head.prev = None


    def delete_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        cur.next.prev = None
        cur.next = None

    def delete_key(self, x):
        cur = self.head
        if cur is None:
            print("List is empty")
            return
        while cur:
            if cur.data == x and cur == self.head:
                self.delete_first()
                return
            elif cur.data == x and cur.next is None:
                self.delete_last()
                return
            elif cur.data == x and cur.next is not None:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur.next = None
                cur.prev = None
                return
            cur = cur.next


    def _delete_node(self, node):
        cur = self.head
        if cur is None:
            print("List is empty")
            return
        while cur:
            if cur == node and cur == self.head:
                self.delete_first()
                return
            elif cur == node and cur.next is None:
                self.delete_last()
                return
            elif cur == node and cur.next is not None:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur.next = None
                cur.prev = None
                return

            cur = cur.next


    def reverse_list(self):

        if self.head is None or self.head.next is None:
            return

        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev

        if tmp:
            self.head = tmp.prev


    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur is not None:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self._delete_node(cur)
                cur = nxt


    def bubble_sort_exdata(self):
        end = None
        while self.head != end:
            cur = self.head
            while cur.next != end:
                nxt = cur.next
                if cur.data > nxt.data:
                    cur.data, nxt.data = nxt.data, cur.data
                cur = cur.next
            end = cur



    def bubble_sort_exlinks(self):
        pass


########################################################################################################################

my_doubly_linked_list = DoublyLinkedList()

while True:
    print("1.Display list")
    print("2.Append element to the list")
    print("3.Prepend element to the list")
    print("4.Insert element after")
    print("5.Insert element before")
    print("6.Insert element at position")
    print("7.Delete first node in the list")
    print("8.Delete last node in the list")
    print("9.Delete node by data in the list")
    print("10.Reverse list")
    print("11.Remove duplicates")
    print("12.Bubble sort exchanging data")
    print("13.Quit")
    print()

    option = int(input("Please choose an option!"))

    if option == 1:
        my_doubly_linked_list.display_list()
    elif option == 2:
        data = int(input("Insert data to be appended to the list : "))
        my_doubly_linked_list.append(data)
    elif option == 3:
        data = int(input("Insert data to be prepended to the list : "))
        my_doubly_linked_list.prepend(data)
    elif option == 4:
        data = int(input("Enter the data to be inserted : "))
        x = int(input("After which element to insert data : "))
        my_doubly_linked_list.insert_after(data, x)
    elif option == 5:
        data = int(input("Enter the data to be inserted : "))
        x = int(input("Before which element to insert data : "))
        my_doubly_linked_list.insert_before(data, x)
    elif option == 6:
        data = int(input("Enter the data to be inserted : "))
        k = int(input("Enter the position at which the data has to be inserted : "))
        my_doubly_linked_list.insert_at_position(data, k)
    elif option == 7:
        my_doubly_linked_list.delete_first()
    elif option == 8:
        my_doubly_linked_list.delete_last()
    elif option == 9:
        x = int(input("Choose the data to be deleted from the list : "))
        my_doubly_linked_list.delete_key(x)
    elif option == 10:
        my_doubly_linked_list.reverse_list()
    elif option == 11:
        my_doubly_linked_list.remove_duplicates()
    elif option == 12:
        my_doubly_linked_list.bubble_sort_exdata()
    elif option == 13:
        break
    else:
        print("Option not available!")
    print('\n')


