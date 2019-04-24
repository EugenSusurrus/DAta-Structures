"""
Adelsin - Velsky and Landis AVL tree is an improved version of the Binary Search Tree BST with a built-in self-balancing
feature.

Balancing is performed after certain insertion and deletion operations (those which cause the tree to be 'unbalanced')

    * For a node to be balanced, the heights of left and right childrn must differ by <= 1.

    * Height_n = 1 + max(Height_n_left, Height_n_right)

"""

class Node:
    def __init__(self, dat=None):
        self.dat = dat
        self.left = None
        self.right = None
        self.parent = None      # Pointer to parent node in tree
        self.height = 1


class AVL_Tree:
    def __init__(self):
        self.root = None


    def __repr__(self):
        if self.root == None:
            return ''
        content = '\n'
        cur_nodes = [self.root]
        cur_height = self.root.height
        sep = ' ' * (2 ** (cur_height-1))
        while True:
            cur_height -= 1
            if len(cur_nodes) == 0:
                break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n is None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.dat is not None:
                    buf = ' ' * int((5 - len(str(n.dat))) / 2)
                    cur_row += '%s%s%s' % (buf, str(n.dat), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left is not None:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right is not None:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * int(len(sep) / 2)
        return content


    def insert(self, dat):
        if self.root is None:
            self.root = Node(dat)

        else:
            self._insert(dat, self.root)


    def _insert(self, dat, cur_node):
        if dat < cur_node.dat:
            if cur_node.left is None:
                cur_node.left = Node(dat)
                cur_node.left.parent = cur_node
                self._inspect_insertion(cur_node.left)
            else:
                self._insert(dat, cur_node.left)
        elif dat > cur_node.dat:
            if cur_node.right is None:
                cur_node.right = Node(dat)
                cur_node.right.parent = cur_node
                self._inspect_insertion(cur_node.right)
            else:
                self._insert(dat, cur_node.right)

        else:
            print("Value already in tree")


    def print_tree(self):
        pass

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print('%s, h=%d' % (str(cur_node.dat), cur_node.height))
            self._print_tree(cur_node.right)


    def get_height(self):
        if self.root is not None:
            return self._get_height(self.root, 0)
        else:
            return 0


    def _get_height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._get_height(cur_node.left, cur_height + 1)
        right_height = self._get_height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)


    def is_member(self, dat):
        if self.root is not None:
            return self._is_member(dat, self.root)
        else:
            return False


    def _is_member(self, dat, cur_node):
        if dat == cur_node.dat:
            return True
        elif dat < cur_node.dat and cur_node.left is not None:
            return self._is_member(dat, cur_node.left)
        elif dat > cur_node.dat and cur_node.right is not None:
            return self.is_member(dat, cur_node.right)
        else:
            return False


    def find(self, dat):
        if self.root is not None:
            return self._find(dat, self.root)
        else:
            return None


    def _find(self, dat, cur_node):
        if dat == cur_node.dat:
            return cur_node
        elif dat < cur_node.dat and cur_node.left is not None:
            return self._find(dat, cur_node.left)
        elif dat > cur_node.dat and cur_node.right is not None:
            return self._find(dat, cur_node.right)


    def delete_val(self, dat):
        return self.delete_node(self.find(dat))


    def delete_node(self, node):
        # protect against deleting a node not found in the tree
        if node is None or self.find(node.dat) is None:
            print("Tree does not contain node to be deleted")
            return None

        # returns the node with min value in tree rooted at input node
        def min_value_node(n):
            current = n
            while current.left is not None:
                current = current.left
            return current

        # returns the number of children for the specified node
        def num_children(n):
            num_children = 0
            if n.left is not None:
                num_children += 1
            if n.right is not None:
                num_children +=1
            return num_children

        # get the parent of the node to be deleted
        node_parent = node.parent

        # get the number of children of the node to e deleted
        node_children = num_children(node)

        # break operation into different cases based on the structure of the tree and node to be deleted

        # CASE 1 (node has no children)
        if node_children == 0:
            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        # CASE 2 (node has a single child)
        if node_children == 1:
            if node.left is not None:
                child = node.left
            else:
                child = node.right

            if node_parent is not None:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child

            # Correct the parent pointer in node
            child.parent = node_parent

        # CASE 3 (node has two children)
        if node_children == 2:
            # get the inorder successor of the deleted node
            successor = min_value_node(node.right)

            # copy the inorder successors value to the node formerly holding the value we wished to delete
            node.dat = successor.dat

            # delete the inorder successor
            self.delete_node(successor)

            return

        if node_parent is not None:
            node_parent.height = 1 + max(self.get_height(node_parent.left),
                                         self.get_height(node_parent.right))

            self._inspect_deletion(node_parent)


    # AVL tree specific functions

    def _inspect_insertion(self, cur_node, path=[]):
        if cur_node.parent is None:
            return

        path = [cur_node] + path

        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)

        if abs(left_height - right_height) > 1:
            path = [cur_node.parent] + path
            self._rebalance_node(path[0], path[1], path[2])
            return

        new_hight = 1 + cur_node.height
        if new_hight > cur_node.parent.height:
            cur_node.parent.height = new_hight

        self._inspect_insertion(cur_node.parent, path)


    def _inspect_deletion(self, cur_node):
        if cur_node is None:
            return

        left_height = self.get_height(cur_node.left)
        right_height = self.get_height(cur_node.right)

        if abs(left_height - right_height) > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self._rebalance_node(cur_node, y, x)

        self._inspect_deletion(cur_node.parent)


    def _rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self._right_rotate(z)
        elif y == z.left and x == y.right:
            self._left_rotate(y)
            self._right_rotate(z)
        elif y == z.right and x == y.right:
            self._left_rotate(z)
        elif y == z.right and x == y.left:
            self._right_rotate(y)
            self._left_rotate(z)
        else:
            raise Exception('z, y, x node configuration not recognized!')


    def _right_rotate(self, z):
        sub_root = z.parent
        y = z.left
        t3 = y.right
        y.right = z
        z.parent = y
        z.left = t3
        if t3 is not None:
            t3.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))


    def _left_rotate(self, z):
        sub_root = z.parent
        y = z.right
        t2 = y.left
        y.left = z
        z.parent = y
        z.right = t2

        if t2 is not None:
            t2.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))


    def get_height(self, cur_node):
        if cur_node is None:
            return 0
        return cur_node.height


    def taller_child(self, cur_node):
        left = self.get_height(cur_node.left)
        right = self.get_height(cur_node.righ)
        return cur_node.left if left >= right else cur_node.right


########################################################################################################################

avl_tree = AVL_Tree()

while True:
    print("1.Display AVL tree")
    print("2.Insert element in AVL tree")
    print("3.Delete an element from the AVL tree")
    print("4.Get height of the AVL tree")
    print("5.Check if AVL tree contains element")
    print("6.Quit")

    option = int(input("Please choose an option >>> "))

    if option == 1:
        print(avl_tree)
    elif option == 2:
        elem = int(input("Input the element to be inserted in the AVL tree >>> "))
        avl_tree.insert(elem)
        print(avl_tree)
    elif option == 3:
        elem = int(input("Select an element to be deleted from the AVL tree >>> "))
        avl_tree.delete_val(elem)
        print(avl_tree)
    elif option == 4:
        print(f"Height of the AVL tree is {avl_tree.get_height()}")
    elif option == 5:
        elem = int(input("Insert the element to be searched in the tree"))
        if avl_tree.is_member(elem):
            print(f"{elem} is found in th AVL tree")
        else:
            print(f"{elem} not found in the AVL tree")
    elif option == 6:
        break
    else:
        print("Option does not exist")
        print()
