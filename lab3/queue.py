#SKOŃCZONE 

class Queue:
    def __init__(self,size = 5,read = 0,write = 0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.read = read
        self.write = write

    def is_empty(self):
        if self.read == self.write:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.read]
        

    def dequeue(self):
        if self.is_empty():
            return None 
        else:
            read_data = self.read
            if self.read == len(self.tab) - 1:
                self.read = 0
            else:
                self.read = self.read + 1
            return self.tab[read_data]

    def realloc(self,tab,size):
        
        return [tab[i] if i<size else None  for i in range(2*size)]
    
    def enqueue(self,data):
        if self.tab[0] is None:
            self.tab[self.write] = data
            self.write = self.write + 1
        elif self.write == self.size - 1:
            self.tab[self.write] = data
            self.write = 0
        elif self.write == self.read and not self.tab[0] is None:
            
            self.tab = self.realloc(self.tab,self.size)
            
            
            old_size = self.size
            self.size = len(self.tab)
            
            new_tab = [None for i in range(self.size)]
            for i in range(self.read):
                new_tab[i] = self.tab[i]
            self.read = self.read + old_size
            for i in range(self.read ,self.size):
                new_tab[i] =  self.tab[i - old_size]
            self.tab = new_tab
            self.tab[self.write] = data
            self.write = self.write + 1
        else:
            self.tab[self.write] = data
            self.write = self.write + 1
        
        

    def queue_str(self):
        
        if self.is_empty():
            print('[]')
        else:
            print('[',end='')
            iter = self.read
            for i in range(self.size - 1):
                if self.tab[iter] is not None:
                    if iter == self.write - 1:
                        print(self.tab[iter],sep='',end='')
                    else:     
                        print(self.tab[iter],sep='',end=', ')
                if iter == self.size - 1:
                    iter = 0
                else:
                    iter+=1
            print(']')
    
    def tab_str(self):
        print(self.tab)



def main():

    queue = Queue() # Utworzenie pustej kolejki

    for i in range(1,5): # Wpisanie 4 danych do kolejki za pomocą enqueue()
        queue.enqueue(i)
    
    print('W kolejce 4 dane od 1 do 4')

    first_data = queue.dequeue() # Odczyt pierwszej danej z kolejki poprzez dequeue()
    print('Pierwsze wypisana dana:  {}'.format(first_data))

    second_data = queue.peek() # Odczyt drugiej wpisanej dalej z kolejki za pomocą peek()

    print('Druga wypisana dana:  {}'.format(second_data))
   
    print('Aktualny stan kolejki: ')
    queue.queue_str() # Tekstowe wypisanie aktualnego stanu kolejki
    
     # Wpisanie 4 danych do kolejki za pomocą enqueue()
    for i in range(5,9): # Wpisanie 4 danych do kolejki za pomocą enqueue()
        queue.enqueue(i)



    print('\nAktualny stan tablicy:  ')
    queue.tab_str()
    
    while not queue.is_empty(): #Opróżnianie kolejki z wypisaniem usuwanych danych
        element = queue.dequeue()
        print(element)

    queue.queue_str() # Wypisanie pustej kolejki


if __name__ == "__main__":
    main()