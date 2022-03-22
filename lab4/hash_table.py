from pyrsistent import v


class Element:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value



class HashTable:
    
    
    def __init__(self, size, c1 = 1, c2 = 0):
        
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2
    
    
    def hash(self, input):
        
        if isinstance(input, int):
            return (input % self.size)
        if isinstance(input, str):
            sum = 0
            for i in input:
               sum += ord(i)
            return (sum % self.size) 

    def rehash(self,input):
        if isinstance(input, int):
            result = (self.hash(input) + self.c1 * input + self.c2 * input ** 2) % self.size 
        else:
            sum = 0
            for i in input:
               sum += ord(i)
            result =  (self.hash(sum) + self.c1 * sum + self.c2 * sum ** 2) % self.size 
        
        return int(result)
 
        
        


    def search(self, key):
        # check = False
        # for i in range(self.size):
        #     if self.tab[i]:
        #         if self.tab[i].key == key:
        #             chech = True
        #             return self.tab[i].value

                    
        # if check == False:
        #     print('Brak danej')
        #     return None
        iter = 0
        hash_key = self.hash(key)
        result = self.tab[hash_key]
        if result and result.key == key:
            return result.value
        else:
            hash_key = self.rehash(hash_key)
            result = self.tab[hash_key]
            while result.key != key:

                if iter == self.size:
                    print ('Brak danej')
                    return None
                else:

                    hash_key = self.rehash(hash_key)
                    result = self.tab[hash_key]
                    iter += 1
            return result.value

    def insert(self,element):
        check = False
        
        for i in range(self.size):
            if self.tab[i]:
                if self.tab[i].key == element.key:
                    self.tab[i].value = element.value
                    check = True 
        if check == False:


            hash_key = element.key
            iter = 0
            
            if self.tab[self.hash(element.key)] == None:
                hash_key = self.hash(element.key) 
            elif self.tab[self.rehash(element.key)] == None:
                hash_key = self.rehash(element.key)
            
            else:
                hash_key = self.rehash(hash_key)
                while self.tab[hash_key]:
                    if iter == self.size:
                        print('Brak miejsca')
                        return None
                    else:    
                        hash_key = self.rehash(hash_key)
                        iter += 1
                    

            for i in range(self.size):
                if hash_key == i:
                    self.tab[i] = element
            
    def __str__(self):
        begin = str('{')
        end = str('}') 
        for i in range(self.size):
            if self.tab[i]:
                begin += (str(self.tab[i].key) + ": '" + str(self.tab[i].value)) + "'"
                if (i != self.size - 1):
                    begin+= ", "
            else:
                begin += str(None)
                if (i != self.size - 1):
                    begin+= ", "
        
        return begin + end 
                

        
                
       
    def remove(self,key):
        # for i in range(self.size):
        #     if self.tab[i]:
        #         if self.tab[i].key == self.hash(key):
        #             self.tab[i] = None

        


def main():
    print(10 % 13)


    element1 = Element(1,'A')
    element2 = Element(2,'B')
    element3 = Element(3,'C')
    element4 = Element(4,'D')
    element5 = Element(5,'E')
    element6 = Element(18,'F')
    element7 = Element(31,'G')
    element8 = Element(8,'H')
    element9 = Element(9,'I')
    element10 = Element(10,'J')
    element11 = Element(11,'K')
    element12 = Element(12,'L')
    element13 = Element(13,'M')
    element14 = Element(14,'N')
    element15 = Element(15,'O')

    tab = HashTable(13)
    tab.insert(element1)
    tab.insert(element2)
    tab.insert(element3)
    tab.insert(element4)
    tab.insert(element5)
    tab.insert(element6)
    tab.insert(element7)
    tab.insert(element8)
    tab.insert(element9)
    tab.insert(element10)
    tab.insert(element11)
    tab.insert(element12)
    tab.insert(element13)
    tab.insert(element14)
    tab.insert(element15)

    print(tab)
    print(tab.search(5))
    print(tab.search(14))
    tab.insert(Element(5,'Z'))
    print(tab.search(5))
    tab.remove(5)
    print(tab)
    print(tab.search(31))



    tab.insert(Element('W','test'))
    print(tab)

    def test_function(size,c1,c2):
        table = HashTable(size,c1,c2)
        number = 13
        string = 'ABCDEFGHIJKLMNO'
        for i in range(len(string)):
            table.insert(Element(13 * (i+1),string[i]))
        print(table)


    test_function(13,1,0)
    test_function(13,0,0.75)



if __name__ == "__main__":
    main()

            



