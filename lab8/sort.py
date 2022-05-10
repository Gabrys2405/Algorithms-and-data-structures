import random
import time

class Element:
    def __init__(self, priority, data):
        self.priority = priority
        self.data = data

    def __gt__(self,other):
        return self.priority > other.priority
    def __lt__(self,other):
        return self.priority < other.priority
    def __le__(self,other):
        return self.priority <= other.priority
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
        if self.tab_size: return False
        else: return True
    def heapify(self):
        size = self.tab_size
        for i in range(self.parent(self.tab_size-1),-1,-1):
            self.repair(size,i)
        self.size = self.tab_size
        

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
    
        while self.size:
            result = self.tab[0]
            self.tab[0] = self.tab[self.size - 1]
            self.tab[self.size - 1] = result
            self.size -= 1
            r_in = self.right(0)
            l_in = self.left(0)
            if r_in != self.size and l_in != self.size:
                self.repair(self.size)
            

    def repair(self,size,index = 0):
        buffer = self.tab[index]
        r_in = self.right(index)
        l_in = self.left(index)
        if r_in < size and l_in < size:
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
                if l_in > size or r_in >= size:
                    break
        # else:
        #     while (self.tab[l_in] > buffer):
        #         self.tab[self.parent(l_in)] = self.tab[l_in]
        #         self.tab[l_in] = buffer
        #         buffer = self.tab[l_in]
        #         r_in = self.right(l_in)
        #         l_in = self.left(l_in)



    def right(self, indeks):
        result = (indeks * 2) + 2
        return result  

    def left(self, indeks):
        result = (indeks * 2) + 1
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
            for i in range(self.tab_size-1):
                print(self.tab[i], end = ', ')
            if self.tab[self.tab_size-1]: print(self.tab[self.tab_size-1] , end = ' ')
            print( '}')

    
    def print_tree(self, idx, lvl):
        if idx<self.tab_size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)
    def swap(self):
        for i in range(self.tab_size):
            min = i 
            for j in range(i, self.tab_size):
                if self.tab[j] < self.tab[min]:
                    
                    min = j
            self.tab[i],self.tab[min] = self.tab[min],self.tab[i]
            
    def shift(self):
        for j in range(self.tab_size):
            for i in range(j,self.tab_size): 
                if self.tab[j] > self.tab[i] :
                    self.tab.insert(j,self.tab.pop(i))
                    

                
def main():


    prio = PrioQueue([Element(pr,dat)for pr, dat in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]])
    prio.heapify()
    prio.print_tree(0,0)
    prio.print_tab()
    prio.dequeue()
    prio.print_tab()
    tab = [int(random.random()*100)for x in range(10000)]
    prio2 = PrioQueue(tab)
    t_start = time.perf_counter()
    prio2.heapify()
    prio2.dequeue()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))


    prio3 = PrioQueue([Element(pr,dat)for pr, dat in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]])

    prio3.swap()
    prio3.print_tab()

    prio4 = PrioQueue([Element(pr,dat)for pr, dat in [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]])
    prio4.shift()
    prio4.print_tab()

    prio5 = PrioQueue(tab)
    
    t_start = time.perf_counter()
    prio5.shift()
    t_stop = time.perf_counter()
    print("Czas obliczeń dla shift:", "{:.7f}".format(t_stop - t_start))
    tab2 = [int(random.random()*100)for x in range(10000)]
    prio6 = PrioQueue(tab2)
    t_start = time.perf_counter()
    prio6.swap()
    t_stop = time.perf_counter()
    print("Czas obliczeń dla swap:", "{:.7f}".format(t_stop - t_start))




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

    





    

