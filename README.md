# NPETL
NPETL Week 3 Programming Assignment (ANSWER) 2023


1).Write a function expanding(l) that takes as input a list of integer l and returns True if the absolute difference between each adjacent pair of elements strictly increases.


def expanding(lst):
   list1=[]
   for i in range(len(lst)):
     for j in range(i+1,len(lst)):
       if lst[i]>lst[j]:
         list1.append(lst[i]-lst[j])
         break
       elif lst[j]>lst[i]:
         list1.append(lst[j]-lst[i])
         break
       else:
         pass
  flag=1
  a=0
  for k in list1:

    if a<k:
      flag=1
      a=k
    else:
      flag=2
      break

  if flag==1:
    return True
  else:
    return False

2) Write a Python function sumsquare(l) that takes a nonempty list of integers and returns a list [odd,even], where odd is the sum of squares all the odd numbers in l and even is the sum of squares of all the even numbers in l.

def sumsquare(l):
  sum_odd = sum([num ** 2 for num in l if num % 2 != 0])
  sum_even = sum([num ** 2 for num in l if num % 2 == 0])
  return [sum_odd, sum_even]


    
3)A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix. For instance, the matrix



def transpose(matrix):
    if isinstance(matrix[0], list): 
        if isinstance(matrix[0][0], list):  
            dim1 = len(matrix)
            dim2 = len(matrix[0])
            dim3 = len(matrix[0][0])

            transposed = [[[0 for _ in range(dim1)] for _ in range(dim2)] for _ in range(dim3)]
            print(transposed)
            for i in range(dim1):
                for j in range(dim2):
                    for k in range(dim3):
                        transposed[k][i][j] = matrix[i][j][k]

            return transposed
        else:  # It's a 2D matrix
            rows = len(matrix)
            columns = len(matrix[0])

            transposed = [[0 for _ in range(rows)] for _ in range(columns)]
            
            for i in range(rows):
                for j in range(columns):
                    transposed[j][i] = matrix[i][j]

            return transposed
    else:  
        return matrix  
