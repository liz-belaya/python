def Deduction(q):   # строится массив из x: x=a**2 mod q
    matrix=[]
    for i in range(q):
        matrix.append(i**2%q) # append-добавление в матрицу %-mod
    return(matrix)


def Legandr_symbol(x,q): 
    if x==0:
        return(0)
    elif x in deduction:
        return(1)
    else:
        return(-1)


def matrix_Djecobstola():  
    matrix=[]
    for i in range(q):
        matrix.append([])
        for j in range(q):
            matrix[i].append(Legandr_symbol((j-i)%q,q))
    return(matrix)


def method_Peli():
    matrix=[]
    for i in range(q+1):
        matrix.append([])
        for j in range(q+1):
            if i==0:
                matrix[i].append(1)
            elif j==0:
                matrix[i].append(1)
            elif j==i:
                matrix[i].append(-1)
            else:
                matrix[i].append(Q[i-1][j-1])
    return(matrix)


def method_Silvestor(n,Hn):
    matrix=[]
    for i in range(2*n):
        matrix.append([])
        for j in range(2*n):
            if i>=n and j>=n:
                matrix[i].append(Hn[i%n][j%n]*(-1))
            else:   #  иначе
                matrix[i].append(Hn[i%n][j%n])
    return(matrix)
                
               
def Test_Ferma(q): #тест на простоту 
    for i in range(1,10):
        if q%i!=0:
            mod=i**(q-1)%q
            break
    if mod==1:
        return(True)
    else:
        return(False)
    

def matrix_addition(matrix):# 0 меняем на 1 , -1 меняем на 0
    matrix_add=[]
    for i in range(len(matrix)):
        matrix_add.append([])
        for j in range(len(matrix[i])):
            if matrix[i][j]==1:
                matrix_add[i].append(0)
            else:
                matrix_add[i].append(1)
    return(matrix_add)
            
            
def A_cod(matrix):
    cod=[]
    for i in range(len(matrix)):
        cod.append([])
        for j in range(len(matrix[i])):
            if j!=0: # != не равно
                cod[i].append(matrix[i][j])
    return(cod)


def B_cod(matrix):
    cod=[]
    for i in range(len(matrix)): # len длина
        cod.append([])
        for j in range(len(matrix[i])):
            if j!=0:  
                cod[i].append(matrix[i][j])
    for i in range(len(matrix)):
        cod.append([])
        for j in range(len(matrix[i])):
            if j!=0:
                if matrix[i][j]==1:
                    cod[i+len(matrix)].append(0)
                else:
                    cod[i+len(matrix)].append(1) #append - добавить в матрицу
    return(cod)


def C_cod(matrix):
    cod=[]
    for i in range(len(matrix)):
        cod.append([])
        for j in range(len(matrix[i])):
            cod[i].append(matrix[i][j])
    for i in range(len(matrix)):
        cod.append([])
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                cod[i+len(matrix)].append(1)
            else:
                cod[i+len(matrix)].append(0)
    return(cod)


def binary(x,dlina):#построение двоичных вектров заданной длины (необходимо для проверки на линейность)
    n=''
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    if len(n)<dlina:
        n='0'*(dlina-len(n))+n
    return (n)


def summ_of_vectors(v1,v2): #суммирует два вектора
    summ=[0]*len(v1)
    for i in range(len(v1)):
        summ[i]=(v1[i]+v2[i])%2
    return(summ)


def linearity_check(cod): #проверка на линейность
    for i in range(2**len(cod)-1):
        vector=binary(i,len(cod))
        word=[0]*len(cod[0])
        for j in range(len(vector)):
            if vector[j]=='1':
                word=summ_of_vectors(word,cod[j])
        if word not in cod:
            print('Not lineatrity cod')
            f.write('Нелинейный код'+'\n')
            break
    if math.log2(n)==int(math.log2(n)):
        print('linearity cod')
        f.write('Линейный код'+'\n')
    return(len(cod))


def d_min(cod): #считает мин код расстояние
    d_min=len(cod[0])
    for i in range(len(cod)):
        if cod[i].count(0)!=len(cod[i]):
            d=cod[i].count(1)
            if d<d_min:
                d_min=d
    return(d_min)
                  



