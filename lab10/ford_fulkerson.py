import numpy as np



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
    def __str__(self) -> str:
        return str(self.key)
    

class Edge:
    def __init__(self,capacity,isR,flow = 0, residual = None): 
        
        self.capacity = capacity
        self.flow = flow
        self.isResidual = isR
        if residual == None:
            self.residual = capacity
        else:
            self.residual = residual 

    def __str__(self):
        return str(self.capacity) + ' ' + str(self.flow) + ' ' + str(self.residual) + ' ' + str(self.isResidual)

    def __repr__(self):
        rep = self.capacity + ' ' + self.flow + ' ' + self.residual + ' ' + self.isResidual
        return rep


class Graph:
    def __init__(self):
        self.vertex_list: list[Vertex] = []
        self.neigh_list: list[list[(int, int)]] = []
        self.dict = {}
        




    def insertVertex(self,vertex):
        
        
        self.vertex_list.append(vertex)
        self.dict[hash(vertex)] = len(self.vertex_list) - 1
        self.neigh_list.append([])

         
          


    def insertEdge(self, vertex1, vertex2,capacity):
        if (vertex1 and vertex2) in self.vertex_list:
            
            self.neigh_list[self.dict[hash(vertex1)]].append((vertex2, Edge(capacity,False)))
            self.neigh_list[self.dict[hash(vertex2)]].append((vertex1, Edge(capacity,True, residual=0)))
                
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
                edges_list.append((self.vertex_list[i].key,self.neigh_list[i][j][0].key))
        return edges_list


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

def BFS(g, start):
    
    n = len(g.vertex_list)
    visited = [0] * n
    parent = [-1] * n 
    queue = []

    queue.append(start)
    visited[g.getVertexIdx(start)] = 1

    while queue:
        elem = queue.pop(0)
        
        
        neigh = g.neighbours(g.getVertexIdx(elem))
        for i in range(len(neigh)):
            if visited[g.getVertexIdx(neigh[i][0])] == 0 and neigh[i][1].residual > 0:
                queue.append(neigh[i][0])
                visited[g.getVertexIdx(neigh[i][0])] = 1
                parent[g.getVertexIdx(neigh[i][0])] = elem
                
    return parent

def trace(graph,vertex1,vertex2,parents):
    index = graph.getVertexIdx(vertex2)
    min_capacity = float('inf')
    if not isinstance(parents[index],Vertex):
        return 0
    else:
        while graph.getVertex(index) != vertex1:
            parent = parents[index]
            neigh = graph.neighbours(graph.getVertexIdx(parent))
            for i in neigh:
                if i[0] == graph.getVertex(index):
                    if i[1].isResidual == False:
                        if i[1].residual < min_capacity:
                            min_capacity = i[1].residual
            index = graph.getVertexIdx(parent)
    return min_capacity

def augmenting(graph,vertex1,vertex2,parents,min_capacity):
    index = graph.getVertexIdx(vertex2)
    if not isinstance(parents[index],Vertex):
        return 0
    else:
        while graph.getVertex(index) != vertex1:
            parent = parents[index]
            neigh = graph.neighbours(graph.getVertexIdx(parent))
            for i in neigh:
                if i[0] == graph.getVertex(index):
                    if i[1].isResidual == False:
                        i[1].residual -= min_capacity
                
                        i[1].flow += min_capacity
                

            vert_neigh = graph.neighbours(index)
            for j in vert_neigh:
                if j[0] == parent:
                    if j[1].isResidual == True:
                        j[1].residual += min_capacity
            index = graph.getVertexIdx(parent)
    return graph

def ford_fulkerson(graph,vertex1,vertex2):
    bfs = BFS(graph,vertex1)
    max_flow = 0
    min_cap = trace(graph,vertex1,vertex2,bfs)
    max_flow = min_cap
    while min_cap > 0:
        graph = augmenting(graph,vertex1,vertex2,bfs,min_cap)
        bfs = BFS(graph,vertex1)
        min_cap = trace(graph,vertex1,vertex2,bfs)
        max_flow += min_cap 

    return max_flow,graph









        

def main():
    
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graph = Graph()
    for i in graf_0:
        vert1 = Vertex(i[0])
        vert2 = Vertex(i[1])
    
        if not vert1 in graph.vertex_list:
            graph.insertVertex(vert1)

        if not vert2 in graph.vertex_list:
            graph.insertVertex(vert2)

        graph.insertEdge(vert1, vert2, i[2]) 

    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]

    graph1 = Graph()
    for j in graf_1:
        vert1 = Vertex(j[0])
        vert2 = Vertex(j[1])
    
        if not vert1 in graph1.vertex_list:
            graph1.insertVertex(vert1)

        if not vert2 in graph1.vertex_list:
            graph1.insertVertex(vert2)

        graph1.insertEdge(vert1, vert2, j[2])

    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]

    graph2 = Graph()
    for k in graf_2:
        vert1 = Vertex(k[0])
        vert2 = Vertex(k[1])
    
        if not vert1 in graph2.vertex_list:
            graph2.insertVertex(vert1)

        if not vert2 in graph2.vertex_list:
            graph2.insertVertex(vert2)

        graph2.insertEdge(vert1, vert2, k[2])

    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]

    graph3 = Graph()
    for l in graf_3:
        vert1 = Vertex(l[0])
        vert2 = Vertex(l[1])
    
        if not vert1 in graph3.vertex_list:
            graph3.insertVertex(vert1)

        if not vert2 in graph3.vertex_list:
            graph3.insertVertex(vert2)

        graph3.insertEdge(vert1, vert2, l[2])

       


 
    
    #printGraph(graph2)
    #printGraph(graph3)
    

    ford = ford_fulkerson(graph,Vertex('s'),Vertex('t'))
    print(ford[0])
    printGraph(ford[1])
    

    ford1 = ford_fulkerson(graph1,Vertex('s'), Vertex('t'))
    print(ford1[0])
    printGraph(ford1[1])
    

    ford2 = ford_fulkerson(graph2,Vertex('s'),Vertex('t'))
    print(ford2[0])
    printGraph(ford2[1])
    

    ford3 = ford_fulkerson(graph3,Vertex('s'),Vertex('t'))
    print(ford3[0])
    printGraph(ford3[1])
    


   



if __name__ == "__main__":      
    main()  