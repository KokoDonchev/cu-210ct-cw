"""
Week 2 Task 3

Write the pseudocode corresponding to functions for addition, subtraction and
multiplication of two matrices, and then compute A=B*C –2*(B+C), where B and C
are two quadratic matrices of order n. What is the run-time?

Let's say that our Matrices are going to have 3 rows and 3 columns

GENERATE-MATRIX(n)
    matrix <- new Matrix()
    FOR all values in n
        matrix.push([0] * n)

    RETURN matrix

This helps us create an empty matrix
[0, 0, 0]
[0, 0, 0]
[0, 0, 0]

ADDITION(A, B)
    length <- sizeof(A)
    Z <- GENERATE-MATRIX(length)
        for a in length
            for b in length
                Z[a][b] = A[a][b] + B[a][b]
        return Z

SUBTRACTION(A, B)
    length <- sizeof(A)
    Z <- GENERATE-MATRIX(length)
        for a in length
            for b in length
                Z[a][b] = A[a][b] - B[a][b]
        return Z

MULTIPLICATION(A, B)
    length <- sizeof(A)
    Z <- GENERATE-MATRIX(length)
    if B is an Integer
        for a in length
            for b in length
                Z[a][b] = A[a][b] * B
    else
        for a in length
            for b in length
                Z[a][b] = A[a][b] * B[a][b]
    return Z

"""

# some tests

def generateMatrix(n):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)

    return matrix

n = 3
B = generateMatrix(n)
C = generateMatrix(n)


B[0] = [1,2,3]
B[1] = [6,7,8]
B[2] = [9,8,1]

C[0] = [4,1,1]
C[1] = [4,2,2]
C[2] = [1,8,4]

def Addition(A, B):
    length = len(A)
    Z = generateMatrix(length)
    for a in range(length):
        for b in range(length):
            Z[a][b] = A[a][b] + B[a][b]
    return Z

def Subtraction(A, B):
    length = len(A)
    Z = generateMatrix(length)
    for a in range(length):
        for b in range(length):
            Z[a][b] = A[a][b] - B[a][b]
    return Z

def Multiplication(A, B):
    length = len(A)
    Z = generateMatrix(length)
    if type(B) == int:
        for a in range(length):
            for b in range(length):
                Z[a][b] = A[a][b] * B
    else:
        for a in range(length):
            for b in range(length):
                Z[a][b] = A[a][b] * B[a][b]
    return Z

print(Subtraction(Multiplication(B, C), Multiplication(Addition(B, C), 2)))