#SKOŃCZONE

from typing import List


class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def destroy(self):
            self.head = None
   
    def add(self,node):
            node = Node(node)
            node.next = self.head
            self.head = node
             
    def is_empty(self):
        return self.head == None
    
    def remove(self):
        node = self.head
        if not (self.is_empty()):
            self.head = node.next
    
    def length(self):
        length = 0
        
        node = self.head
    
        while(node != None):
            length +=1
            node = node.next

        return length

    def get(self):
        return self.head.data

    def str(self):
        
        if (self.is_empty()):
            print("[]")
        else:
            print("[", self.head.data, ", ",sep='', end='')
            node = self.head.next
            while node:
                
                if(node.next is None):
                    print(node.data,"]",sep='')    
                else:
                    
                    print(node.data,", ",sep='',end='')

                
                node = node.next
      
    def add_end(self,elem):
        
        new_node = Node(elem)
        if self.head is None:
            self.head = new_node
        node = self.head

        while node.next:
            
            node = node.next
        new_node.next = node.next
        node.next = new_node
        
    def remove_end(self):
        node = self.head
        iter = 0
        while node.next:
            iter += 1
            node = node.next
            if (iter == self.length() - 2):
                node.next = None
        
    def take(self,list,n):
        if isinstance(list, List):
            node = Node(list[0])
            node.next = self.head
            self.head = node
            
            if(n > len(list)):
                for i in range(1,len(list)):
                    node.next = Node(list[i])
                    node = node.next
            else:
                for i in range(1,n):
                    node.next = Node(list[i])
                    node = node.next

    def drop(self,list,n):
        if isinstance(list, List):
            
            
            if(n < len(list)):
                node = Node(list[n])
                node.next = self.head
                self.head = node
                for i in range(n + 1,len(list)):
                    node.next = Node(list[i])
                    node = node.next
            else:
                self.head = None

def main():

    list = LinkedList() #Utworzenie pustej listy
    list.str()
    list.add(('PG','Gdańsk',1945))## Dodawanie elementów na początek listy
    list.add(('UP','Poznań',1919))
    list.add(('UW','Warszawa',1915))
    list.str()
    list.add(('PW','Warszawa',1915))
    list.add(('UJ','Kraków',1364))
    list.add(('AGH','Kraków',1919))
    list.str() # Wypisanie listy
   
    
    list.remove() # Usunięcie elementu z początku listy
    list.str()
    list.add(('AGH','Kraków',1919))
    print(list.is_empty()) #Sprawdzenie czy lista jest pusta

    print(list.length()) # Długość listy

    print(list.get()) # Zwrócenie 1 elementu listy

    list.add_end(('Nowy','Kraków',2022)) # Dodanie elementu na koniec listy
    list.str()
    list.remove_end() # Usunięcie elementu z końca listy
    list.str()
    list.destroy() #Zniszczenie listy
    list.str()


    list_1 = LinkedList()
    list_1.take([1,2,3,4,5,6,7,8,9,10], 5) # Stworzenie listy wiązanej z n elementów podanej listy
    list_1.str()
    list_1.destroy()
    list_1.take([1,2,3,4,5,6,7,8,9,10], 12) # Ta sama sytuacja dla n większego od rozmiaru listy
    list_1.str()  
    list_1.destroy()
    list_1.drop([1,2,3,4,5,6,7,8,9,10], 5) # Stworzenie listy wiązanej z pominięciem n pierwszych elementów podanej listy
    list_1.str()
    list_1.destroy()
    list_1.drop([1,2,3,4,5,6,7,8,9,10], 12) # Pusta lista dla n większego od rozmiaru listy
    list_1.str()
    
if __name__ == "__main__":
    main()