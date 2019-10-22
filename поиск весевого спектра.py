def transMatrix(matrix):
    matrix_t1=[]
    for i in range(len(matrix[0])):
        matrix_t1.append([0]*len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
             matrix_t1[j][i]=matrix[i][j]
    return matrix_t1


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
    matrix_P=[]
    for i in range(n-k):
        matrix_P.append([0]*k)
    for i in range(n-k):
        for j in range(n):
            if j<(k):
                matrix_P[i][j]=matrix[i][j]
    return(matrix_P)

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

def spector(matrix):
    sp1=[]
    sp1.append([0]*(n+1))
    for i in range((n+1)):
        for j in range(2**k):
            if matrix[j].count(1)==i:
                sp1[0][i]=sp1[0][i]+1
    return(sp1)
                



sp=[]
H=[]
G=[]
inf_cod=[]
print('Bведите параметр кода n')
n=int(input())
print('Bведите параметр кода k')
k=int(input())
print ('Введите G, если будете вводить проверочную матрицу. Введите H, если будете вводить порождающую матрицу')
nameMatrix=input().upper()
print('Введите матрицу', nameMatrix)
if nameMatrix=='G':
    for i in range(k):
        G.append(list(map(int, input().split())))          
else:
    for i in range(n-k):
        H.append(list(map(int, input().split())))
    H_sys=sysMatrixH(H)
    print('H_sys',H_sys)
    P=ProMatrix(H_sys)
    G=sysG(P)
    print('G_sys',G)
inf_cod=InfCodWord(G)
print('inf_cod',inf_cod)
sp=spector(inf_cod)
for i in range((n+1)):
    print('Количество векторов веса', i,'-',sp[0][i])

    
