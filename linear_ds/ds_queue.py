"""
A queue or FIFO (first in, first out) is an abstract data type that serves as a collection of elements, with two
principal operations: enqueue, the process of adding an element to the collection. (The element is added from the rear
side) and dequeue, the process of removing the first elemet that was added (the element is removed from the front side).
It can be implemented by using both array or linked list.

Insertion : O(1)
Deletion  : O(1)
Access Time : O(n) [Worst Case]
"""

class Node:
    def __init__(self, dat):
        self.dat = dat
        self.nxt = None

class Queue:
    def __init__(self):
        self.head = None

    def display_queue(self):
        if self.head is None:
            print("Queue is empty")
            return
        else:
            print("Queue is : \n")
            n = self.head
            while n is not None:
                print(f"{n.dat} :: ", end="")
                n = n.nxt
            print()

    def enqueue(self, dat):
        temp = Node(dat)
        if self.head is None:
            self.head  = temp
            return

        n = self.head
        while n.nxt is not None:
            n = n.nxt
        n.nxt = temp

    def dequeue(self):
        if self.head is None:
            return
        else:
            out = self.head
            self.head = self.head.nxt
            return out

    def count_queue_elements(self):
        n = self.head
        count = 0
        while n is not None:
            count += 1
            n = n.nxt
        print(f"Number of elements in queue : {count}")
        return count


    def create_queue(self):
        num_elem = int(input("Enter the number of elements in the queue : "))
        if num_elem == 0:
            return

        for node in range(num_elem):
            dat = input("Enter the element to be inserted : ")
            self.enqueue(dat)


########################################################################################################################
my_queue = Queue()
my_queue.create_queue()

while True:
    print("1.Display queue")
    print("2.Count the elements in the queue")
    print("3.Enqueue element")
    print("4.Dequeue")
    print("5.Quit")

    option = int(input("Please choose an option"))

    if option == 1:
        my_queue.display_queue()
    elif option == 2:
        my_queue.count_queue_elements()
    elif option == 3:
        dat = input("Enter the data to be enqueued : ")
        my_queue.enqueue(dat)
    elif option == 4:
        my_queue.dequeue()
    elif option == 5:
        break
    else:
        print("Wrong option")
    print()