import math
f=open('1.txt','w') #имя документа
print('Input n')
n=int(input())
f.write('При n='+str(n)+'\n')
if Test_Ferma(n-1)==True: # если n-1 простое
    f.write('******************************************'+'\n'+
            'Матрица Адамара постороенная методом Пейли'+'\n'+
            '******************************************'+'\n')
    q=n-1
    deduction=Deduction(q) #вычеты
    
    Q=matrix_Djecobstola()
    f.write('Матрица Джекобстола размером '+str(n-1)+'x'+str(n-1)+'\n') #str- превращает число в строку
    for i in range(len(Q)):
        f.write(str(Q[i])+'\n') # f- документ
        print(Q[i])
    H_Peli=method_Peli()
    print('Peli')
    f.write('Матрица Адамара'+'\n')
    for i in range(len(H_Peli)):
        f.write(str(H_Peli[i])+'\n')
        print(H_Peli[i])
    H_Peli=matrix_addition(H_Peli)#addition - дополнение
    A=A_cod(H_Peli)
    B=B_cod(H_Peli)
    C=C_cod(H_Peli)
    print('A')
    f.write('Код А'+'\n')
    for i in range(len(A)):
        f.write( str(A[i])+'\n')
        print(A[i])
    print('Parametrs (n,M,d_min)= (',len(A[0]),',',linearity_check(A),',',d_min(A),')')
    f.write('Параметры кода (n,M,d_min)=('+str(len(A[0]))+','+str(len(A))+','+str(d_min(A))+')'+'\n')
    print('B')
    f.write('Код B'+'\n')
    for i in range(len(B)):
        f.write( str(B[i])+'\n')        
        print(B[i])
    print('Parametrs (n,M,d_min)= (',len(B[0]),',',linearity_check(B),',',d_min(B),')')
    f.write('Параметры кода (n,M,d_min)=('+str(len(B[0]))+','+str(len(B))+','+str(d_min(B))+')'+'\n')
    print('C')
    f.write('Код C'+'\n')
    for i in range(len(C)):
        f.write( str(C[i])+'\n')
        print(C[i])
    print('Parametrs (n,M,d_min)= (',len(C[0]),',',linearity_check(C),',',d_min(C),')')
    f.write('Параметры кода (n,M,d_min)=('+str(len(C[0]))+','+str(len(C))+','+str(d_min(C))+')'+'\n')
else:
    print('We can not construct matrix Adamara with n=',n,'by method Peli')
    f.write('\n'+'Невозможно потроить матрицу Адамара с данными параметрами методом Пейли'+'\n')
if math.log2(n)==int(math.log2(n)): # проверить, что n это 2 в какой-то степени
    f.write('\n'+'******************************************'+'\n'+
            'Матрица Адамара постороенная методом Пейли'+'\n'+
            '******************************************'+'\n')
    H_Silvestor=[[1]]
    n1=1
    while n1!=n:  # выполнять пока n1 не равен n
        H_Silvestor=method_Silvestor(int(n1),H_Silvestor)
        n1*=2
    print('Silvestor')
    
    for i in range(len(H_Silvestor)):
        f.write(str(H_Silvestor[i])+'\n')
        print(H_Silvestor[i])
    H_Silvestor=matrix_addition(H_Silvestor)
    A=A_cod(H_Silvestor)
    B=B_cod(H_Silvestor)
    C=C_cod(H_Silvestor)
    print('A')
    f.write('Код А'+'\n')
    for i in range(len(A)):
        f.write( str(A[i])+'\n')
        print(A[i])
    print('Parametrs (n,M,d_min)= (',len(A[0]),',',linearity_check(A),',',d_min(A),')')
    f.write('Параметры кода (n,M,d_min)=('+str(len(A[0]))+','+str(len(A))+','+str(d_min(A))+')'+'\n')
    print('B')
    f.write('Код B'+'\n')
    for i in range(len(B)):
        f.write( str(B[i])+'\n')
        print(B[i])
    print('Parametrs (n,M,d_min)= (',len(B[0]),',',linearity_check(B),',',d_min(B),')')
    f.write('Параметры кода (n,M,d_min)=('+str(len(B[0]))+','+str(len(B))+','+str(d_min(B))+')'+'\n')
    print('C')
    f.write('Код C'+'\n')
    for i in range(len(C)):
        f.write( str(C[i])+'\n')
        print(C[i])
    print('Parametrs (n,M,d_min)= (',len(C[0]),',',linearity_check(C),',',d_min(C),')')
    f.write('Параметры кода (n,M,d_min)=('+str(len(C[0]))+','+str(len(C))+','+str(d_min(C))+')'+'\n')
else:
    print('We can not construct matrix Adamara with n=',n,'by method Silvestor')
    f.write('\n'+'Невозможно потроить матрицу Адамара с данными параметрами методом Сильвестора'+'\n')
f.close()
