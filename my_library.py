# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# FACTORIAL FUNCTION
# ASSIGNMENT 1
# %%
def factorial(n):
    fact = 1
    i = 1
    while i < n+1:
        fact = fact*i
        i = i+1
    return fact    


# %%

## Assingment 3
'''
#A function to read the data from the files to obtain the matrix
#The file must be created in the following format, 
    #only one row must be written in a line, with elements separated by commas,
    #no comma is allowed to be placed at the end of a line except when the line describes the last row
    #Comma at the end of the last row is necessary
    #[1 0 0] is entered as 1,0,0
     [0 1 0]               0,1,0 <-note the absence of comma
     [0 0 1]               0,0,1,<- note this comma
    #
'''
# READ WRITE

def read_matrix(file_name):
    file=open(str(file_name),"r")
    M=[[]]
    temp=''
    i=0
#what follows below is a just accessing the strings one by one, and and converting the file data to list
#of lists format
    for j in file:
        for k in j:
            if k=='\n':
                M[i]+=[int(temp)]
                temp=''
                i+=1
                M+=[[]]
            elif k!=',' and k!='\n':
                temp+=k
            elif k==',' or k=='':
                M[i]+=[int(temp)]
                temp=''
    return(M)



'''
#Creating a matrix class that will facilitate the handling of matrices of any dimension
The matrix class will take input in list of lists format, e.g., the matrix 
[1 0 0] will be entered as [[1,0,0],[0,1,0],[0,0,1]]
[0 1 0]
[0 0 1]
'''
class Matrix:
    def __init__(self,list_of_lists):
        for i in range(len(list_of_lists)):
            if len(list_of_lists[i]) != len(list_of_lists[0]): #It must be a matrix afterall
                print("undefined matrix")
        self.lol=list_of_lists
    def show(self):#Method to display the matrix appropriately
        for i in self.lol:
            for j in i:
                print(str(j)+str(','),end='')
            print("\n")
    def Transpose(self):#Method defining the Transpose of a matrix
        C=[]
        for _ in range(len(self.lol[0])):#Inverting the number of rows and columns
            C+=[[]]
        for i in range(len(self.lol)):
            for j in range(len(self.lol[i])):#appending the rows as columns
                C[j].append(self.lol[i][j])
        return(Matrix(C))
def Mat_product(X,Y,show=True):
    if isinstance(X,Matrix) == True and isinstance(Y,Matrix) ==True:
#Just a check to see if the matrices can be actually be multiplied
        if len(X.lol[0])!=len(Y.lol):
            print('Product not defined')
        else:
            m=len(X.lol)
            n=len(Y.lol[0])
            Z=[]
            for _ in range(m):#creating the new matrix
                Z+=[[]]
            for i in range(len(X.lol)):#populating the entries of the new matrix
                temp=0
#The next three lines multiply the necessary elements to find the i,l th element of the new matrix
                for l in range(len(Y.lol[0])):
                    for j in range(len(X.lol[i])):
                        temp+=X.lol[i][j]*Y.lol[j][l]
                    Z[i].append(temp)
                    temp=0
            if show==True:
                Matrix(Z).show()
            return(Matrix(Z))
    else:
        print("Not a matrix")



'''
A function to multiply a factor 'fact' to the Rth row(i.e., perform the operation: R-->R*fact)
'''
def multRow(lst_of_lsts,R,fact):
    for i in range(len(lst_of_lsts[R])):
        lst_of_lsts[R][i]=lst_of_lsts[R][i]*fact
'''
A function to multiply a factor 'fact' to each element of the R2th row and replace each element of R1th row 
with the sum of both.(i.e., perform the operation: R1-->R1+R2*fact)
'''
def rowAdd(lst_of_lsts,R1,R2,fact=1):
    for i in range(len(lst_of_lsts[R2])):
        lst_of_lsts[R1][i]+=fact*lst_of_lsts[R2][i]

'''
Find the maximum value of all the elements in a matrix
'''
def maxVal(lst_of_lsts):
    temp=lst_of_lsts[0][0]
    for i in lst_of_lsts:
        for j in i:
            if j>temp:
                temp=j
    return(temp)

