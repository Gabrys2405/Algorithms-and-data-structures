



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
            if node is None:
                node = self.head
            
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
                
    def search(self,key,node = None):
        
        if node == None:
            node = self.head 
        
        if key == node.key:
            return node.data
        if key < node.key:
            if node.left == None:
                return None
            return self.search(key,node.left)
        if node.right == None:
            return False
        return self.search(key,node.right)

    def delete(self,key,node = None):
        if node == None:
            node = self.head
        if node == None:
            return node 
        if key < node.key:
            node.left = self.delete(key,node.left)
            return node
        if key > node.key:
            node.right = self.delete(key,node.right)
            return node
        if node.right == None:
            return node.left
        if node.left == None:
            return node.right
        min_node = node.right
        while min_node.left:
            min_node = min_node.left
        node.data = min_node
        node.right = self.delete(min_node.data,node.right)
        return node
        
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
    tree.insert( 15, 'B')
    tree.insert(62, 'C')
    tree.insert(5, 'D')
    tree.insert(20, 'E')
    tree.insert( 58, 'F')
    tree.insert(91, 'G')
    tree.insert(3, 'H')
    tree.insert(8, 'I')
    tree.insert( 37, 'J')
    tree.insert(60, 'K')
    tree.insert(24, 'L')


    tree.print_tree()
    

    print(tree.search(60))
    tree.delete(91)

    tree.print_tree()
    print('TEST')


if __name__ == "__main__":
    main()




