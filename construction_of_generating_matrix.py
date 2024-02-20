def matrix_I(matrix):
    I1=[]
    for i in range(k):
        I1.append([0]*k)
    for i in range(k):
        for j in range(k):
            if i==j:
                I1[i][j]=1
    for i in range(k):
        
        Gsys[i]=I1[i]+matrix[i]
    return(I1)


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



def matrix_P(n,k):
    P=[]
    for i in range(k):
        P.append([0]*(n-k))
    for i in range(q**(k*(n-k))):
        vector=Perevod_chisla(i,(k*(n-k)))
        for j in range(n-k):
            for m in range(k):
                P[j][m]=int(vector[(n-k)*j+m])
        print(P)
    return(P)


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


def weight(matrix):
    d=n
    for i in range(q**k):
        if (n-matrix[i].count(0))<d and matrix[i].count(0)!=n:
            d=n-matrix[i].count(0)
            #print('here')
            #print(matrix[i],matrix[i].count(0),d)
        
    return(d)





        
    
                     
        
Gsys=[]        
I=[]
P=[]
d_min=0
d_max=0
print('Введите размерность поля')
q=int(input())
print('Bведите параметр кода n')
n=int(input())
print('Bведите параметр кода k')
k=int(input())
for i in range(k):
    Gsys.append([0]*n)
    I.append([0]*k)
for i in range(k):
    for j in range(k):
        if i==j:
            I[i][j]=1
for i in range(k):
    P.append([0]*(n-k))
    print(P)
for i in range(q**(k*(n-k))):
    vector=Perevod_chisla(i,(k*(n-k)))
    for j in range(k):
        for m in range(n-k):
            P[j][m]=int(vector[(n-k)*j+m])
    #print('Gsys')
    for l in range(k):
        Gsys[l]=I[l]+P[l]
     #   print(Gsys[l])
    words=InfCodWord(Gsys)
    #print('words')
    #for l in range(q**k):
     #   print(words[l])
    
    d_min=weight(words)
    #print(d_min)
    if d_min>d_max:
        d_max=d_min
        best=vector
#print('best',best)
for j in range(k):
    for m in range(n-k):
        P[j][m]=int(best[(n-k)*j+m])
print('The best Gsys')
for l in range(k):
    Gsys[l]=I[l]+P[l]
    print(Gsys[l])

        
    


