



class RootNode:
    def __init__(self,root):
    
        self.head = root


class Node:
    def __init__(self,key,value):
        self.key = key
        self.data = value
        self.left = None
        self.right = None

class Bst:

    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head:
            return False
        else:
            return True
    def create(self,key,data):
        return Node(key,data)

    def insert(self, key,data, node = None):
        if self.is_empty():
            node = self.create(key,data)
            root = RootNode(node)
            self.head = root.head
        else:

            if key < node.key:
                if node.left == None:
                    node.left = self.create(key,data)
                else:
                    self.insert(key,data, node.left)
            elif key > node.key:
                if node.right == None:
                    node.right = self.create(key,data)
                else:
                    self.insert(key,data, node.right)
    def search(self,head):

        pass
    def print_tree(self):
        print("==============")
        self._print_tree(self.head, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            self._print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.data)
     
            self._print_tree(node.left, lvl+5)


def main():

    tree = Bst()
    tree.insert(50,'A')
    tree.insert( 15, 'B',tree.head)
    tree.insert(62, 'C', tree.head)
    tree.insert(5, 'D',tree.head)
    tree.insert(20, 'E', tree.head)
    tree.insert( 58, 'F',tree.head)
    tree.insert(91, 'G', tree.head)
    tree.insert(3, 'H',tree.head)
    tree.insert(8, 'I', tree.head)
    tree.insert( 37, 'J',tree.head)
    tree.insert(60, 'K', tree.head)
    tree.insert(24, 'L',tree.head)


    tree.print_tree()
    

    
    print('TEST')


if __name__ == "__main__":
    main()




