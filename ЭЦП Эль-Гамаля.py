def NOD(a,b):
    while a!=0 and b!=0:
        if a>b:
            a=a%b
        else:
            b=b%a
    return(max(a,b))

def primitive_root(modulo):
    required_set = set(num for num in range (1, modulo) if NOD(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            g1=g
            break
    return(g1)


def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1
 
    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return r

def Invert_number(num,modul):
    inv=1
    while inv*num%modul!=1:
        inv+=1
    return(inv)
    


def Input(event):
    p,k=8627,2   
    doc_name=text1.get()
    x=int(text2.get())
    f=open(doc_name, 'rb')
    text=f.read()
    #print(text)
    h=hashlib.sha1(text)
    h=str(h.hexdigest())
    m=int(h,16)
    while NOD(k,p-1)!=1:
        k=random.randint(2,p-2)
    g=primitive_root(p)
    y=pow_h(g,x,p)
    r=pow_h(g,k,p)
    s=((m-x*r)*Invert_number(k,p-1))%(p-1)
    text3.insert(0,str('('+str(r)+', '+str(s)+')'))
    text4.insert(0,str('('+str(p)+', '+str(g)+', '+str(y)+')'))
#####CHECK###
    left=(pow_h(y,r,p)*pow_h(r,s,p))%p
    right=pow_h(g,m,p)
    if right==left:
        label5.config(text='Подпись верна')
    return(doc_name)


from tkinter import *
import sys
import hashlib
import random
p,k=8627,2    
root=Tk()
root.geometry('400x200+360+200')
root.title('El-Gamal')
label1=Label(root,text='Имя документа')
label1.grid(row=0,column=0)
label2=Label(root,text='Секретный ключ')
label2.grid(row=0,column=1)
text1=Entry(root,bd=5,width=15)
text1.grid(row=1,column=0)
text2=Entry(root,bd=5,width=15)
text2.grid(row=1,column=1)
button1=Button(root,text='Ввод',width=4,height=1,bg='black',fg='white',font='arial 14')
button1.grid(row=1,column=2)
label3=Label(root,text='Подпись')
label3.grid(row=2,column=0)
text3=Entry(root,bd=5,width=15)
text3.grid(row=3,column=0)
label4=Label(root,text='Открытый ключ')
label4.grid(row=4,column=0)
text4=Entry(root,bd=5,width=15)
text4.grid(row=5,column=0)
label5=Label(root,text='')
label5.grid(row=6,column=0)
name=button1.bind('<Button-1>', Input)
root.mainloop()


