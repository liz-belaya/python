def mask_create(n,k):
    matrix=[]
    for i in range(2**n-1):
        vector=binary(i,n)
        if vector.count('0')==k-1 and vector.count('1')==n-k+1:
            matrix.append(vector)
    print(matrix)
    mask=[]
    for i in range(n):
        mask.append([])
        for j in range(len(matrix)):
            mask[i].append(matrix[j][i])
    return(mask)

def parts():
    parts=[]
    for i in range(n):
        parts.append([])
        for j in range(len(data)):##
            if mask[i][j%(len(mask[i]))]=='1':
                parts[i].append(data[j])
            else:
                parts[i].append(0)
    return(parts)

def save_file(path, bytes_file):
    writable_file = open(path, 'bw+')
    writable_file.write(bytes(bytes_file))
    writable_file.close()

                  
        
def binary(x,dlina):
    n=''
    while x > 0:
        y = str(x % 2)
        n = y + n
        x = int(x / 2)
    if len(n)<dlina:
        n='0'*(dlina-len(n))+n
    return (n)

def data_recovery():
    recover_data=[]
    for i in range(len(doli[0])):
        recover_data.append(0)
    for i in range(k1):
        for j in range(len(doli[0])):
            recover_data[j]|=doli[i][j]
    return(recover_data)


def data_comunity():
    data1=[]
    for i in range(len(data)):
        for j in range(len(data[i])):
            data1.append(data[i][j])
    return(data1)

print('Input n')
n=int(input())
print('Input k')
k=int(input())
mask=mask_create(n,k)
#print(mask)
print('Input name of file')
name=input()
f=open(name,"rb")
data=f.readlines()
#for i in range(len(data[0])):
#print(data[0])
data=data_comunity()
doli=parts()
#print(doli)
print('Enter the number of participants who provided the key')
k1=int(input())
if k1<k:
    print('Not enough keys')
recover_data=data_recovery()
#print(recover_data)
save=save_file('save.png',recover_data)

