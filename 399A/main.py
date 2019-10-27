a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
li = []
for i in range(b-c,b+c+1):
    if i>0:
        li.append(i)
 
if li[0]!=1:
    print("<<",end=" ")
 
for i in li:
    
    if i==b:
        print('('+str(i)+')',end=" ")
    else:
        print(i,end=" ")
 
    if i==a:
        break
 
if a not in li:
    print(">>")