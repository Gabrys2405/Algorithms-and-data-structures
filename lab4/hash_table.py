

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

    def rehash(self,input,failure):
        if isinstance(input, int):
            result = (self.hash(input) + self.c1 * failure + self.c2 * failure ** 2) % self.size 
        else:
            sum = 0
            for i in input:
               sum += ord(i)
            result =  (self.hash(sum) + self.c1 * failure + self.c2 * failure ** 2) % self.size 
        
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
        failure = 0
        hash_key = self.hash(key)
        result = self.tab[hash_key]
        failure += 1
        if result and result.key == key:
            return result.value
        else:
            hash_key = self.rehash(hash_key,failure)
            failure += 1
            result = self.tab[hash_key]
            while result.key != key:

                if failure == self.size:
                    print ('Brak danej')
                    return None
                else:

                    hash_key = self.rehash(hash_key,failure)
                    result = self.tab[hash_key]
                    failure += 1
            return result.value

    def insert(self,element):
        # check = False
        
        # for i in range(self.size):
        #     if self.tab[i]:
        #         if self.tab[i].key == element.key:
        #             self.tab[i].value = element.value
        #             check = True 
        # if check == False:


        #     hash_key = element.key
        #     failure = 0
            
        #     if self.tab[self.hash(element.key)] == None:
        #         hash_key = self.hash(element.key)
        #         failure  += 1 
        #     elif self.tab[self.rehash(element.key,failure)] == None:
        #         hash_key = self.rehash(element.key,failure)
        #         failure += 1
        #     else:
        #         failure += 1
        #         hash_key = self.rehash(hash_key,failure)
        #         failure += 1
        #         while self.tab[hash_key]:
        #             if iter == self.size:
        #                 # print('Brak miejsca')
        #                 return None
        #             else:    
        #                 hash_key = self.rehash(hash_key,failure)
        #                 failure += 1
                    

        #     for i in range(self.size):
        #         if hash_key == i:
        #             self.tab[i] = element
        failures = 0
        hash_key = self.hash(element.key)
        failures += 1
        if self.tab[hash_key] == None:
            self.tab[hash_key] = element
        else:
            while self.tab[hash_key]:
                if failures == self.size:
                    print('Brak miejsca')
                    return None
                if element.key  == self.tab[hash_key].key:
                    self.tab[hash_key].value = element.value
                    break
                else:
                    hash_key = self.rehash(element.key,failures)
                    failures += 1
            self.tab[hash_key] = element

            
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
        
        
        hash_key = self.hash(key)
        result = self.tab[hash_key]
        if self.tab[hash_key]:
            if self.tab[hash_key].key == key:
                self.tab[hash_key] = None
            
        else:
            hash_key = self.rehash(hash_key)
            result = self.tab[hash_key]
            while result.key != key:

                hash_key = self.rehash(hash_key)
                result = self.tab[hash_key]
            self.tab[hash_key] == None        
            




def main():
    

    def test_function(size,c1 = 1,c2 = 0):
        table = HashTable(size,c1,c2)
        number = 13
        string = 'ABCDEFGHIJKLMNO'
        for i in range(1,len(string) + 1):
            if i == 6:
                table.insert(Element(18,string[i - 1]))
            elif i == 7:
                table.insert(Element(31,string[i - 1]))
            else: 
                table.insert(Element(i,string[i - 1]))
        
        return table
    tab = test_function(13)

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

    def test_function2(size,c1,c2):
        table = HashTable(size,c1,c2)
        number = 13
        string = 'ABCDEFGHIJKLMNO'
        for i in range(1,len(string) + 1):
            table.insert(Element(13 * i,string[i - 1]))
        print(table)


    test_function2(13,1,0)
    test_function2(13,0,1)
    print(test_function(13,0,1))


if __name__ == "__main__":
    main()

            



