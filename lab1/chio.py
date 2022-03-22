from matrix import Matrix

def chio(mat: Matrix) -> int:
    if (mat[0][0] != 0):    
        if (len(mat) == len(mat[0])):
            ch_matrix = Matrix((len(mat) - 1,len(mat[0]) - 1),0)
            if (len(mat) > 2):
                for i in range(len(ch_matrix)):
                    for j in range(len(ch_matrix[0])):
                        ch_matrix[i][j] = mat[0][0] * mat[i + 1][j + 1] - mat[0][j + 1] * mat[i + 1][0]   
                return 1/(mat[0][0] **(len(mat) - 2)) * chio(ch_matrix)    
            elif(len(mat) <= 2):
                return mat[0][0]*mat[1][1] - mat[0][1] * mat[1][0]
    else:
        if (len(mat) <= 2):
             return mat[0][0]*mat[1][1] - mat[0][1] * mat[1][0]
        else:
            det = 0
            row = 0
            col = 0

            compl = Matrix((len(mat) - 1, len(mat[0]) - 1), 0)
            
            for k in range(len(mat)):    
                for i in range(len(compl)):
                    for j in range(len(compl[0])):
                        if (j >= col):
                            compl[i][j] = mat[i + 1][j + 1]
                        else:
                            compl[i][j] = mat[i + 1][j]
                det += (-1)**(col + 1 + row + 1) * mat[row][col] * chio(compl)
                col += 1 
            return det 
                
            

A = Matrix([

[5 , 1 , 1 , 2 , 3],

[4 , 2 , 1 , 7 , 3],

[2 , 1 , 2 , 4 , 7],

[9 , 1 , 0 , 7 , 0],

[1 , 4 , 7 , 2 , 2]

])


print("wyznacznik \n", chio(A))


print(A)


B = Matrix( [
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])
print("\n", B)


print(chio(B))


C = Matrix( [
     [0 , 3 , 5 , 7 , 3],
     [4 , 5 , 6 , 2 , 3],
     [1 , 8 , 2 , 3 , 7],
     [8 , 1 , 7 , 3 , 0],
     [4 , 4 , 3 , 2 , 9]
    ])

print ("\n",C)

print(chio(C))