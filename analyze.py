from tkinter import *
from tkinter import filedialog as fd
import numpy as np
import random


def sigmoid(x):
    """сигмоидальная функция, работает и с числами, и с векторами (поэлементно)"""
    return 1 / (1 + np.exp(-x))

def sigmoid_prime(x):
    """производная сигмоидальной функции, работает и с числами, и с векторами (поэлементно)"""
    return sigmoid(x) * (1 - sigmoid(x))

def ExsamplesCreator():
   # text.insert('end','Процесс обучения нейронной сети...')
    f=open(text1.get())
    mass=f.readlines()
   # wordText=''
    mass = [line.rstrip() for line in mass]
    exsamples=[]
  
    answerOfExsamples=[]
    for i in range(len(mass)):
        exsamples.append([])
        answerOfExsamples.append([])                 
        answerOfExsamples[i].append(int(mass[i][-2]))
        mass[i]=mass[i][1:-4]
        for j in range(0,len(mass[i]),2):
            exsamples[i].append(int(mass[i][j]))
    exsamples=np.array(exsamples)
    answerOfExsamples=np.array(answerOfExsamples)
    print(answerOfExsamples)
    print(exsamples)
    return(exsamples, answerOfExsamples)



def WeightCreator():
    W1=[]
    W2=[]
    bians1=[]
    bians2=[]
    for i in range(64):
        W1.append([])
        for j in range(8):
            W1[i].append(round(random.uniform(-0.5,0.5),3))
    #    print(W[0][i])
    W2.append([])
    bians1.append([])
    for i in range(64):
        W2[0].append(round(random.uniform(-0.5,0.5),3))
        bians1[0].append(round(random.uniform(-0.5,0.5),3))
    bians2.append(round(random.uniform(-0.5,0.5),3))
    bians1=np.array(bians1)
    bians2=np.array(bians2)
    W1=np.array(W1)
    W2=np.array(W2)
   # print(W1,W2)
    return(W1,W2,bians1,bians2)

def LearningFirstLayer(exsample,W1,bians1):
    summator=exsample.dot(W1.T)+bians1[0]
   # print(summator)
    active=sigmoid(summator)
   # print(active)
    return(active,summator)

def LearningSecondLayer(active,W2,bians2):
    summator=active.dot(W2.T)+bians2[0]
    #print(summator)
    answer=sigmoid(summator)
   # print('ans',answer)
    return(answer,summator)

def ErrorCorrection(d,W2):
    D2=d*W2
   # print('W2',W2)
#    print(W2.shape)
    return(D2)

def WeightCorrection(vector,W1,W2,
                     bians1,bians2,
                     D2,summatorFunction,
                     summatorFunction2,
                     activeFunction,d):
    #print('len',len(W1))
    for i in range(len(W1)):
     #   print('len',len(W1))
      #  input()
        bians1[0][i]=bians1[0][i]+D2[0][i]*sigmoid_prime(summatorFunction[i])*a
        for j in range(len(W1[i])):
            W1[i][j]=W1[i][j]+D2[0][i]*sigmoid_prime(summatorFunction[i])*vector[j]*a  #x
    for i in range(len(W2[0])):
        W2[0][i]=W2[0][i]+d*sigmoid_prime(summatorFunction2[0])*activeFunction[i]*a
    bians2[0]=bians2[0]+d*sigmoid_prime(summatorFunction2[0])*a
    return(W1,W2,bians1,bians2)
    



