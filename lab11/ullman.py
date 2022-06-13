from copy import deepcopy
import numpy as np

class Vertex:
    def __init__(self,key):
        self.key = key
    def __eq__(self,other):
        return self.key == other.key
    def __hash__(self):
        return hash(self.key)



class Graph:
    def __init__(self):
        self.vertex_list: list[Vertex] = []
        self.neigh_matrix: list[list[int]] = []
        self.dict = {}

    def get_neigh_matrix(self):
        return self.neigh_matrix

    def insertVertex(self,vertex):
        
        
        self.vertex_list.append(vertex)
        self.dict[hash(vertex)] = len(self.vertex_list) - 1
        self.neigh_matrix.append([])
        for i in range(len(self.neigh_matrix)):
            self.neigh_matrix[i].append(0)

            if len(self.neigh_matrix[i]) < len(self.neigh_matrix[0]):
                diff = len(self.neigh_matrix[0]) - len(self.neigh_matrix[i])
                for j in range(diff):

                    self.neigh_matrix[i].append(0)

         
          


    def insertEdge(self, vertex1, vertex2, edge = None):
        if (vertex1 and vertex2) in self.vertex_list:
            
                self.neigh_matrix[self.dict[hash(vertex1)]][self.dict[hash(vertex2)]] = 1
                self.neigh_matrix[self.dict[hash(vertex2)]][self.dict[hash(vertex1)]] = 1
        else:
            return None
            


    def deleteVertex(self,vertex):
        if vertex in self.vertex_list:
            
                
            index = self.getVertexIdx(vertex) 
                    
            
            self.vertex_list.remove(vertex)
            list_of_keys = list(self.dict.keys())
            for i in range(len(self.neigh_matrix)):
                self.neigh_matrix[i][self.getVertexIdx(vertex)] = 0
            del self.neigh_matrix[self.getVertexIdx(vertex)]
            for j in range(len(self.neigh_matrix)):
                del self.neigh_matrix[j][self.getVertexIdx(vertex)]

            

            for l in range(index,len(list_of_keys)):
                if l == index:
                    del self.dict[list_of_keys[l]]
            new_list_of_keys = list(self.dict.keys())
            for m in range(index,len(new_list_of_keys)):
                self.dict[new_list_of_keys[m]] = m


    def deleteEdge(self, vertex1, vertex2):
        self.neigh_matrix[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)] = 0
        self.neigh_matrix[self.getVertexIdx(vertex2)][self.getVertexIdx(vertex1)] = 0
    def getVertexIdx(self,vertex):
        return self.dict[hash(vertex)]
    def getVertex(self,vertex_idx):
        return self.vertex_list[vertex_idx]
    def neighbours(self,vertex_idx):
        return self.neigh_matrix[vertex_idx]
    def order(self):
        return len(self.vertex_list)
    def size(self):
        size = 0
        for i in range(len(self.neigh_matrix)):
            size += len(self.neigh_matrix[i])
        return size//2

    def edges(self):
        edges_list = []
        for i in range(len(self.neigh_matrix)):
            for j in range(len(self.neigh_matrix[i])):
                if self.neigh_matrix[i][j] == 1:
                    edges_list.append((self.vertex_list[i].key,self.vertex_list[j].key))
        return edges_list

def ullman(used_cols, current_row, G, P, M, no_recursion = 0, no_izo = 0):

    
    
    if current_row == M.shape[0]:
        MG = np.dot(M,G)
        izo = np.dot(M, np.transpose(MG))
        if np.array_equal(izo, P):
            no_izo += 1
            
        return no_izo, no_recursion

    copy_M = deepcopy(M)
    if current_row < M.shape[0]:
        for c in range(copy_M.shape[1]):
            if c  not in used_cols:
                no_recursion += 1
                copy_M[current_row][:] = 0
                copy_M[current_row][c] = 1
                used_cols.append(c)
                res =ullman(used_cols,current_row+1,G, P, copy_M, no_recursion, no_izo)
                if res is not None:
                    no_recursion = res[1]
                    no_izo = res[0]
                used_cols.remove(c)
            
    return no_izo, no_recursion

def m0(M,G,P):
    M = np.zeros((M.shape[0], M.shape[1]))
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if sum(G[j]) >= sum(P[i]):
                M[i][j] = 1
            else:
                M[i][j] = 0
    return M
        

