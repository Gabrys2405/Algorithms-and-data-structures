import numpy as np
from graf_mst import graf


class Vertex:
    def __init__(self,key):
        self.key = key
        
    def __eq__(self,other):
        return self.key == other.key
    def __hash__(self):
        return hash(self.key)
    def set_color(self, color):
        self.color = color
    def get_color(self):
        return self.color
    

class Edge:
    def __init__(self, vertex1, vertex2, weight):
        self.vertex1 = vertex1
        self.vertex2 = vertex2 
        self.weight = weight
    


class Graph:
    def __init__(self):
        self.vertex_list: list[Vertex] = []
        self.neigh_list: list[list[(int, int)]] = []
        self.dict = {}




    def insertVertex(self,vertex):
        
        
        self.vertex_list.append(vertex)
        self.dict[hash(vertex)] = len(self.vertex_list) - 1
        self.neigh_list.append([])

         
          


    def insertEdge(self, vertex1, vertex2,weight, edge = None):
        if (vertex1 and vertex2) in self.vertex_list:
            
                self.neigh_list[self.dict[hash(vertex1)]].append((vertex2, weight))
                self.neigh_list[self.dict[hash(vertex2)]].append((vertex1, weight))
        else:
            return None
            


    def deleteVertex(self,vertex):
        if vertex in self.vertex_list:
            
                
            index = self.getVertexIdx(vertex) 
                    
            self.neigh_list.remove(self.neigh_list[index])
            self.vertex_list.remove(vertex)
            list_of_keys = list(self.dict.keys())
            for i in range(len(self.neigh_list)):
                for j in range(len(self.neigh_list[i])):
                    if self.neigh_list[i][j][0] == vertex:
                        self.neigh_list[i].remove(self.neigh_list[i][j])

            for l in range(index,len(list_of_keys)):
                if l == index:
                    del self.dict[list_of_keys[l]]
            new_list_of_keys = list(self.dict.keys())
            for m in range(index,len(new_list_of_keys)):
                self.dict[new_list_of_keys[m]] = m

            for n in range(len(self.neigh_list)):
                l = len(self.neigh_list[n])
                for o in range(l-1):
                    if self.neigh_list[n][o][0] == vertex:
                        del self.neigh_list[n][o]
                        l-=1

            
    def get_weight(self,vertex1, vertex2):
        return self.neigh_list[self.getVertexIdx(vertex1)][self.getVertexIdx(vertex2)][1]

    def deleteEdge(self, vertex1, vertex2):
        self.neigh_list[self.getVertexIdx(vertex1)].remove((vertex2, self.get_weight(vertex1,vertex2)))
        self.neigh_list[self.getVertexIdx(vertex2)].remove((vertex1,self.get_weight(vertex1,vertex2)))
    def getVertexIdx(self,vertex):
        return self.dict[hash(vertex)]
    def getVertex(self,vertex_idx):
        return self.vertex_list[vertex_idx]
    def neighbours(self,vertex_idx):
        return self.neigh_list[vertex_idx]
    def order(self):
        return len(self.vertex_list)
    def size(self):
        size = 0
        for i in range(len(self.neigh_list)):
            size += len(self.neigh_list[i])
        return size//2

    def edges(self):
        edges_list = []
        for i in range(len(self.neigh_list)):
            for j in range(len(self.neigh_list[i])):
                edges_list.append((self.vertex_list[i].key,self.neigh_list[i][j].key))
        return edges_list

    


