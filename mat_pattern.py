n = int(input())
mat1 = [[0 if(i==0 or i==n-1 or j==0 or j==n-1) else 1 for i in range(n)]for j in range(n)]
print("mat1")
print(*mat1,sep="\n")
mat2 = [[0 if(i+j)%2==0 else 1 for i in range(n)]for j in range(n)]
print("mat2")
print(*mat2,sep="\n")
