x = [.55,.60,.65,.70]
y = [1.102,1.099,1.017,1.111]

def Vandermonde(x):
  """ This function finds the Vandermonde Matrix of a given set of numbers, it does this by making a square matrix with dimensions same as the lenght of the set of numbers, and then each number in the set is given a row and each column represents the number to the n-1 collumn while n is the column number  """  
  n = len(x)
  Vm = [[0]*n for row in range(n)]
  # creates a square matrix with n rows and n columns, n is the lenght of the set of numbers
  for i in range(n):    
    for j in range(n):
  # creates a for loop which will continue for as long as i,j reach n      
      Vm[i][j] = x[i]**j
  # since python indexes start with 0 each element can be to the index's power as for the actual matrix, the x is to the n-1th power    
  return(Vm)

A = Vandermonde(x)

def norm(vector):
  """ This function finds the 2 norm for a given vector. It does this by squaring each value in the list, summing them, and then finally finding the square root of the sum"""
  result = 0
  # initial value for the result of this function
  for z in range(len(vector)):
  # this loop will continue as long as there are more values in the list    
    result += vector[z]**2
  result = result**.5
  # The two equations above find the sum of the squares and then the square root of the squares
  return result

def unit(vector):
  """ This function finds the unit vector, also known as the normalization, of a given vector. It does this by using the the function above to find the 2norm and then dividing each unit in the list by the 2norm"""
  result = [[0] for row in range(len(vector))]
  # creates the initial value for result of this function, which is a vector full of 0s with the same lenght of a given vector 
  for z in range(len(vector)):
  # for loop which continues as long as there are more elements in the vector    
    result[z] = vector[z]/norm(vector)
  # the new result being each element in the list being divided by the norm  
  return result

def subtract(vector01,vector02):
  """ This function finds difference between two vectors, it does this by subtracting each element in the first vector by the corresponding element in the second vector """  
  result = [[0] for row in range(len(vector01))]
  # Creates list full of 0s with the same lenght as vector01
  for z in range(len(vector01)):
  # for loop which continues as long as there are more elements in vector01    
    result[z] = vector01[z]-vector02[z]
  # the subtraction of each element which replaces the corresponding element in the vector full of 0s  
  return result


def scalarmul(scalar,vector):
  """ This function finds the product between a scalar and a vector. It does this by taking the vector and multiplying each element by the scalar"""
  result = [[0] for row in range(len(vector))]
  # creates a list full of 0s with the same lenght of the vector
  for z in range(len(vector)):
  # for loop which continues as long as there are more elements left in the given vector    
    result[z] = scalar*vector[z]
  # the list full of 0s is replaced by the product of each element in the given vector and the the scalar  
  return result  

def dot(vector01,vector02):
    """ This function finds the dot product of two vectors. It does this by multiplying each element in list 1 by the corresponding element in list 2 and summing each of these together"""
    result = 0
    # creates the initial value for the result of the dot product
    for z in range(len(vector01)):
    # for loop which continues as long as there are more values left in the vector    
        result += vector01[z]*vector02[z]
    # the new result is found to be the corresponding values in each vector multiplied and then added together    
    return result

def GramSchmidt(A):
    """ This function finds the QR factorization using the modified gram-schmidt algorithim"""
    n = len(A)
    # Finds the number of lists in the list, which is also the number of rows
    m = len(A[0])
    # Finds the number of elements in list one, which is also the number of columns
    V = A
    R = [[0]*n for i in range(n)]
    # creates an empty list R with dimensions of n rows and n columns
    Q = [[0]*m for i in range(n)]
    # creates an empty list Q with dimensions of n rows and m columns
    inputStatus = True
    # inputStatus is true at this point until proven otherwise
    for i in range(n):
        for j in range(m):
            if ((type(A[i][j]) != int) and (type(A[i][j]) != float) and (type(A[i][j]) != complex)):
                inputStatus = False
                print("Invalid Input")
    # this checks each value in the matrix A to make sure it is some time of number, if it isnt a number then the input status will be false            
    # if the input status is false then an error message will be displayed stating that this is an invalid input
    if inputStatus == True:
    # if the given list does not fall under the previous if statement then the input status will continue to be true and we can continue to find the QR factorization    
        for i in range(n):
    # for loop which continues as long as there are still lists in A        
            R[i][i] = norm(V[i])
    # Creates the border for the upper triangle matrix R, where each value in the diagonal is the 2 norm of the corresponding vector in the original matrix A            
            Q[i] = unit(V[i])
    # Each vector in Q is the unit vector of the corresponding vector in A             
            for j in range(i+1,n):
    # the position j will be 1 more than the position i            
                R[j][i] = dot(Q[i],V[j])
    # The element in R[i+1][i] is the dot product of Q[i] and V[i+1]            
                temp = scalarmul(R[j][i],Q[i])
    # This is the scalar multiplication of R[i+1][i] and Q[i] which will be labeled as temp            
                V[j] = subtract(V[j],temp)
    # V[j] is the difference between the original V[j] and temp            
        return[Q,R]
QR = GramSchmidt(A)
Q = QR[0]
R = QR[1] 

def MatrixVecmul(vector,matrix):
    """This function finds the product between a vector and a matrix by multiplying each row in the matrix by the element in the vector corresponding to the collumn value in the matrix"""    
    n = len(vector)
    m = len(matrix)
    Ax = [[0] for row in range(n)]
    # creates an empty list, which will have the same length as the vector
    a =0
    for i in range(n):
        for j in range(m):
    # for loop that will continue as there are elements left in the vector and rows left in the matrix        
         a += matrix[i][j]*vector[j]    
        Ax[i] = a 
    # each element in the new vector will be equal to the matrix's corresponding row and the sum of each of the collumns in that row times the corresponding value in the vector    
    return(Ax)
Qy = MatrixVecmul(y,Q)

def Backsub(matrix,vector):
    """ This function finds the value of the vector that will be multipied by a matrix which will equal a known vector"""
    C = [[0] for row in range(len(vector))]
    # creates an empty list with the same lenght of the vector
    for i in reversed(range(len(vector))):
    # creates a loop that will continue in reveresd order for as long as there are more elements in the vector    
        C[i] = vector[i]
        for j in range(i+1,len(vector)):
    # for as long as j is in range of i+1 the loop will continue        
            C[i] = C[i] - C[j]*matrix[i][i]
    # each value of C is the difference of the value in the vector minus the next value in the vector times each of the corresponding elements along the diagonal of the matrix        
            C[i] = C[i]/matrix[i][i]
    # the current value of C is divided by the corresponding value along the diagonal of the matrix        
    return C
C = Backsub(R,Qy)
  
            
    
print("The vandermonde matrix A is:")    
print(Vandermonde(x))
print("The QR factorization for matrix A is:")
print(GramSchmidt(A))
print("Q =", Q)
print("R=", R)
print("Q*y=", Qy)
print("The value of C for RC = Q*y is:", Backsub(R,Qy))
print("The polynomial is:",C[0],"x",C[1],"x^2",C[2],"x^3",C[3],"x^4")