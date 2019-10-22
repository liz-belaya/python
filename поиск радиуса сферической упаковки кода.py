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
            #print('I am here', i,matrix)
            if matrix[i][i]==0:
                matrix=Cleaning_Zero(matrix,i)
            for j in range(q):
                 if (matrix[i][i]*j)%q==1:
                   # print('I have founded q')
                    for m in range(n):
                        matrix[i][m]=(matrix[i][m]*j)%q
            for j in range(n-k):
                if i!=j:
                     while matrix[j][i]!=0:
                        for m in range(n):
                            matrix[j][m]=(matrix[j][m]+matrix[i][m])%q        
    return(matrix)


def Cleaning_Zero(matrix,i):
    #print('i=',i)
    for m in range(i,n):
     #   print('m=',m)
        if matrix[i][m]!=0:
      #      print('Position ',m,'without zero')
            for j in range(n-k):
                matrix[j][i],matrix[j][m]=matrix[j][m],matrix[j][i]
            for l in range(n-k):
                
                #print(matrix[l])
                break
    #print('!!!',matrix)
        
    return(matrix)
            
    
    
    


def ProMatrix(matrix):
    matrix_P=[]
    H1=[]
    I=[]
    #print('i have started to construct matrix P')
    for i in range(n-k):
        matrix_P.append([0]*k)  
    for i in range(n-k):
     #   print('i=',i)
        for j in range(n):
      #      print('j=',j)
            if j>=k-1:
       #         print('H[',i,'][',j,']=',matrix[i][j])
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



def transMatrix(matrix):
    matrix_t1=[]
    for i in range(len(matrix[0])):
        matrix_t1.append([0]*len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
             matrix_t1[j][i]=matrix[i][j]
    return matrix_t1


def InfCodWord(matrix):
    inf_cod=[]
    for i in range(q**k):
        inf_cod.append([0]*n)
    for i in range(q**k):  #перебор все информ слов
        num=Perevod_chisla(i,k)  #
        for j in range(k): #перебор цифр числа перевед в q
            for m in range(n):  #перебор 
                #print('num[j]',num[j])
                inf_cod[i][m]=(matrix[j][m]*int(num[j])+inf_cod[i][m])%q
    return(inf_cod)

def Min_Weight(matrix):
    minweight=n
    weight=0
    for i in range(q**k):#sort out all cod words
        for j in range(n):#sort out all numbers of cod word
            if matrix[i][j]!=0:
                weight+=1
        if minweight>weight and weight!=0:
            minweight=weight
        weight=0
    print('Минимальный вес =',minweight)
    return(minweight)



def Cover_of_cod(matrix):
    minweight=n
    radius=0
    for i in range(q**n):#sort out all vectors
        weight=0
        num=Perevod_chisla(i,n)#image numbers from 0 to q**n  
        for m in range(q**k):#sort out all cod words
            vector=''
            for j in range(n):
                vector=vector+str(matrix[m][j])
            if vector!=num:
                for j in range(n):
                    if vector[j]!=num[j]:
                        weight+=1
                if weight<minweight:
                    minweight=weight
        #            print(minweight,'minw i=',i,'m=',m)
         ##           print('vector',vector)
           #         print('word',num)
            else:
                break
            
            if minweight>radius and minweight!=n:
                radius=minweight
                print(radius,'R i=',i,'m=',m)
    return(radius)


H=[]
G=[]
print('Введите размерность поля')
q=int(input())
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
    Gsys=sysMatrix(G)
    print('Gsys',Gsys)
else:
    for i in range(n-k):
        H.append(list(map(int, input().split())))
    #print(' i am here')
    Hsys=sysMatrix(H)
    #print('Hsys')
    #for i in range(n-k):
        
     #   print(Hsys[i])
    P=ProMatrix(Hsys)
    print('P')
    for i in range(n-k):
        
        print(P[i])
    Gsys=G_system(P)
    print('Gsys',Gsys)
inf_cod=InfCodWord(Gsys)
print('Все кодовые слова:')
for i in range(q**k):
    print(inf_cod[i])
d_min=Min_Weight(inf_cod)
r=int((d_min-1)/2)
print('Радиус сферической упаковки кода =',r)
R=Cover_of_cod(inf_cod)
print('Радиус покрытия кода =',R) 
