from random import random 



class SkipNode:
    def __init__(self,key, data,lvl = 0):
        self.key = key
        self.data = data
        self.lvl = lvl
        self.next = [None for i in range(lvl)]
    
    
    
    
    
    
    
    
class SkipList:
    def __init__(self, maxLevel):
        self.maxLevel = maxLevel
        self.head = SkipNode(None,None, maxLevel)


    def randomLevel(self,p = 0.5):
        lvl = 1
        while random() < p and lvl < self.maxLevel:
            lvl += 1
        return lvl
    def search_el(self, key, new = None):
        if new == None:
            new = [None]*len(self.head.next)
            h = self.head
            for i in reversed(range(len(self.head.next))):
                while h.next[i] != None and h.next[i].key < key:
                    h = h.next[i]
                new[i] = h
        if len(new) > 0:
            f_el = new[0].next[0]
            if f_el != None and f_el.key == key:
                return f_el
    def search(self,key):
        return self.search_el(key).data
    
    
    def insert(self,key,value):
        node = SkipNode(key,value,self.randomLevel())

        
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)
        new = [None]*len(self.head.next)
        h = self.head
        for i in reversed(range(len(self.head.next))):
            while h.next[i] != None and h.next[i].key < key:
                h = h.next[i]
            new[i] = h
        if self.search_el(key,new) == None:
            for i in range(len(node.next)):
                node.next[i] = new[i].next[i]
                new[i].next[i] = node
        elif self.search_el(key,new).key == key:
            self.search_el(key,new).data = value   
        
    def remove(self,key):
        new = [None] * len(self.head.next)
        h = self.head
        for i in reversed(range(len(self.head.next))):
            while h.next[i] != None and h.next[i].key < key:
                h = h.next[i]
            new[i] = h

        f_el = self.search_el(key,new)
        if f_el is not None:
            for i in range(len(f_el.next)):
                new[i].next[i] = f_el.next[i]
                
    

    

        



    def displayList_(self):
        node = self.head.next[0]  # pierwszy element na poziomie 0
        keys = []                           # lista kluczy na tym poziomie
        while(node != None):
            keys.append(node.key)
            node = node.next[0]

        for lvl in range(self.maxLevel-1, -1, -1):
            print("{}: ".format(lvl), end=" ")
            node = self.head.next[lvl]
            idx = 0
            while(node != None):                
                while node.key>keys[idx]:
                    print("  ", end=" ")
                    idx+=1
                idx+=1
                print("{:2d}".format(node.key), end=" ")     
                node = node.next[lvl]    
            print("")
    
    def __str__(self, new = None):   
        
       if new == None:
            new = [None]*len(self.head.next)
            h = self.head
            begin = '['
            while h.next[0] != None:
                h = h.next[0]
                key = h.key
                value = h.data
                if h.next[0]: 
                    begin += str(key) + ':' + str (value) + ', '
                else:
                    begin += str(key) + ':' + str (value)
            end = ']'
            return begin + end 

def main():

    skip_list = SkipList(4)
    string = 'ABCDEFGHIJKLMNO'
    for i in range(1,16):
        skip_list.insert(i,string[i - 1])
    
    skip_list.displayList_()
    print(skip_list.search(2))
    skip_list.insert(2,'Z')
    print(skip_list.search(2))
    skip_list.remove(5)
    skip_list.remove(6)
    skip_list.remove(7)
    print(skip_list)
    skip_list.insert(6,'W') 
    print(skip_list)
    
    skip_list2 = SkipList(4)
    for i in range(15,0,-1):
        
        skip_list2.insert(i,string[15-i])
    skip_list2.displayList_()
    print(skip_list2.search(2))
    skip_list2.insert(2,'Z')
    print(skip_list2.search(2))
    
    skip_list2.remove(5)
    skip_list2.remove(6)
    skip_list2.remove(7)
    print(skip_list2)
    print(skip_list2)

if __name__ == "__main__":
    main()
