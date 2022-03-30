



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
            elif key == node.key:
                node.data = data
                
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
            if node.left:
                node.left = self.delete(key,node.left)
            return node
        if key > node.key:
            if node.right:
                node.right = self.delete(key,node.right)
            return node
        if node.right == None:
            return node.left
        if node.left == None:
            return node.right
        min_node = node.right
        while min_node.left:
            min_node = min_node.left
        node.key = min_node.key
        node.data = min_node.data
        node.right = self.delete(node.key,node.right)
    
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
    def inorder(self,list ,node = None):
        
        if node == None:
            node = self.head
        if node.left != None:
            self.inorder(list,node.left)
        if node != None:
            key = str(node.key)
            data = str(node.data)
            list.append((key + ':' + data))
        if node.right != None:
            self.inorder(list,node.right)
        return list

    def print_list(self):
        list = []
        print('[%s]'%', '.join(map(str,self.inorder(list))))
    def height(self,node = 1):
        if node == 1:
            node = self.head 

        if node == None:
            return 0
        else:
            return 1 + max(self.height(node.left),self.height(node.right))

    # def swap(self,key,data,node = None):
    #     if node == None:
    #         node = self.head 
        
    #     if key == node.key:
    #         node.data = data
            
    #     if key < node.key:
    #         if node.left == None:
    #             return None
    #         return self.swap(key,data,node.left)
    #     if node.right == None:
    #         return False
    #     return self.swap(key,data,node.right)

    


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
    tree.print_list()
    
    print(tree.search(24))
    
    tree.insert(20,'AA')
    tree.insert(6,'M')
    tree.delete(62)

    
    tree.insert(59,'N')
    tree.insert(100,'P')
    tree.delete(8)
    tree.delete(15)
    tree.insert(55,'R')
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    tree.print_list()
    tree.print_tree()

    

if __name__ == "__main__":
    main()




