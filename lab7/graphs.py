from import_turtle import draw_map


class Vertex:
    def __init__(self,key):
        self.key = key
    def __eq__(self,other):
        return self.key == other.key
    def __hash__(self):
        return hash(self.key)
    

class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2 
    


class Graph:
    def __init__(self):
        self.vertex_list: list[Vertex] = []
        self.neigh_list: list[list[int]] = []
        self.dict = {}




    def insertVertex(self,vertex):
        
        
        self.vertex_list.append(vertex)
        self.dict[hash(vertex)] = len(self.vertex_list) - 1
        self.neigh_list.append([])

         
          


    def insertEdge(self, vertex1, vertex2, edge = None):
        if (vertex1 and vertex2) in self.vertex_list:
            
                self.neigh_list[self.dict[hash(vertex1)]].append(vertex2)
                self.neigh_list[self.dict[hash(vertex2)]].append(vertex1)
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
                    if self.neigh_list[i][j] == vertex:
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
                    if self.neigh_list[n][o] == vertex:
                        del self.neigh_list[n][o]
                        l-=1

            


    def deleteEdge(self, vertex1, vertex2):
        self.neigh_list[self.getVertexIdx(vertex1)].remove(vertex2)
        self.neigh_list[self.getVertexIdx(vertex2)].remove(vertex1)
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




class Graph2:
    def __init__(self):
        self.vertex_list: list[Vertex] = []
        self.neigh_matrix: list[list[int]] = []
        self.dict = {}




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
                    
            # self.neigh_matrix.remove(self.neigh_matrix[index])
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

            # for n in range(len(self.neigh_matrix)):
            #     l = len(self.neigh_matrix[n])
            #     for o in range(l-1):
            #         if self.neigh_matrix[n][o] == vertex:
            #             del self.neigh_matrix[n][o]
            #             l-=1

            


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
        

def main():
    graf = Graph()
    graf2 = Graph2()
    def test(graf):
        
        vert = Vertex('Z')
        vert2 = Vertex('G')
        vert3 = Vertex('N')
        vert4 = Vertex('B')
        vert5 = Vertex('F')
        vert6 = Vertex('P')
        vert7 = Vertex('C')
        vert8 = Vertex('E')
        vert9 = Vertex('W')
        vert10 = Vertex('L')
        vert11 = Vertex('D')
        vert12 = Vertex('O')
        vert13 = Vertex('S')
        vert14 = Vertex('T')
        vert15 = Vertex('K')
        vert16 = Vertex('R')
        
        graf.insertVertex(vert)
        graf.insertVertex(vert2)
        graf.insertVertex(vert3)
        graf.insertVertex(vert4)
        graf.insertVertex(vert5)
        graf.insertVertex(vert6)
        graf.insertVertex(vert7)
        graf.insertVertex(vert8)
        graf.insertVertex(vert9)
        graf.insertVertex(vert10)
        graf.insertVertex(vert11)
        graf.insertVertex(vert12)
        graf.insertVertex(vert13)
        graf.insertVertex(vert14)
        graf.insertVertex(vert15)
        graf.insertVertex(vert16)
        graf.insertEdge(vert,vert2)
        graf.insertEdge(vert,vert6)
        graf.insertEdge(vert,vert5)
        graf.insertEdge(vert2,vert6)
        graf.insertEdge(vert2,vert7)
        graf.insertEdge(vert2,vert3)
        graf.insertEdge(vert3,vert7)
        graf.insertEdge(vert3,vert9)
        graf.insertEdge(vert3,vert4)
        graf.insertEdge(vert4,vert9)
        graf.insertEdge(vert4,vert10)
    
        graf.insertEdge(vert5,vert6)
        graf.insertEdge(vert5,vert11)
        graf.insertEdge(vert6,vert7)
        graf.insertEdge(vert6,vert8)
        graf.insertEdge(vert6,vert12)
        graf.insertEdge(vert6,vert11)
        graf.insertEdge(vert7,vert9)
        graf.insertEdge(vert7,vert8)
        graf.insertEdge(vert8,vert9)
        graf.insertEdge(vert8,vert14)
        graf.insertEdge(vert8,vert13)
        graf.insertEdge(vert8,vert12)
        graf.insertEdge(vert9,vert10)
        graf.insertEdge(vert9,vert14)
        graf.insertEdge(vert10,vert16)
        graf.insertEdge(vert10,vert14)
        
        graf.insertEdge(vert11,vert12)
        graf.insertEdge(vert12,vert13)
        graf.insertEdge(vert13,vert14)
        graf.insertEdge(vert13,vert15)
        graf.insertEdge(vert14,vert16)
        graf.insertEdge(vert14,vert15)
        graf.insertEdge(vert15,vert16)
        graf.deleteVertex(vert15)
        graf.deleteEdge(vert9, vert8)
        graf_list = graf.edges()
        

        draw_map(graf_list)
    
    test(graf2)

    test(graf2)
   

      
if __name__ == "__main__":      
    main()  