def ButtonLearn():
   # text.insert('end','Процесс обучения нейронной сети...')
    findWord='password'        
    a=0.1
    exsamples,answerOfExsamples = ExsamplesCreator()
    #print(exsamples,answerOfExsamples)
    W1,W2,bians1,bians2 = WeightCreator()
    #print('bians',bians2)

    #input()
   # text.insert('end','Процесс обучения нейронной сети...')
    for j in range(1000):
        print(j)
        for i in range(len(exsamples)):
        
            activeFunction,summatorFunction = LearningFirstLayer(exsamples[i],
                                                                 W1,bians1)
            answerOfNet,summatorFunction2 = LearningSecondLayer(activeFunction,
                                                                W2,bians2)
            d = answerOfExsamples[i]-answerOfNet
            D2 = ErrorCorrection(d,W2)

   # print('D2',D2)
    #print(D2.shape)
   # print(W1)
            W1,W2,bians1,bians2=WeightCorrection(exsamples[i],W1,W2,
                                                 bians1,bians2,D2,
                                                 summatorFunction,
                                                 summatorFunction2,
                                                 activeFunction,d)
    text.insert('end','Искусственная нейронная сеть успешно обучена \n')
   # print(W1)


def similar(text):
    #if not len(first) == len(second):
     #   return False
    word='password' 
    mass=[]
    for i in range(len(text)-len(word)):
        find=text[i:i+len(word)]
       # print(find)
        if len(find) - sum(l1==l2 for l1, l2 in zip(find, word)) < 5:
            #return False
            mass.append(text[i:i+len(word)])
    return (mass)

def ButtonAnalyze():
    f=open(text2.get(), encoding="utf-8")
    f=f.readlines()
    codeText=''
    for i in range(len(f)):
        codeText+=f[i]
    #print(text)
    word='password'
#mass=[]
#for i in range(len(f)-len(word)):
    
 #   mass.append(similar(f[i:i+len(word)]
    
#print(f)
    massOfSimilarWords=similar(codeText)
    

    print(massOfSimilarWords)
    
    analyzingVector=[]
    for i in range(len(massOfSimilarWords)):
        analyzingVector.append([])
        print(massOfSimilarWords[i])
        for  j in range(len(massOfSimilarWords[i])):
           # print(massOfSimilarWords[i])
            if massOfSimilarWords[i][j]==word[j]:
               # print(massOfSimilarWords[i][j],word[i])
                analyzingVector[i].append(1)
            else:
                #print(massOfSimilarWords[i][j],word[i])
                analyzingVector[i].append(0)
    analyzingVector=np.array(analyzingVector)
    print(analyzingVector)
    for i in range(len(analyzingVector)):
        activeFunction,summatorFunction = LearningFirstLayer(analyzingVector[0])
        answerOfNet,summatorFunction2 = LearningSecondLayer(activeFunction)
        print(answerOfNet)
        
        
    
 
def insertText1():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert('end','Обучающая выборка:\n')
    text.insert('end', file_name+'\n')
   # text.insert(1.0, s)
    text1.insert(0,file_name)
    f.close()

def insertText2():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    text.insert('end','Анализируемый код: \n')
    text.insert('end', file_name + '\n')
    text2.insert(0,file_name)
    f.close()


findWord='password'        
a=0.1 
root = Tk()
root.geometry('400x400+360+200')
root.title('Text Generation')
text = Text(width=45, height=15)
text.place(x=10,y=130)
scroll = Scrollbar(command=text.yview)
scroll.place(x=370, y=130)
text.config(yscrollcommand=scroll.set)
label1=Label(root,width=17, height=2,text='Обучающая выборка')
text1=Entry(root,bd=5,width=25)
text1.place(x=10,y=30)
label1.place(x=8,y=4)
label2=Label(root,width=13, height=2,text='Код программы')
label2.place(x=8, y=65)
text2=Entry(root,bd=5,width=25)
text2.place(x=10, y = 90)
b1 = Button(text="...", command=insertText1)
b1.place(x=180, y=30)
b2 = Button(text="...", command=insertText2)
b2.place(x=180, y=90)
button1=Button(text= 'LEARN',width=10, command=ButtonLearn)
button1.place(x=230, y=30)
button2=Button(text="ANALYZE", width=10, command=ButtonAnalyze)
button2.place(x=230, y=90)
root.mainloop()
