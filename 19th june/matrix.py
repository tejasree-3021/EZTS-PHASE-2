R=int(input())
C=int(input())
matrix=[]
print(int(input("enter entries")))
for i in range(R):          
    a =[]
    for j in range(C):     
         a.append(int(input()))
    matrix.append(a)
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()
print("diagonal elements")
for i in range(R):
    for j in range(C):
        if i==j:
            print(matrix[i][j],end=" ")
            print()
print(" not diagonal elements")        
for i in range(R):
    for j in range(C):
        if i!=j:
            print(matrix[i][j],end=" ")
            print()

print(" lower diagonal elements")
for i in range(R):
    for j in range(C):
        if i<=j:
            print(matrix[i][j],end=" ")
            print()

print(" upper diagonal elements")
for i in range(R):
    for j in range(C):
        if i>=j:
            print(matrix[i][j],end=" ")
            print()

print("The Transpose Matrix is:")
for i in range(R):
    for j in range(C):
        print(matrix[j][i],end=" ")
    print()
# print("The Addition ")