def prim(graph: Graph, vertex: Vertex) -> Graph:
    MST = Graph()
    n = len(graph.vertex_list)
    intree = [0] * n
    distance = [np.float('Inf')] * n
    parent = [-1] * n 
    sum = 0 

    for j in graph.vertex_list:
        MST.insertVertex(j)

    while intree[graph.getVertexIdx(vertex)] == 0:
        intree[graph.getVertexIdx(vertex)] = 1
        for i in range(len(graph.neighbours(graph.getVertexIdx(vertex)))):
            if graph.neighbours(graph.getVertexIdx(vertex))[i][1] < distance[graph.getVertexIdx(graph.neighbours(graph.getVertexIdx(vertex))[i][0])] and intree[graph.getVertexIdx(graph.neighbours(graph.getVertexIdx(vertex))[i][0])] == 0:
                distance[graph.getVertexIdx(graph.neighbours(graph.getVertexIdx(vertex))[i][0])] = graph.neighbours(graph.getVertexIdx(vertex))[i][1]
                
                parent[graph.getVertexIdx(graph.neighbours(graph.getVertexIdx(vertex))[i][0])] = graph.getVertexIdx(vertex)
                # MST.insertEdge(graph.getVertex(graph.neigh_list[graph.getVertexIdx(vertex)]), parent(graph.getVertex(graph.neigh_list[graph.getVertexIdx(vertex)])), distance[graph.getVertexIdx(graph.neigh_list[graph.getVertexIdx(vertex)])])

        
        min = np.float('inf')
        for k in graph.vertex_list:
            if intree[graph.getVertexIdx(k)] == 0  and distance[graph.getVertexIdx(k)] < min:
                min = distance[graph.getVertexIdx(k)]
                vertex = k
        if min != np.float('inf'):
            MST.insertEdge(vertex, graph.getVertex(parent[graph.getVertexIdx(vertex)]),min)
            sum+=min
    return MST
        

    return MST  
def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v.key, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(g.getVertexIdx(j)).key, w, end=";")
        print()
    print("-------------------")






        

def main():
    
    # vertA = Vertex('A')
    # vertB = Vertex('B')
    # vertC = Vertex('C')
    # vertD = Vertex('D')
    # vertE = Vertex('E')
    # vertF = Vertex('F')
    # vertG = Vertex('G')
    # vertH = Vertex('H')
    # vertI = Vertex('I')
    # vertJ = Vertex('J')
   
    
    # graf.insertVertex(vertA)
    # graf.insertVertex(vertB)
    # graf.insertVertex(vertC)
    # graf.insertVertex(vertD)
    # graf.insertVertex(vertE)
    # graf.insertVertex(vertF)
    # graf.insertVertex(vertG)
    # graf.insertVertex(vertH)
    # graf.insertVertex(vertI)
    # graf.insertVertex(vertJ)
   
    # graf.insertEdge(vertA,vertC, 1)
    # graf.insertEdge(vertA,vertB, 4)
    # graf.insertEdge(vertC,vertD, 3)
    # graf.insertEdge(vertB,vertG, 7)
    # graf.insertEdge(vertG,vertJ, 8)
    # graf.insertEdge(vertG,vertF, 8)
    # graf.insertEdge(vertF,vertH, 2)
    # graf.insertEdge(vertF,vertE, 2)
    # graf.insertEdge(vertH,vertI, 3)



    # graf.insertEdge(vertD,vertJ, 18)
    # graf.insertEdge(vertD,vertG, 10)
    # graf.insertEdge(vertC,vertG, 9)
    # graf.insertEdge(vertA,vertD, 4)
    # graf.insertEdge(vertB,vertC, 5)
    # graf.insertEdge(vertB,vertE, 9)
    # graf.insertEdge(vertB,vertF, 9)
    # graf.insertEdge(vertE,vertH, 4)
    # graf.insertEdge(vertE,vertI, 6)

    # graf.insertEdge(vertI,vertJ, 9)
    # graf.insertEdge(vertH,vertJ, 9)
    # graf.insertEdge(vertG,vertH, 9)
    
    
    graph = Graph()
    
    for i in graf:
        vert1 = Vertex(i[0])
        vert2 = Vertex(i[1])
    
        if not vert1 in graph.vertex_list:
            graph.insertVertex(vert1)

        if not vert2 in graph.vertex_list:
            graph.insertVertex(vert2)

        graph.insertEdge(vert1, vert2, i[2]) 
       


 
    MST = prim(graph, graph.vertex_list[0])
    printGraph(MST)


if __name__ == "__main__":      
    main()  