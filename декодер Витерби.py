def Distance_of_Hemming(vector1,vector2):
    d=0
    for i in range(len(vector1)):
        if vector1[i]!=vector2[i]:
            d+=1
    return(d)

def Inform_word(matrix):
    word=''
    way=Right_way(matrix)
    for i in range(len(way)):
        if i%K==0:
            word=word+way[i]
    return(word)    




def Right_way(matrix):
    right=len(matrix[0][1])
    for i in range(2**K):
        if right>int(matrix[i][2]):
              right=int(matrix[i][2])
              way=matrix[i][0]
    print(way)
    return(way)


def Coding(vector,polinom):#coding of iformation word from link
    sost='0'*K ##'000'
    znach=''
    vec=''
    for i in range(len(vector[0][0])):
        sost=vector[0][0][i]+sost
        sost=sost[:-1]
        #print('sost',sost)
        for j in range(n):
            for m in range(K):
                if polinom[j][m]==1:
                    znach=znach+sost[m]
            vec=vec+str(znach.count('1')%2)
            znach=''
    return(vec)


def Ways_of_Conditions(matrix,vector):
    #print('len(matrix[0][0]',len(matrix[0][0]),'len matrix[0][1]',len(matrix[0][1]))
    for i in range(2**K):
        matrix[i][1]=''
        for j in range(int(len(matrix[0][0])/K)):
            sost=matrix[i][0][3*j:3*j+K]
            #print(sost,'sost')
            num=int(sost,2)
            for m in range(n):
                cond=str(conditions[num][m])
                matrix[i][1]=matrix[i][1]+cond
                cond=''
        matrix[i][2]=Distance_of_Hemming(vector[0][:len(matrix[i][1])],matrix[i][1])
    return(matrix)


def Conditions_def(polinom,matrix):
    cond=''
    for i in range(2**K):     #sort out all registrs`s conditions
        znach=dvoichnoe_chislo(i,K)
        for j in range(n):   #sort out all polinoms
            for m in range(K):  #sort out polinom j
                if polinom[j][m]==1:
                    cond=cond+str(znach[m])
            matrix[i][j]=cond.count('1')%2
            cond=''
    return(matrix)


def Survided_Ways(matrix):
    standard=len(matrix[0][0])
    for i in range(2**K):
        for j in range(2**K):
           # print('i=',i,'j=',j)
            if matrix[i][0][-3:-1]==matrix[j][0][-3:-1] and matrix[i][0]!=matrix[j][0]:
                if len(matrix[i][0])==standard and len(matrix[j][0])==standard:
                    #print('matrix[',i,']=',matrix[i][0][-3:-1],'matrix[',j,']=',matrix[j][0][-3:-1])
                    if matrix[i][2]>matrix[j][2]:
                        matrix[i][0]=matrix[j][0]+'0'+matrix[j][0][-3:-1]
                        matrix[j][0]=matrix[j][0]+'1'+matrix[j][0][-3:-1]
                    else:
                        matrix[j][0]=matrix[i][0]+'0'+matrix[i][0][-3:-1]
                        matrix[i][0]=matrix[i][0]+'1'+matrix[i][0][-3:-1]
                #break
    return(matrix)


def Noisiness(vector,error):
    for i in range(error):
        position=random.randint(0,len(vector))
        if vector[position]=='1':
            vector=vector[:position]+'0'+vector[position+1:]
        else:
            vector=vector[:position]+'1'+vector[position+1:]
    return(vector)
                
                        


def State_of_Registrs(matrix):#build 2**(K-1) ways with different states of registrs  
    for i in range(2**K):
        znach=dvoichnoe_chislo(i,K)
        sost='0'*K
        for j in range(K):
            sost=znach[j]+sost
            sost=sost[:-1]
            matrix[i][0]=matrix[i][0]+sost
    return(matrix)


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





inform=[]
v1=[]
v=[]
g=[]
conditions=[]
ways=[]
inform.append([''])
print('Введите название файла')
name=input()
myfile=open(name,"rb")
data=myfile.readlines()
for i in range(len(data)):
    for j in range(len(data[i])):
        a='{0:b}'.format(data[i][j])
        if len(a)<8:
            O='0'*(8-len(a))
            a=O+a
        inform[0][0]=inform[0][0]+a
inform[0][0]=inform[0][0][:-8]
print('inform',inform)
v1.append([''])
v.append([''])
print('Введите кодовое ограничение К')
K=int(input())
print('Введите 2, если скорость кода=1/2')
print('Введите 3, если скорость кода=1/3')
n=int(input())
for i in range (n):
    print('Введите коэффициенты x^0... x^',K-1,' полинома g',i+1,'(x)')
    g.append(list(map(int, input().split())))
v1[0]=Coding(inform,g)
print('v1',v1)
print(len(v1))
print('Введите количество ошибок')
percent=int(input())
import random
v[0]=Noisiness(v1[0],percent)
print(v)
    
for i in range(2**K):
    conditions.append([0]*n)
    ways.append(['']*3)
ways=State_of_Registrs(ways)
conditions=Conditions_def(g,conditions)
ways=Ways_of_Conditions(ways,v)
#for i in range(len(ways)):
 #   print(ways[i])
#print('lenv[0]=',len(v[0]))
for I in range (int((len(v[0])-K*n)/n)):
    ways=Survided_Ways(ways)
    #for i in range(2**K):
     #   print(ways[i])
    ways=Ways_of_Conditions(ways,v)
    #for i in range(2**K):
     #   print(ways[i])
word=Inform_word(ways)
print(word)
f=open('decoding.txt','w')
for i in range(int(len(word)/8)):
    buk=int(word[i*8:i*8+8],2)
    f.write(chr(buk))
f.close()

        
    
    

    

