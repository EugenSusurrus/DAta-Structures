"""
Trees are hierarchical data structures

A binary tree is a tre data structure in which each node has at most two children, which are refered to as
left child and right child. It is implemented using links

A tree is represented by a pointer to the topmost node in tree. If the tree is empty, then value of root is NULL.
A binary tree node contains the following parts:
    1. Data
    2. Pointer to left child
    3. Pointer to right child

A BT can be traversed in three ways:
    1. Inorder (Left -> Root -> Right)
    2. Preorder (Root -> Left -> Right)
    3. Postorder (Left -> Right -> Root)

Binary Tree Properties:

* The maximum number of nodes at level ‘l’ = 2l-1.

* Maximum number of nodes = 2h – 1.
Here h is height of a tree. Height is considered
as is maximum number of nodes on root to leaf path

* Minimum possible height =  ceil(Log2(n+1))

* In Binary tree, number of leaf nodes is always one
more than nodes with two children.

* Time Complexity of Tree Traversal: O(n)
"""

class BST_Node:

    def __init__(self, dat):
        self.dat = dat          # Node data
        self.left = None        # pointer to left child
        self.right = None       # pointer to right child


    def insert(self, dat):
        if self.dat == dat:
            print("Choose a value different to the value held in the current node")
            return

        if self.dat < dat:
            if self.right is None:
                self.right = BST_Node(dat)
            else:
                self.right.insert(dat)
        else:
            if self.left is None:
                self.left = BST_Node(dat)
            else:
                self.left.insert(dat)

    def display_tree(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height and horizontal coordinate of the root."""
        # No child
        if self.right is None and self.left is None:
            line = '%s' % self.dat
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.dat
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Only right child
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.dat
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.dat
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def is_member(self, val):
        if val == self.dat:
            print(f"{val} is found in the BST")
            return True
        elif val < self.dat:
            if self.left is None:
                print(f"{val} is NOT found in the BST")
                return False
            else:
                return self.left.is_member(val)
        else:
            if self.right is None:
                print(f"{val} is NOT found in the BST")
                return False
            else:
                return self.right.is_member(val)

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()

        print(self.dat, end=" ")

        if self.right is not None:
            self.right.print_in_order()

    def print_pre_order(self):
        print(self.dat, end=" ")

        if self.left is not None:
            self.left.print_pre_order()

        if self.right is not None:
            self.right.print_pre_order()

    def print_post_order(self):
        if self.left is not None:
            self.left.print_post_order()

        if self.right is not None:
            self.right.print_post_order()

        print(self.dat, end=" ")

    def print_level_order(self):
        if self is None:
            return

        # Create an empty queue FIFO
        queue = []

        # Enqueue root and initialize height
        queue.append(self)

        while len(queue) > 0:
            # Print front of queue and dequeue
            print(queue[0].dat, end=" ")
            node = queue.pop(0)

            # Enqueue left child
            if node.left is not None:
                queue.append(node.left)

            # Equeue right child
            if node.right is not None:
                queue.append(node.right)

    def print_reverse_level_order(self):
        # Create an empty queue q and an empty stack s
        q = []
        s = []

        # Enqueue the root node in the queue
        q.append(self)

        while len(q) > 0:
            node = q.pop(0)
            s.append(node)

            if node.right is not None:
                q.append(node.right)

            if node.left is not None:
                q.append(node.left)

        while len(s) > 0:
            node = s.pop(-1)
            print(node.dat, end=" ")

    def _get_height(self, node):
        """Returns the number of nodes on longest path from root to the deepest node"""
        if node is None:
            return 0

        left_depth = self._get_height(node.left)
        right_depth = self._get_height(node.right)

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1


    def get_size(self):
        if self is None:
            return 0

        s = []
        s.append(self)
        size = 1
        while s:
            node = s.pop(-1)
            if node.left:
                size += 1
                s.append(node.left)
            if node.right:
                size += 1
                s.append(node.right)

        return size

    def _get_size(self, node):
        if node is None:
            return 0
        return 1 + self._get_size(node.left) + self._get_size(node.right)

########################################################################################################################


root_dat = int(input("Insert the data for the first node in the tree >>> "))

my_tree = BST_Node(root_dat)

while True:
    print("1.Display tree.")
    print("2.Insert data.")
    print("3.Check if a value is contained in the BST.")
    print("4.Print tree IN-ORDER fashion (Left -> Root -> Right).")
    print("5.Print tree PRE-ORDER fashion (Root -> Left -> Right).")
    print("6.Print tree POST-ORDER fashion (Left -> Right -> Root).")
    print("7.Print tree LEVEL-ORDER fashion.")
    print("8.Print tree REVERSE-LEVEL-ORDER fashion.")
    print("9.Get the height of the binary tree.")
    print("10.Get the size of the binary tree.")
    print("11.Quit.")

    option = int(input("Please choose an option >>> "))

    if option == 1:
        my_tree.display_tree()
    elif option == 2:
        info = int(input("Data to be inserted : "))
        my_tree.insert(info)
    elif option == 3:
        value = int(input("Insert value to be checked in the BST : "))
        my_tree.is_member(value)
    elif option == 4:
        my_tree.print_in_order()
    elif option == 5:
        my_tree.print_pre_order()
    elif option == 6:
        my_tree.print_post_order()
    elif option == 7:
        my_tree.print_level_order()
    elif option == 8:
        my_tree.print_reverse_level_order()
    elif option == 9:
        print(f"The height of the binary tree is : {my_tree._get_height(my_tree)}")
    elif option == 10:
        print(f"The number of elements in the binary tree is : {my_tree._get_size(my_tree)}")
    elif option == 11:
        break
    else:
        print("Wrong option")
    print()
