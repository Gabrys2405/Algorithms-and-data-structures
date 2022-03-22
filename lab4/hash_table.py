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
            return input % self.size
        if isinstance(input, str):
            sum = 0
            for i in input:
               sum += ord(i)
            return sum % self.size 

    def rehash(self):
        pass
        
        


    def search(self, key):
        check = False
        for i in range(self.size):
            if self.tab[i]:
                if self.tab[i].key == key:
                    chech = True
                    return self.tab[i].value

                    
        if check == False:
            return None
        

    def insert(self,element):
        for i in range(self.size):
            if self.tab[i]:
                if self.tab[i].key == self.hash(element.key):
                    self.tab[i].value = element.value
            elif i == self.hash(element.key):
                self.tab[self.hash(element.key)] = element
                return 0
    def remove(self,key):
        for i in range(self.size):
            if self.tab[i]:
                if self.tab[i].key == self.hash(key):
                    self.tab[i] = None


def main():
    element = Element(1,75)
    table = HashTable(13)
    table.insert(element)
    print('COKOLWIEK')
    element1 = Element('1',115)
    table.insert(element1)
    print('COKOLWIEK')

    search = table.search(1)

    search2 = table.search(5)
    search3 = table.search('1')

    print('COKOLWIEK')
    table.remove(1)

    print('COKOLWIEK')




if __name__ == "__main__":
    main()

            



