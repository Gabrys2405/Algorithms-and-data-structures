
SIZE = 6


class Node:
    def __init__(self):
        self.tab = [None for i in range(SIZE)]
        self.next = None
        self.length = 0

    def add(self,index,data):
        if self.length == 0:
            self.tab[index] = data
        elif self.tab[index]:
            old_data = self.tab[index]
            self.tab[index] = data
            self.tab[index + 1] = old_data
        else:
            self.tab[index] = data
    def remove(self,index):
        if self.length != 0:
            if self.tab[index]:
                self.tab[index] = None
        for i in range(index + 1,SIZE):
            self.tab[i - 1] = self.tab[i]



class UnrolledList:

    def __init__(self):
        self.head = None
    
    def get(self,index):
        pass



    def insert(self,index,data):
        iter = 0
        if self.head == None:
            node = Node()
            node.next = None
            self.head = node
            node.tab[index] = data
            node.length += 1
        else:
            node = self.head
            
            while node:
                if node.length != SIZE:
                    node.add(index,data)
                    node.length += 1
                    node = node.next
                else:
                    new_node = Node()
                    new_node.next = None
                    node.next = new_node
                    if index < SIZE:
                        for i in range(int(SIZE/2),SIZE):
                            node.next.tab[i - int(SIZE/2)] = node.tab[i]
                            node.tab[i] = None
                        node.add(index,data)
                        new_node.length = int(SIZE/2)
                        node.length = int(SIZE/2) + 1
                    node = new_node.next
                    
                    




list = UnrolledList()
list.insert(0,55)
print('COKOLWIEK')
list.insert(1,56)
list.insert(2,57)
list.insert(3,58)
list.insert(4,59)
print('CKOLOWIEK2')
list.insert(5,60)
list.insert(3,61)
print('COKOLWIEK3')
list.insert(4,65)
list.insert(5,67)
print('COKOLWIEK')
        