def ullman_prune(used_cols, current_row, G, P, M , no_recursion = 0, no_izo = 0):
    
    
    if current_row == M.shape[0]:
        MG = np.dot(M,G)
        izo = np.dot(M, np.transpose(MG))
        if np.array_equal(izo, P):
            no_izo += 1
            
        return no_izo, no_recursion

    
   
    
    copy_M = deepcopy(M)
    
    M = prune(M,G,P)
    if current_row < M.shape[0]:
        for c in range(M.shape[1]):
            if c  not in used_cols and M[current_row][c]:
                
                no_recursion += 1
                
                copy_M[current_row][:] = 0
                copy_M[current_row][c] = 1
                used_cols.append(c)
                
                res =ullman_prune(used_cols,current_row+1,G, P, copy_M, no_recursion, no_izo)
                if res is not None:
                    no_izo = res[0]
                    no_recursion = res[1]
                
                
                used_cols.remove(c)
            
    return no_izo, no_recursion
   


def prune(M, G, P, check = True):
        


    
    while check:
        check = False
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):# Chodzimy po 1 w macierzy M
                if M[i][j]:
                    P_neighbours = []  # Wyznaczamy sąsiadów
                    G_neighbours = []
                    for k in range(len(P[i])):
                        if P[i][k] != 0:
                            P_neighbours.append(k)
                    for l in range(len(G[j])):
                        if G[j][l] != 0:
                            G_neighbours.append(l)
                    odp = False
                    for x in P_neighbours:
                        for y in G_neighbours:
                            if M[x][y] == 1:
                                odp = True
                                     
                        if odp:
                            break
                    else:
                        M[i][j] = 0
                        check = True
    return M




def ullman_m0(used_cols, current_row, G, P, M, no_recursion = 0, no_izo = 0,  M_0 = None):
    
    
    if current_row == M.shape[0]:
        MG = np.dot(M,G)
        izo = np.dot(M, np.transpose(MG))
        if np.array_equal(izo, P):
            no_izo += 1
           
        return no_izo, no_recursion
    if current_row < M.shape[0]:
        
        copy_M = deepcopy(M)

        if M_0 is None:
            M_0 = m0(M,G,P)
        for c in range(copy_M.shape[1]):
            if c  not in used_cols and M_0[current_row][c]:
                
                no_recursion += 1

                copy_M[current_row][:] = 0
                copy_M[current_row][c] = 1
                used_cols.append(c)
                res =ullman_m0(used_cols,current_row+1,G, P, copy_M, no_recursion, no_izo, M_0)
                if res is not None:
                    no_recursion = res[1]
                    no_izo = res[0]
                used_cols.remove(c)
                
        return no_izo, no_recursion
                    
                

   





def main():
    graf = Graph()
    vert_a = Vertex('A')
    vert_b = Vertex('B')
    vert_c = Vertex('C')
    vert_d = Vertex('D')
    vert_e = Vertex('E')
    vert_f = Vertex('F')

    graf.insertVertex(vert_a)
    graf.insertVertex(vert_b)
    graf.insertVertex(vert_c)
    graf.insertVertex(vert_d)
    graf.insertVertex(vert_e)
    graf.insertVertex(vert_f)

    graf.insertEdge(vert_a,vert_b)
    graf.insertEdge(vert_b,vert_f)
    graf.insertEdge(vert_b,vert_c)
    graf.insertEdge(vert_c,vert_d)
    graf.insertEdge(vert_c,vert_e)
    graf.insertEdge(vert_d,vert_e)



    graf2 = Graph()
    

    graf2.insertVertex(vert_a)
    graf2.insertVertex(vert_b)
    graf2.insertVertex(vert_c)
    

    graf2.insertEdge(vert_a,vert_b)
    graf2.insertEdge(vert_b,vert_c)
    graf2.insertEdge(vert_a,vert_c)
    


    G = np.array(graf.get_neigh_matrix())
    P = np.array(graf2.get_neigh_matrix())
    M = np.zeros((P.shape[0], G.shape[0]))
    ul = ullman([],0,G,P,M) 
    print(ul[0], ul[1])   


    ul_m0 = ullman_m0([],0,G,P,M)
    print(ul_m0[0],ul_m0[1])

    ul_p = ullman_prune([],0,G,P,m0(M,G,P))
    print(ul_p[0],ul_p[1])


if __name__ == "__main__":      
    main()  