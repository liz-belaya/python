def similar():
    #if not len(first) == len(second):
     #   return False
    mass=[]
    for i in range(len(text)-len(word)):
        find=text[i:i+len(word)]
       # print(find)
        if len(find) - sum(l1==l2 for l1, l2 in zip(find, word)) < 5:
            #return False
            mass.append(text[i:i+len(word)])
    return (mass)


f=open('analyze.py', encoding="utf-8")
f=f.readlines()
text=''
for i in range(len(f)):
    text+=f[i]
print(text)
word='password'
#mass=[]
#for i in range(len(f)-len(word)):
    
 #   mass.append(similar(f[i:i+len(word)]
    
#print(f)
mass=similar()

print(mass)        
                
