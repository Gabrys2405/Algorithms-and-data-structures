
SIZE = 6


class Node:
    def __init__(self):
        self.tab = [None for i in range(SIZE)]
        self.next = None
        self.length = 0

    def add(self,index,data):
        if self.length == 0:
            self.tab[index % SIZE] = data
        elif self.tab[index % SIZE] and self.length != SIZE:
            self.tab[(index % SIZE) + 1 : SIZE] = self.tab[(index % SIZE) : SIZE - 1]
            self.tab[index % SIZE] = data

        else:
            self.tab[index % SIZE] = data
    def remove(self,index):
        if self.length != 0:
            if self.tab[index % SIZE]:
                self.tab[index % SIZE] = None
        
                self.tab[(index % SIZE) : SIZE - 1] = self.tab[(index % SIZE) + 1 : SIZE]



class UnrolledList:

    def __init__(self):
        self.head = None
    
    def get(self,index):
        if self.head == None:
            return None
        else:
            node = self.head
            elem_index = index // SIZE
            node_old = node
            i = 0
            while i != elem_index:
                i += 1
                node = node.next
            

            return node.tab[index % SIZE]




    def insert(self,index,data):
       
        if self.head == None:
            node = Node()
            node.next = None
            self.head = node
            # node.tab[index] = data
            node.add(index,data)
            node.length += 1
        else:

            node = self.head
            elem_index = index // SIZE
            node_old = node
            i = 0
            while i != elem_index:
                i += 1
                node = node.next
            if node:
                if node.length != SIZE:
                    node.add(index % SIZE, data)
                    node.length += 1
                else:
                    

                    if node.next and node.next.length != SIZE:
                        for i in range(SIZE//2,SIZE):
                            node.next.add(i - SIZE//2,node.tab[i])
                            node.tab[i] = None
                        node.length -= 3
                        node.next.length +=3
                        if index % SIZE < SIZE//2:
                            node.add(index % SIZE,data)
                            node.length += 1
                        else:
                            node.next.add(index % SIZE,data)
                            node.next.length += 1
                    else:
                        node_new = Node()
                        node_new.next = None
                        node_old.next = node
                        node.next = node_new
                        
                        for i in range(SIZE//2,SIZE):
                            node.next.add(i - SIZE//2,node.tab[i])
                            node.tab[i] = None
                        node.length -= 3
                        node.next.length +=3
                        if index % (SIZE - 1) < SIZE//2:
                            node.add(index % SIZE,data)
                            node.length += 1
                        else:
                            node.next.add(index % SIZE,data)
                            node.next.length += 1

            else:
                node_new = Node()
                node_new.next = None
                node_old.next = node_new
                
                node_new.add(index % SIZE,data)
                node_new.length += 1
   
           
            # while node:
            #     if node.length != SIZE:
            #         node.add(index,data)
            #         node.length += 1
            #     else:
            #         if node.next is None:
            #             new_node = Node()
            #             new_node.next = None
            #             node.next= new_node
            #             for i in range(int(SIZE/2),SIZE):
            #                 new_node.tab[i-int(SIZE/2)] = node.tab[i]
            #                 node.tab[i] = None
                
            #         if index < int(SIZE/2):
            #             node.add(index,data)
            #             node.length += 1
            #         else:
            #             node.next.add(index,data)
            #             node.next.length += 1
            #     node = node.next
       
    def delete(self,index):
        
        if self.head == None:
            return None
        else:
            node = self.head
            elem_index = index // SIZE
            node_old = node
            i = 0
            while i != elem_index:
                i += 1
                node = node.next
            node.remove(index % SIZE)
            node.length -= 1
            if node.length < SIZE // 2:
                if node.next:
                    element = node.next.tab[0]
                    for i in range(SIZE):
                        if node.tab[i] == None:
                            index = i
                            break
                    node.add(index,element)
                    node.next.remove(0)
                    node.next.length -= 1
                    if node.next.length < SIZE // 2:
                        for i in range(node.next.length):
                            node.add(index + 1,node.next.tab[i])
                            node.length += 1
                        node.next = node.next.next


    def print_list(self):
        node = self.head
        i = 0
        while node.next:
            i += 1
            node = node.next
        print('[',end = '',sep = '')
        for j in range(i * SIZE):
            if j == (i * SIZE) - 1:
                print(self.get(j),end = '',sep = '')
            else:

                print(self.get(j),', ',end = '',sep = '')
             
        print(']',sep='')   
       
        # iter = 0
        # if self.head == None:
        #     node = Node()
        #     node.next = None
        #     self.head = node
        #     node.tab[index] = data
        #     node.length += 1
        # else:
        #     node = self.head
            
        #     while node:
        #         if node.length != SIZE and node.next == None:

        #             node.add(index,data)
        #             node.length += 1
        #             node = node.next
        #         elif node.next == None:
        #             new_node = Node()
        #             new_node.next = None
        #             node.next = new_node
        #         else:

        #             if index < SIZE:
                
        #                 for i in range(int(SIZE/2),SIZE):
        #                     node.next.tab[i - int(SIZE/2)] = node.tab[i]
        #                     node.tab[i] = None
                        
        #                 if index < int(SIZE/2):
        #                     node.add(index,data)
        #                     new_node.length = int(SIZE/2)
                            
        #                 else:
        #                     new_node.add(index,data)
        #                     new_node.length += (int(SIZE/2) + 1)
        #                 node.length = int(SIZE/2)
        #             node = new_node.next
                    
                    




list = UnrolledList()
for i in range(1,10):
    list.insert(i - 1,i)

print(list.get(3))
list.insert(1,10)
list.insert(8,11)
list.print_list()
list.delete(1)
list.delete(2)

list.print_list()


# list.insert(0,55)
# print('COKOLWIEK')
# list.insert(1,56)
# list.insert(2,57)
# list.insert(3,58)
# list.insert(4,59)
# print('CKOLOWIEK2')
# list.insert(5,60)
# list.insert(6,61)
# print('COKOLWIEK3')
# list.insert(4,62)
# list.insert(5,63)
# print('COKOLWIEK')

# list.insert(6,64)
# print('COKOLWIEK')