'''
This function carries out the partial pivot operation, it takes the list of lists as input and carries out 
partial pivot about the pivot number supplied. As instructed in class, all elements that are less than two
orders of magnitude smaller than the maximum element are counted as zero.
'''
def partialPivot(lst_of_lsts,pivnum):
    piv=lst_of_lsts[pivnum][pivnum]#selecting the pivot
    m=len(lst_of_lsts)             #number of rows
    n=len(lst_of_lsts[0])          #number of columns
    mx=maxVal(lst_of_lsts)         #max value in the matrix
    swp_nos=0
    if abs(piv/mx)>10**(-2):       #If pivot not required then return the number of swaps
        return(swp_nos)
    else:
        swp_nos+=1                 #If pivot required, increment the number of swaps done
        swap_row_ind=pivnum        #This is the index of the row with which we will swap
        for i in range(pivnum,m):  #searching the row with largest swappable element
            if lst_of_lsts[i][pivnum]>lst_of_lsts[swap_row_ind][pivnum]:
                swap_row_ind=i
        if abs(lst_of_lsts[swap_row_ind][pivnum]/mx)<10**(-2): #if no swappable element found in any row
            return("Unswappable zero pivot reached!")        #message indicating that partial pivot not possible
        lst_of_lsts[pivnum],lst_of_lsts[swap_row_ind]=lst_of_lsts[swap_row_ind],lst_of_lsts[pivnum]
        return(swp_nos)            #return the number of swaps done



'''
Defining a function that will take an augmented matrix object, perform the Gauss jordan and return the 
Row reduced echelon matrix
'''
def GaussJordan(mtrx):
    lst_of_lsts=mtrx.lol
    m=len(lst_of_lsts)   #number of rows
    n=len(lst_of_lsts[0])#number of columns
    for i in range(m):   #Looping through all rows
        partialPivot(lst_of_lsts,i) #Partial pivoting if required
        if partialPivot(lst_of_lsts,i)=="Unswappable zero pivot reached!":
            return("Unswappable zero pivot reached!") #In case Gauss Jordan is not possible
        multRow(lst_of_lsts,i,1/lst_of_lsts[i][i])    
        for j in range(m):  #eliminating all elements in the column except the pivot
            if j!=i:
                rowAdd(lst_of_lsts,j,i,-lst_of_lsts[j][i])

'''
A function that takes in the Augmented matrix and returs the inverse.
Note: It does not return the augmented matrix but only the inverse
'''

def inverse(mtrx):
    lst_of_lsts=mtrx.lol
    m=len(lst_of_lsts)   #number of rows
    n=len(lst_of_lsts[0])#number of columns
    det_check=GaussJordan(mtrx)
    if det_check=="Unswappable zero pivot reached!": #if partial pivot not possible, inverse does not exist
        return('Inverse does not exist')
    else:
    #extract the inverse from the reduced row echelon matrix
        C=[]
        for i in range(m):
            C+=[lst_of_lsts[i][m:]]
        return(Matrix(C))
        


'''
A function that calculates the determinant of a square matrix
'''

def Determinant(mtrx):
    lst_of_lsts=mtrx.lol
    m=len(lst_of_lsts)   #number of rows
    n=len(lst_of_lsts[0])#number of columns
    if m!=n:
        return("Determinant does not exist")
    swp_nos=0                                    #A counter that keeps track of total number of swaps
    for i in range(m):   
        pP=partialPivot(lst_of_lsts,i)
        if pP=="Unswappable zero pivot reached!":#In case partial pivoting is not possible, determinant is 0
            return(0)
        swp_nos+=pP                              #counting the total number of partial pivots done
        for j in range(i+1,m):             #eliminating all the elements in the pivoting column below the pivot
            rowAdd(lst_of_lsts,j,i,-lst_of_lsts[j][i]/lst_of_lsts[i][i])
    val=1
    for pivnum in range(m):
        val*=lst_of_lsts[pivnum][pivnum]
    return((-1)**(swp_nos)*val)





