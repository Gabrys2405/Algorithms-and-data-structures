class Matrix:
    
    def __init__(self,mat, p = 0):   
        if isinstance(mat, tuple):
            self.matr = [[p for x in range(mat[1])] for i in range(mat[0])]
        else:    
            self.matr = mat
    def __getitem__(self, row):## GOTOWE
        return self.matr[row]
    def __len__(self):
        return len(self.matr)
    def __str__(self):
        begin = str('[')
        end = str(']') 
        for i in range(len(self.matr)):
            begin += str(self.matr[i])
            if (i != len(self.matr) - 1):
                begin+= ",\n"
        
        return begin + end 

    def __add__(self,other):    
        if len(self.matr) == len(other.matr) and len(self.matr[0]) == len(other.matr[0]):
            result = Matrix((len(self.matr),len(self.matr[0])),p = 0)
            for i in range(len(self.matr)):
                for j in range(len(self.matr[0])):
                    result[i][j] = self.matr[i][j] + other.matr[i][j]
            return result
        else:
            return str("Wymiary macierzy nie są takie same")
    def __mul__(self,other):
        if len(self.matr[0]) == len(other.matr):
            result = Matrix((len(self.matr),len(other.matr[0]),0))
            for i in range(len(self.matr)):
                for j in range(len(other.matr[0])):
                    for k in range(len(self.matr[0])):
                        result[i][j] += self.matr[i][k]*other.matr[k][j]
            return result
        else:
            return str("Liczba kolumn macierzy A jest różna od liczby wierszy macierzy B")


        
        
def transpose(mat):
    result = Matrix((len(mat[0]),len(mat)),0)
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = mat[j][i] 
    return result 


    
def main():

    a = Matrix([[1, 0, 2], [-1, 3, 1]])
    b = Matrix((2, 3), 1)
    c = Matrix([[3, 1], [2, 1], [1, 0]])
    
    print("a = \n", a, "\n")
    print("b = \n", b, "\n")
    print("c = \n", c, "\n")
    
    print("Transpozycja macierzy a: \n", transpose(a),"\n")

    print("a + b = \n", a + b, "\n")

    print("a * c = \n", a * c, "\n")

    print(a * b, "\n")

    d = Matrix([[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,2,3,1]])

    print(d)

    del d[1]

    print(d)




    

if __name__ == "__main__":
    main()