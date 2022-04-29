class Element:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

    def __gt__(self,other):
        return self.priority > other.priority
    def __lt__(self,other):
        return self.priority < other.priority
    def __str__(self):
        priority = str(self.priority)
        data = str(self.data)
        return priority + ":" + data


class PrioQueue:
    def __init__(self,tab = None):
        self.tab = tab
        self.tab_size = len(self.tab)
        self.size = 0
    def is_empty(self):
        if self.size: return False
        else: return True
    def heapify(self):
        for i in range(self.tab_size):
            self.repair(i)
    def enqueue(self,priority,data):
        element = Element(priority,data)
        if self.is_empty():
            self.tab.append(element)
            self.size += 1
        else:
            self.tab.append(element)
            self.size += 1
            new_elem_in = self.size - 1
            parent_in = self.parent(new_elem_in)
            
            while self.tab[new_elem_in] > self.tab[parent_in]:
                buffer = self.tab[parent_in]
                self.tab[parent_in] = element
                self.tab[new_elem_in] = buffer
                new_elem_in = parent_in
                if self.parent(new_elem_in) > 0:
                    parent_in = self.parent(new_elem_in) 
                
    def dequeue(self):
        if self.is_empty():
            return None
        elif self.size == 1:
            
            buf = self.tab[0]
            self.tab = []
            self.size -= 1
            return buf.data
        else:
            result = self.tab[0]
            self.tab[0] = self.tab[self.size - 1]
            self.tab[self.size - 1] = 0
            self.size -= 1
            r_in = self.right(0)
            l_in = self.left(0)
            if r_in != self.size and l_in != self.size:
                self.repair(0)
            return result.data

    def repair(self,index):
        buffer = self.tab[index]
        r_in = self.right(index)
        l_in = self.left(index)
        while (self.tab[r_in] > buffer or self.tab[l_in] > buffer):
            if self.tab[r_in] > self.tab[l_in]:
                self.tab[self.parent(r_in)] = self.tab[r_in]
                self.tab[r_in] = buffer
                buffer = self.tab[r_in]
                l_in = self.left(r_in)
                r_in = self.right(r_in)
            else:
                self.tab[self.parent(l_in)] = self.tab[l_in]
                self.tab[l_in] = buffer
                buffer = self.tab[l_in]
                r_in = self.right(l_in)
                l_in = self.left(l_in)
            if l_in > self.size or r_in >= self.size:
                break


    def right(self, indeks):
        result = (indeks * 2) + 2
        if result < self.tab_size:
        
            return result  

    def left(self, indeks):
        result = (indeks * 2) + 1
        if result < self.tab_size:
        
            return result 
    def parent(self, indeks):
        return ( indeks - 1) // 2
    def peek(self):
        return self.tab[0].data
    def print_tab(self):
        if self.is_empty():
            print('{}')
        else:
            print ('{', end=' ')
            for i in range(self.size-1):
                print(self.tab[i], end = ', ')
            if self.tab[self.size-1]: print(self.tab[self.size-1] , end = ' ')
            print( '}')

    
    def print_tree(self, idx, lvl):
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)





def main():


    prio = PrioQueue([Element(pr,dat)for pr, dat in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]])
    
    prio.heapify()
    
    prio.print_tree(0,0)
    prio.print_tab()
    
    
  
    print(prio.peek())
    prio.print_tab()
    element = 1
    while element:
        element = prio.dequeue()
        if element:
            print(element)
    prio.print_tab()
    print('TEST')



    # prio = PrioQueue()
   
    # tab = [4,7,6,7,5,2,2,1]
    # string = 'ALGORYTM'
    # for i in range(len(tab)):
    #     prio.enqueue(tab[i], string[i])

    # prio.print_tree(0,0)
    # prio.print_tab()
    
    # print(prio.dequeue())
  
    # print(prio.peek())
    # prio.print_tab()
    # element = 1
    # while element:
    #     element = prio.dequeue()
    #     if element:
    #         print(element)
    # prio.print_tab()

if __name__ == "__main__":
    main()

    





    

