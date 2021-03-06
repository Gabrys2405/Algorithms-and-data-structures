from typing import List



class Node:

    def __init__(self,data):
        self.data = data
        self.next = None




def nil():
    head = None
    return head
def cons(el,list):
    element = Node(el)
    element.next = list 
    return element
def first(list):
    head = list
    return head.data


def rest(list):
    list = list.next
    return list




def create(): 
    return nil()
    

def destroy(list): 
    return nil()

    

def add(el,list): 
    return cons(el,list)

     
def is_empty(list):
    if list:
        return False
    else:
        return True

def remove(list):
    return rest(list)
     

def length(list,iter = 0):
    if is_empty(list):
        return iter 
    else:
        
        first_el = first(list)
        rest_lst = rest(list)
        iter += 1
        return length(rest_lst,iter)



def get(list):
    return first(list)


def print_list(list,iter = 0):
    
    if iter == 0:
        print('[',end='')
    if is_empty(list):
        print(']')
    else:
    
        first_el = first(list)
        rest_lst = rest(list)
        iter += 1
        if rest_lst:
            print(first_el,', ',end='',sep='') 
            print_list(rest_lst,iter)
        else:
            print(first_el,end='') 
            print_list(rest_lst,iter) 
        
    



def add_end(el,list):
    if is_empty(list):
        return cons(el,list)
    else:
        first_el = first(list)
        rest_lst = rest(list)
        recreated_lst = add_end(el,rest_lst)
        return cons(first_el,recreated_lst)


def remove_end(list):
    if length(list) == 1:
        return remove(list)
    else:
        first_el = first(list)
        rest_lst = rest(list)
        recreated_lst = remove_end(rest_lst)
        return cons(first_el,recreated_lst)

def take(list,n):
    if isinstance(list, List):
        lista = nil()
        lista = add(list[0],lista)
        
        if(n > len(list)):
            for i in range(1,len(list)):
                lista = add_end(list[i],lista)
                
        else:
            for i in range(1,n):
                lista = add_end(list[i],lista)

        return lista

def drop(list,n):
    if isinstance(list, List):
        lista = nil()
        
        
        if(n < len(list)):
            lista = add(list[n],lista)
            for i in range(n + 1,len(list)):
                lista = add_end(list[i],lista)
            return lista
        else:
            return lista



def main():
    
    
    list = create() #Utworzenie pustej listy
    print_list(list)
    list = add(('PG','Gda??sk',1945),list)## Dodawanie element??w na pocz??tek listy
    list = add(('UP','Pozna??',1919),list)
    list = add(('UW','Warszawa',1915),list)
    print_list(list)
    list = add(('PW','Warszawa',1915),list)
    list = add(('UJ','Krak??w',1364),list)
    list = add(('AGH','Krak??w',1919),list)
    print_list(list) # Wypisanie listy
   
 
    list = remove(list) # Usuni??cie elementu z pocz??tku listy
    print_list(list)
    list = add(('AGH','Krak??w',1919),list)
    print(is_empty(list)) #Sprawdzenie czy lista jest pusta

    print(length(list)) # D??ugo???? listy

    print(get(list)) # Zwr??cenie 1 elementu listy

    list = add_end(('Nowy','Krak??w',2022),list) # Dodanie elementu na koniec listy
    print_list(list)
    list = remove_end(list) # Usuni??cie elementu z ko??ca listy
    print_list(list)
    list = destroy(list) #Zniszczenie listy
    print_list(list)


    
    list_1 = take([1,2,3,4,5,6,7,8,9,10], 5) # Stworzenie listy wi??zanej z n element??w podanej listy
    print_list(list_1)
    list_1 = destroy(list_1)
    list_1 = take([1,2,3,4,5,6,7,8,9,10], 12) # Ta sama sytuacja dla n wi??kszego od rozmiaru listy
    print_list(list_1)
    list_1 = destroy(list_1)
    list_1 = drop([1,2,3,4,5,6,7,8,9,10], 5) # Stworzenie listy wi??zanej z pomini??ciem n pierwszych element??w podanej listy
    print_list(list_1)
    list_1 = destroy(list_1)
    list_1 = drop([1,2,3,4,5,6,7,8,9,10], 12) # Pusta lista dla n wi??kszego od rozmiaru listy
    print_list(list_1)


if __name__ == "__main__":
    main()


