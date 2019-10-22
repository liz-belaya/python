def transMatrix(matrix):
    matrix_t1=[]
    for i in range(len(matrix[0])):
        matrix_t1.append([0]*len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
             matrix_t1[j][i]=matrix[i][j]
    return matrix_t1

def sysMatrixG(matrix):
    matrix_t = transMatrix(matrix)
    for i in range(k):
        for j in range(n):
            if matrix_t[j][i]==1 and matrix_t[j].count(0)==k-1: 
                for m in range(k):
                    matrix_t[j][m],matrix_t[i][m]=matrix_t[i][m],matrix_t[j][m]
                break
    matrix=transMatrix(matrix_t)#G
    return matrix #G

def sysMatrixH(matrix):
    matrix_t = transMatrix(matrix)
    print('t',matrix_t)
    for i in range (n-k):#место на котором должна быть 1
        for j in range(n):#перебираем строки в транс матрице
            if matrix_t[j][i]==1 and matrix_t[j].count(0)==n-k-1:
                for m in range(n-k):
                    matrix_t[j][m],matrix_t[i+k][m]=matrix_t[i+k][m],matrix_t[j][m]#i+n-k
                break
            
    matrix=transMatrix(matrix_t)
    return matrix


def ProMatrix(matrix):
    if nameMatrix=='G':
        matrix_P=[]
        for i in range(k):
            matrix_P.append([0]*(n-k))
        for i in range(k):
            for j in range(n):
                if j>=k:
                    matrix_P[i][j-k]=matrix[i][j] #G
    else:
        matrix_P=[]
        for i in range(n-k):
            matrix_P.append([0]*k)
        
        for i in range(n-k):
            for j in range(n):
                if j<(k):
                    matrix_P[i][j]=matrix[i][j]
    return(matrix_P)

def sysH(matrix):
    P_t=transMatrix(P)
    H1=[]
    I=[]
    for i in range(n-k):
        H1.append([0]*n)
        I.append([0]*(n-k))
    for i in range(n-k):
        for j in range(n-k):
            if i==j:
                I[i][j]=1
    for i in range(n-k):
        H1[i]=P_t[i]+I[i]
    return(H1)

def sysG(matrix):
    P_t=transMatrix(P)
    G1=[]
    I=[]
    for i in range(k):
        G1.append([0]*n)
        I.append([0]*k)
    for i in range(k):
        for j in range(k):
            if i==j:
                I[i][j]=1
    for i in  range(k):
        G1[i]=I[i]+P_t[i]
    return(G1)
        
    
def InfCodWord(matrix):
    for i in range(2**k):
        inf_cod.append([0]*n)
    for i in range(2**k):
        num=dvoichnoe_chislo(i,k)
        for j in range(k):
            if num[j]=='1':
                for m in range(len(matrix[0])):
                    inf_cod[i][m]=inf_cod[i][m]^matrix[j][m]
    return(inf_cod)

def Sindrom(vector):
    H_t=transMatrix(H_sys)
    s.append([0]*(n-k))
    for i in range(n):
        if vector[0][i]==1:
            for j in range(n-k):
                s[0][j]=s[0][j]^H_t[i][j]
    return(s)

def ErorVector(sindrom):
    H_t=transMatrix(H_sys)
    e.append([0]*n)
    s1=[]
    s1.append([0]*(n-k))
   # print('s1',s1)
    for i in range(n):
        for j in range(2**n):
            num=dvoichnoe_chislo(j,n)
            if num.count('1')==i:
                for l in range(n):
                    if num[l]=='1':
                        for m in range(n-k):
                            #print('H_t',H_t,'s1', s1)
                            s1[0][m]=s1[0][m]^H_t[l][m]
            if s1==s:
                if num.count('0')<n:
                    num1=num
                break
            else:
                s1=[[0]*(n-k)]
    return(num1)


def dvoichnoe_chislo(num,dlina):
    dva=''
    while num>0:
        y=str(num%2)
        dva=y+dva
        num=int(num/2)
    if len(dva)<dlina:
        O='0'*(dlina-len(dva))
        dva=O+dva
    return(dva)
    

                

e=[]    
s=[]
q=2
H=[]
G=[]
a=[] #???
inf_cod=[]
matrix_t=[]
v=[]
v1=[]
eror=[]
print('Bведите параметр кода n')
n=int(input())
print('Bведите параметр кода k')
k=int(input())
print ('Введите G, если будете вводить проверочную матрицу. Введите H, если будете вводить порождающую матрицу')
nameMatrix=input().upper()
print('Введите слово, полученное из канала связи')
v.append(list(map(int, input().split())))
v1.append([0]*n)

print('Введите матрицу', nameMatrix)
if nameMatrix=='G':
    for i in range(k):
        G.append(list(map(int, input().split())))
    G_sys=sysMatrixG(G)
    print('G_sys')
    for i in range(len(G_sys)):
        print(G_sys[i])
    P=ProMatrix(G_sys)
    print('ProMatrix')
    for i in range(len(P)):  
        print(P[i])
    H_sys=sysH(P)
    print('H_sys')
    for i in range(len(H_sys)):
        print(H_sys[i])
    inf_cod=InfCodWord(G_sys)
    print('inform words')
    for i in range(len(inf_cod)):
        print(inf_cod[i])
else:
    for i in range(n-k):
        H.append(list(map(int, input().split())))
    H_sys=sysMatrixH(H)
    print('H_sys')
    for i in range(len(H_sys)):
        print(H_sys[i])
    P=ProMatrix(H_sys)
    G_sys=sysG(P)
    print('G_sys')
    for i in range(len(G_sys)):    
        print(G_sys[i])
    print('ProMatrix')
    for i in range(len(P)):
        print(P[i])
    print('H_sys')
    for i in range(len(H_sys)):
        print(H_sys[i])
    inf_cod=InfCodWord(G_sys)
    print('inform words')
    for i in range(len(inf_cod)):
        print(inf_cod[i])
s=Sindrom(v)
print('s',s)
if s[0].count(0)==n-k:
    for i in range(2**k):
        if inf_cod[i]==v[0]:
            inf=i
            print(i)
else:
    e=ErorVector(s)
    print('e',e)
    for i in range(n):
        v1[0][i]=v[0][i]^(int(e[i]))
    print('v1',v1)
    for i in range(2**k):
        if inf_cod[i]==v1[0]:
            inf=i
print('Исходгое информационное слово', dvoichnoe_chislo(inf,k))
        



