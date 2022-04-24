class Vertex:
    def __init__(self,key):
        self.key = key
    def __eq__(self,other):
        return self.key == other.key
    def __hash__(self):
        return hash(self.key)
    

class Edge:
    def __init__(self):
        pass
    


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
        if vertex1:
            if self.vertex_list == self.vertex_list[hash(vertex2)] - 1:

                if self.neigh_list[self.dict[hash(vertex1)]] == []:
                    self.neigh_list[self.dict[hash(vertex1)]].append(vertex2)
            else:
                self.insertVertex(vertex2)
                self.insertVertex(vertex1, vertex2)


    def deleteVertex(self,vertex):
        pass
    def deleteEdge(self, vertex1, vertex2):
        pass
    def getVertexIdx(self,vertex):
        pass
    def getVertex(self,vertex_idx):
        pass
    def neighbours(self,vertex_idx):
        pass
    def order(self):
        pass
    def size(self):
        pass
    def edges(self):
        pass


def main():
    vert = Vertex('A')
    vert2 = Vertex('B')

    print(vert.__hash__())
    graph = Graph()
    graph.insertVertex(vert)
    
    graph.insertEdge(vert,vert2)


    print('Coś tam')

      
if __name__ == "__main__":      
    main()  