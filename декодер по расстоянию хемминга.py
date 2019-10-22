def transMatrix(matrix):
    matrix_t1=[]
    for i in range(len(matrix[0])):
        matrix_t1.append([0]*len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
             matrix_t1[j][i]=matrix[i][j]
    return matrix_t1

def Cleaning_Zero(matrix,i):
    for m in range(i,n):
        if matrix[i][m]!=0:
            for j in range(n-k):
                matrix[j][i],matrix[j][m]=matrix[j][m],matrix[j][i]
            for l in range(n-k):
                break
    return(matrix)

def Perevod_chisla(chislo,dlina):
    result=''
    while chislo>0:
        y=str(chislo%q)
        result=y+result
        chislo=int(chislo/q)
    if len(result)<dlina:
        O='0'*(dlina-len(result))
        result=O+result
    return(result)

def sysMatrix (matrix):
    if nameMatrix=='G':
        for i in range(k):
            if matrix[i][i]==0:
                for j in range(k):
                    matrix[j][i],matrix[j][i+1]=matrix[j][i+1],matrix[j][i]
            for j in range(q):
                if (matrix[i][i]*j)%q==1:
                    for m in range(n):
                        matrix[i][m]=(matrix[i][m]*j)%q
            for j in range(k):
                if i!=j:
                    while matrix[j][i]!=0:
                        for m in range(n):
                            matrix[j][m]=(matrix[j][m]+matrix[i][m])%q
    else:
        for i in range(n-k):
            if matrix[i][i]==0:
               matrix=Cleaning_Zero(matrix,i)
            for j in range(q):
                 if (matrix[i][i]*j)%q==1:
              #      print('inverse number=',j)
                    for m in range(n):
                        matrix[i][m]=(matrix[i][m]*j)%q
            for j in range(n-k):
                if i!=j:
                     while matrix[j][i]!=0:
                        for m in range(n):
                            matrix[j][m]=(matrix[j][m]+matrix[i][m])%q        
    return(matrix)


def ProMatrix(matrix):
    matrix_P=[]
    H1=[]
    I=[]
   # print('i have started to construct matrix P')
    for i in range(n-k):
        matrix_P.append([0]*k)  
    for i in range(n-k):
        for j in range(n):
            if j>=k-1:
                matrix_P[i][j-k+1]=matrix[i][j]
    for i in range(n-k):
        H1.append([0]*n)
        I.append([0]*(n-k))
    for i in range(n-k):
        for j in range(n-k):
            if i==j:
                I[i][j]=1
    for i in range (n-k):
        H1[i]=matrix_P[i]+I[i]
    print('H_sys')
    for i in range(n-k):
        print(H1[i])
    return(matrix_P)


def G_system(matrix):
    for i in range(n-k):
        for j in range(k):
            P[i][j]=(q-P[i][j])%q
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
    inf_cod=[]
    for i in range(q**k):
        inf_cod.append([0]*n)
    for i in range(q**k):  #перебор все информ слов
        num=Perevod_chisla(i,k)  #
        for j in range(k): #перебор цифр числа перевед в q
            for m in range(n):  #перебор 
                inf_cod[i][m]=(matrix[j][m]*int(num[j])+inf_cod[i][m])%q
    return(inf_cod)


def Weight_of_Word(matrix, word):
    minweight=n
    weight=0
    for i in range(q**k):
        for j in range(n):
            if matrix[i][j]!=word[0][j]:
                weight+=1
        if minweight>weight:
            minweight=weight
            codword=matrix[i]
            infword=Perevod_chisla(i,k)
        weight=0
    #print('Минимальный вес = ',minweight)
    print('Кодовое слово - ', codword)
    print('Информационное слово - ',infword)
        
            



H=[]
G=[]
v=[]
print('Введите размерность поля')
q=int(input())
print('Bведите параметр кода n')
n=int(input())
print('Bведите параметр кода k')
k=int(input())
print ('Введите G, если будете вводить проверочную матрицу. Введите H, если будете вводить порождающую матрицу')
nameMatrix=input().upper()
print('Введите слово, полученное из канала связи')
v.append(list(map(int, input().split())))
print('Введите матрицу', nameMatrix)
if nameMatrix=='G':
    for i in range(k):
        G.append(list(map(int, input().split())))
    Gsys=sysMatrix(G)
    print('Gsys')
    for i in range(k):
        print(Gsys[i])
else:
    for i in range(n-k):
        H.append(list(map(int, input().split())))
    Hsys=sysMatrix(H)
    P=ProMatrix(Hsys)
    print('P')
    for i in range(n-k):
        
        print(P[i])
    Gsys=G_system(P)
    print('Gsys')
    for i in range(k):
        print(Gsys[i])
inf_cod=InfCodWord(Gsys)
print('Все кодовые слова:')
for i in range(q**k):
    print(inf_cod[i])
weight=Weight_of_Word(inf_cod,v)




