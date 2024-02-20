def Create_of_text(piece, N, text):
    mass_of_positions=[]
    num,j,k=0,0,0
    piece1=piece[-N+1:]
    while k==0:
        mass_of_positions.append(text[0].find(piece1, j, (len(text[0])-len(piece1)-1)))
        if mass_of_positions[num]==-1:
            k=-1
        else:
            j=mass_of_positions[num]+1
            num+=1
   # print('Sort out from',mass_of_positions)
    random_number=random.randint(0,len(mass_of_positions)-2) #generate letter`s position
    position=mass_of_positions[random_number]
    #print('position new letter', position)
    new_letter=text[0][position+len(piece1)]
    return(new_letter)

def Input(event):
    doc_name=text1.get()
    size=int(text2.get())
    f=open(doc_name)
    text=f.readlines()
    N=int(text3.get())
    random_number=random.randint(0,len(text[0]))
    computer_text=text[0][random_number]
    for i in range(size-1):
        computer_text1=computer_text
        computer_text+=Create_of_text(computer_text1, N, text)
    T.insert(END, computer_text)   
    print(computer_text)
    
    
    return(doc_name)





from tkinter import *
import random
root=Tk()
root.geometry('400x400+360+200')
root.title('Text Generation')
f_top=Frame(root)
f_bot=Frame(root)
#label1=Label(root,text='Имя документа')
#label1.grid(row=0,column=0)
label1=Label(f_top,width=15, height=4,text='Имя документа')
#label1.pack()
#label2=Label(root,text='Длина текста')
#label2.grid(row=0,column=1)
#label2.pack()
label2=Label(f_top,width=15, height=4, text='Длина текста')
#label3=Label(root,text='Число переходов')
#label3.grid(row=0,column=2)
#label3.pack()
label3=Label(f_top, width=15, height=4,text='Число переходов')
text1=Entry(f_bot,bd=5,width=15)
#text1.grid(row=1,column=0)
#text1.pack()

text2=Entry(f_bot,bd=5,width=15)
#text2.grid(row=1,column=1)
text3=Entry(f_bot,bd=5,width=15)
#text3.grid(row=1,column=2)
T=Text(root)
#T.grid(row=2, column=0)
S=Scrollbar(root)

button1=Button(root,text='Ввод',width=4,height=1,bg='black',fg='white',font='arial 14')
#button1.grid(row=1,column=3)
f_top.pack()
label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)
f_bot.pack()
text1.pack(side=LEFT)
text2.pack(side=LEFT)
text3.pack(side=LEFT)
button1.pack()
S.pack(side= RIGHT, fill=Y)
T.pack(side=LEFT,fill=BOTH)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
name=button1.bind('<Button-1>', Input)
root.mainloop()
