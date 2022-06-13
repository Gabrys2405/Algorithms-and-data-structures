import string
import numpy as np


def string_compare(P, T, i, j):
    
    
    if i == 0: return j
    if j == 0: return i
    compare = 1 if P[i] != T[j] else 0
    change = string_compare(P,T, i - 1, j - 1) + compare
    insert = string_compare(P,T, i, j - 1) + 1
    delete = string_compare(P, T, i - 1, j) + 1
    return min(change, insert, delete)




def PD(P,T):
    D = np.zeros((len(P), len(T)))
    parents = np.zeros((len(P), len(T))).astype('str')
    for i in range(D.shape[0]):
        D[i][0] = i
    for j in range(D.shape[1]):
        D[0][j] = j

    for i in range(parents.shape[0]):
        for j in range(parents.shape[1]):
            if i > 0 and j > 0:
                parents[i][j] = 'X'
            elif i == 0 and j > 0:
                parents[i][j] = 'I'
            elif j ==0  and i > 0:
                parents[i][j] = 'D'
            elif i == 0 and j == 0:
                parents[i][j] = 'X'
    for i in range(1,parents.shape[0]):
        for j in range(1,parents.shape[1]):
            compare = 1 if P[i] != T[j] else 0
            change = D[i - 1][j - 1] + compare 
            insert = D[i, j - 1] + 1
            delete = D[i - 1, j] + 1
            
            mini = min(change, insert, delete)
            D[i][j] = mini
            if mini == insert:
                
                parents[i][j] = 'I'
                
            if mini == delete:
                
                parents[i][j] = 'D'
                
            if mini == change:
                if compare:

                    
                    parents[i][j] = 'S'
                    
                else:
                    parents[i][j] = 'M'
                    
    return int(D[-1][-1]), parents, D
def reconstruct(parents,P,T):
    
    i = parents.shape[0]-1
    j = parents.shape[1]-1
    check = parents[i][j]
    lista = []
    n_change = [] # najdłuższa wspólna sekwencja do podpunktu e)
    while check != 'X':
        lista.append(check)
        if check == 'M' or check == 'S':
            if check == 'M':
                n_change.append(P[i])
            
            i -= 1
            j -= 1
            
        elif check == 'D':
            i -= 1
        elif check == 'I':
            j -= 1

        check = parents[i][j]
    lista = lista[::-1]
    n_change = n_change[::-1]
    str1 = ''
    str2 = ''
    for ele in lista:
        str1 += ele
    for ele1 in n_change:
        str2+= ele1
    return str1, str2

def fit(P,T):
    D = np.zeros((len(P), len(T)))
    parents = np.zeros((len(P), len(T))).astype('str')
    for i in range(1,D.shape[0]):
        D[i][0] = i
    for j in range(D.shape[1]):
        D[0][j] = 0

    for i in range(parents.shape[0]):
        for j in range(parents.shape[1]):
            if j > 0 and i >= 0:
                parents[i][j] = 'X'
            
            elif j ==0  and i > 0:
                parents[i][j] = 'D'
            elif i == 0:
                parents[i][j] = 'X'
    for i in range(1,parents.shape[0]):
        for j in range(1,parents.shape[1]):
            compare = 1 if P[i] != T[j] else 0
            change = D[i - 1][j - 1] + compare 
            insert = D[i, j - 1] + 1
            delete = D[i - 1, j] + 1
            
            mini = min(change, insert, delete)
            D[i][j] = mini
            if mini == insert:
                
                parents[i][j] = 'I'
                
            if mini == delete:
                
                parents[i][j] = 'D'
                
            if mini == change:
                if compare:

                    
                    parents[i][j] = 'S'
                    
                else:
                    parents[i][j] = 'M'
                    
    return D[-1][-1], parents, D


    

def goal_cell(P,T):
    i = len(P) - 1
    j = 0
    
    D = fit(P,T)[2]
    
    for k in range(1,len(T)):
        if D[i][k] < D[i][j]:
            j = k
    iter = 0
    for i in range(len(P)):
        if P[i] != ' ':
            iter += 1
    j = j - (iter - 1)       
    return j
def sequence(P,T):
    D = np.zeros((len(P), len(T)))
    parents = np.zeros((len(P), len(T))).astype('str')
    for i in range(D.shape[0]):
        D[i][0] = i
    for j in range(D.shape[1]):
        D[0][j] = j

    for i in range(parents.shape[0]):
        for j in range(parents.shape[1]):
            if i > 0 and j > 0:
                parents[i][j] = 'X'
            elif i == 0 and j > 0:
                parents[i][j] = 'I'
            elif j ==0  and i > 0:
                parents[i][j] = 'D'
            elif i == 0 and j == 0:
                parents[i][j] = 'X'
    for i in range(1,parents.shape[0]):
        for j in range(1,parents.shape[1]):
            compare = np.inf if P[i] != T[j] else 0
            change = D[i - 1][j - 1] + compare 
            insert = D[i, j - 1] + 1
            delete = D[i - 1, j] + 1
            
            mini = min(change, insert, delete)
            D[i][j] = mini
            if mini == insert:
                
                parents[i][j] = 'I'
                
            if mini == delete:
                
                parents[i][j] = 'D'
                
            if mini == change:
                if compare:

                    
                    parents[i][j] = 'S'
                    
                else:
                    parents[i][j] = 'M'
                    
    res, n_change = reconstruct(parents, P, T)
    
    return n_change 

def sort_seq(P):
    lista = []
    for i in P:
        if i != ' ':
            lista.append(i)
    for j in range(len(lista)):
        lista[j] = int(lista[j])
    lista = sorted(lista)
    str1 = ''
    for elem in lista:
        str1 += str(elem)
    seq = sequence(P,str1)
    return seq


def main():

    
    #a)wariant rekurencyjny
    P = ' kot'
    T = ' pies'
    cost = string_compare(P,T, len(P) - 1, len(T) - 1)
    print(cost)
    
    
    #b)wariant PD
    K = ' biały autobus'
    D = ' czarny autokar'

    
    
    result = PD(K,D)
    print(result[0])
    

    #c) odtwarzanie ścieżki
    P2 = ' thou shalt not'
    T2 = ' you should not'

    res,res1,res2 = PD(P2,T2)
    rec, n_change = reconstruct(res1, P2, T2)
    print(rec)
    #d) dopasowanie podciągów
    P3 = ' ban'
    T3 = ' mokeyssbanana'
    goal = goal_cell(P3,T3)
    print(goal)
    #e) najdłuższa wspólna sekwencja 
    P4 = ' democrat'
    T4 = ' republican'

    print(sequence(P4,T4))
    
    #f) podsekwencja monotoniczna
    
    P5 = ' 243517698'
    print(sort_seq(P5)) 

    
if __name__ == "__main__":      
    main()  