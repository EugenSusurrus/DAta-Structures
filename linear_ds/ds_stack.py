"""
A stack or LIFO (last in, first out) is an abstract data type that serves as a collection of elements, with two principal
operations: push, which adds an element to the collection, and pop, which removes the last element that was added.
In stack, both the operations of push and pop take place at the same end, that is the top of the stack. It can be
implemented by using both linked lists and arrays.

Insertion : O(1)
Deletion :  O(1)
Access Time : O(n) [Worst Case]
Insertion and Deletion are allowed on one end

"""

class Node():
    def __init__(self, dat):
        self.dat = dat
        self.nxt = None

class Stack:
    def __init__(self):
        self.ptr = None

    def display_stack(self):
        if self.ptr is None:
            print("Stack is empty")
            return
        else:
            print("Stack is: \n")
            n = self.ptr
            while n is not None:
                print(f"{n.dat}\n|\n", end="")
                n = n.nxt
            print()

    def push(self, dat):
        temp = Node(dat)
        if self.ptr is None:
            self.ptr = temp
            return

        n = self.ptr
        while n.nxt is not None:
            n = n.nxt
        n.nxt = temp

    def create_stack(self):
        n = int(input("Enter the number of nodes in the stack : "))
        if n == 0:
            return

        for node in range(n):
            dat = input("Enter the element to be inserted : ")
            self.push(dat)

    def pop(self):
        # Case stack is empty
        if self.ptr is None:
            return

        # Case stack contains only one element
        if self.ptr.nxt is None:
            popped = self.ptr.dat
            self.ptr = None
            return popped

        # Gets the ptr to the last element of stack
        n = self.ptr
        while n.nxt.nxt is not None:
            n = n.nxt

        # Pops last element of stack
        popped = n.nxt.dat
        n.nxt = None
        return popped

    def count_stack_elements(self):
        n = self.ptr
        num_elem = 0
        while n is not None:
            num_elem += 1
            n = n.nxt
        print(f"Number of elements in the stack is : {num_elem}")
        return num_elem

########################################################################################################################
my_stack = Stack()
my_stack.create_stack()

while True:
    print("1.Display stack")
    print("2.Count the number of elements in the stack")
    print("3.Push element to stack")
    print("4.Pop element out of stack")
    print("5.Quit")

    option = int(input("Please chose an option : "))

    if option == 1:
        my_stack.display_stack()
    elif option == 2:
        my_stack.count_stack_elements()
    elif option == 3:
        data = input("Insert the data to be pushed to the stack : ")
        my_stack.push(data)
    elif option == 4:
        my_stack.pop()
    elif option == 5:
        break
    else:
        print("Wrong option")
    print()
