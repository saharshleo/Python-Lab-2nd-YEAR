def lowerTriangular(m):
	return [[0 if i>j else 1 for i in range(m)]for j in range(m)]

def upperTriangular(m):
	return [[0 if i<j else 1 for i in range(m)]for j in range(m)]

def transpose(matrix):
	return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def multiplication(matrix1,matrix2):	
	matrix=[[]]
	sum=0
	for i in range(len(matrix1)):
		for j in range(len(matrix2)):
			sum=sum+matrix1[i][j]*matrix2[i][j]
			matrix[i][j]
	
l=int(input())
print(lowerTriangular(l))
print(upperTriangular(l))
print(transpose(lowerTriangular(l)))			
