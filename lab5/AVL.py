


class RootNode:
    def __init__(self,root):
    
        self.head = root
        self.heigh = 1


class Node:
    def __init__(self,key,value):
        self.key = key
        self.data = value
        self.left = None
        self.right = None
        self.heigh = 0

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


class AVL(Bst):
    

    def gHeight(self,head):
        if not head:
            return 0
        return head.heigh
    def gBalance(self,head):
        if not head:
            return 0
        if not head.left:
            return self.gHeight(head.right) + 1
        elif not head.right:
            return self.gHeight(head.left) + 1
        else:
            return (self.gHeight(head.right) + 1) - (self.gHeight(head.left) + 1)
    def lRotate(self,node):
        if node.left:   
            l = node.left
            bufer = l.left
            l.right = node 
            node = l
            
             


            
            l.heigh = 1 + max(self.gHeight(l.left),self.gHeight(l.right))
            return l


    
    def rRotate(self,node):
        if node.right:    
            r = node.right
            buffer = r.right
            r.right = node
            node.left = buffer

            node.heigh = 1 + max(self.gHeight(node.left),self.gHeight(node.right))
            r.heigh = 1 + max(self.gHeight(r.left),self.gHeight(r.right))

            return r
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
    
        node.heigh = 1 + max(self.gHeight(node.left), self.gHeight(node.right))
        
        balance = self.gBalance(node)
        
        if balance > 1:
            if key < node.left.key:
                node = self.lRotate(node)
                
            
        if balance < -1:
            if key > node.right.key:
                return self.rRotate(node)
           

        return node
    

def main():

    tree = AVL()
    tree.insert(50,'A')
    tree.insert( 15, 'B')
    tree.insert(62, 'C')
    tree.insert(5, 'D')
    tree.insert(2, 'E')
    tree.insert( 1, 'F')
    tree.insert(11, 'G')
    tree.insert(100, 'H')
    tree.insert(7, 'I')
    tree.insert( 6, 'J')
    tree.insert(55, 'K')
    tree.insert(52, 'L')

    tree.insert( 51, 'M')
    tree.insert(57, 'N')
    tree.insert(8, 'O')
    tree.insert(9, 'P')
    tree.insert( 10, 'R')
    tree.insert(99, 'S')
    tree.insert(12, 'T')


    tree.print_tree()
    tree.print_list()
    
    print(tree.search(10))
    
   

    

if __name__ == "__main__":
    main()