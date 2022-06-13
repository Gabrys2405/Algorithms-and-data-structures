from copy import deepcopy
import numpy as np

class Node:
    def __init__(self, key, color = None):
        self.key = key
        self.color = color

    def __hash__(self):
        return hash(self.key)

    def __eq__(self, other):
        return hash(self) == hash(other)

class Matrix_graph:
    def __init__(self):
        self.vertices: list = []
        self.vertex_list: list[list] = []
        self.dict_list: dict = {}

    def insertVertex(self, vertex: Node):
        self.dict_list[hash(vertex)] = len(self.vertices)
        self.vertex_list.append([])
        for i in self.vertex_list:
            if i == self.vertex_list[-1]:
                for _ in self.vertex_list:
                    i.append(0)
            else:
                i.append(0)
        self.vertices.append(vertex)

    def insertEdge(self, vertex1: Node, vertex2: Node, edge=1):

        id1 = self.getVertexIdx(vertex1)
        id2 = self.getVertexIdx(vertex2)
        if id1 is None:
            self.insertVertex(vertex1)
            id1 = self.getVertexIdx(vertex1)

        if id2 is None:
            self.insertVertex(vertex2)
            id2 = self.getVertexIdx(vertex2)
        self.vertex_list[id1][id2] = edge

    def getVertexIdx(self, vertex: Node):
        if vertex in self.vertices:
            return self.dict_list[hash(vertex)]
        else:
            return None

    def deleteVertex(self, vertex: Node):
        id = self.getVertexIdx(vertex)
        del self.dict_list[hash(vertex)]
        self.vertices.remove(vertex)
        self.vertex_list = self.vertex_list[:id] + self.vertex_list[id + 1:]
        for i in range(len(self.vertex_list)):
            self.vertex_list[i] = self.vertex_list[i][:id] + self.vertex_list[i][id + 1:]
        dictionary: dict = {}
        j = 0
        for i in self.dict_list.keys():
            dictionary[i] = j
            j += 1
        self.dict_list = dictionary

    def deleteEdge(self, vertex1: Node, vertex2: Node):
        id1 = self.getVertexIdx(vertex1)
        id2 = self.getVertexIdx(vertex2)
        if id1 is None or id2 is None:
            return None
        self.vertex_list[id1][id2] = [None]

    def getVertex(self, vertex_idx):
        for i in self.vertices:
            id = self.getVertexIdx(i)
            if id == vertex_idx:
                return i
        return None

    def neighbours(self, vertex_idx):

        if self.dict_list[vertex_idx]:
            return self.dict_list[vertex_idx]
        else:
            return None

    def order(self):
        return len(self.vertices)

    def size(self):
        result = 0
        for i in self.vertex_list:
            for j in i:
                if j[0] == 1:
                    result += 1
        return result

    def edges(self):
        result = []
        k = 0
        for i in self.vertex_list:
            m = 0
            for j in i:
                if j[0] == 1:
                    kstr = self.getVertex(k)
                    mstr = self.getVertex(m)
                    result.append((kstr, mstr))
                m += 1
            k += 1

        return result

    def getVertexByKey(self, vertex_key):
        return self.vertices[self.dict_list[hash(vertex_key)]]
def policz(lista):
    ile = 0
    for i in range(len(lista)):
        if lista[i] != 0:
            ile = ile + 1
    return ile
def ullman(used_columns, current_row, G: np.array, P: np.array, M: np.array, tryb = 1, M_0 = None, no_recursion = 0, matrixs = []):
    no_recursion = no_recursion + 1
    if current_row == M.shape[0]:

        if np.array_equal(P, np.dot(M, np.transpose(np.dot(M, G)))):
            matrixs.append(M)
            return matrixs, no_recursion
    M_prim = deepcopy(M)

    if tryb != 1 and M_0 is None:
        M_0 = np.zeros((P.shape[0], G.shape[0]))
        for i in range(G.shape[0]):
            for j in range(P.shape[0]):

                if policz(G[i]) >= policz(P[j]):
                    M_0[j][i] = 1
        M_0[0], M_0[-1] = M_0[-1], M_0[0] #zamieniam wiersze w M_0 ?eby dosta? jaki? wynik

    if tryb == 3:
        M_prim = prune(G, P, M_prim)
        if M_prim is None:
            return False

    if current_row < M_prim.shape[0]:
        for c in range(M_prim.shape[1]):
            if c not in used_columns:
                if M_0 is not None:
                    if M_0[current_row][c] != 1:
                        continue
                M_prim[current_row][:] = 0
                M_prim[current_row][c] = 1

                used_columns.append(c)
                result = ullman(used_columns, current_row+1, G, P, M_prim, tryb, M_0, no_recursion, matrixs)
                no_recursion = result[1]
                if result[0] is not False:
                    if current_row == 0:
                        
                        print(len(result[0]))
                        return result[1]
                    elif result is False:
                        pass
                    else:
                        return result
                used_columns.remove(c)
    return False, no_recursion

def prune(G, P, M):
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if M[i][j] == 1:
                for x in range(len(P[i])):
                    if P[i][x] == 1:
                        zero = True
                        for y in range(len(G[j])):
                            if G[j][y] == 1:
                                if zero is True:
                                    if M[x][y] == 1:
                                        zero = False
                                        pass
                        if zero is True:
                            M[i][j] = 0
        """for k in M:
            if policz(k) == 0:
                return None"""
    return M

if __name__ == '__main__':
    graph_G = [('A', 'B', 1), ('B', 'F', 1), ('B', 'C', 1), ('C', 'D', 1), ('C', 'E', 1), ('D', 'E', 1)]
    graph_P = [('A', 'B', 1), ('B', 'C', 1), ('A', 'C', 1)]
    G = Matrix_graph()
    P = Matrix_graph()
    for i in graph_G:
        if i[0] not in G.vertices:
            G.insertVertex(Node(i[0]))
        if i[1] not in G.vertices:
            G.insertVertex(Node(i[1]))
    """ for i in ['A', 'B', 'C', 'D', 'E', 'F']:
        if i not in G.vertices:
            G.insertVertex(Node(i))"""

    for i in graph_G:
        G.insertEdge(Node(i[0]), Node(i[1]), i[2])

    for i in graph_P:
        if i[0] not in P.vertices:
            P.insertVertex(Node(i[0]))
        if i[1] not in P.vertices:
            P.insertVertex(Node(i[1]))

    for i in graph_P:
        P.insertEdge(Node(i[0]), Node(i[1]), i[2])

    G_mat = np.array(G.vertex_list)

    P_mat = np.array(P.vertex_list)

    M = np.zeros((P_mat.shape[0], G_mat.shape[0]))
    result = ullman([], 0, G_mat, P_mat, M, 2)

    if isinstance(result, tuple):
        if result[0] is False:
            print(0)
    else:
        print(result)
