no = int(input())
for i in range(no):
    print("I ",end="")
    if i==no-1:        
        if i&1==0:
            print("hate ",end="")
        else:
            print("love ",end="")
        print("it")
        continue
    if i&1==0:
        print("hate ",end="")
    else:
        print("love ",end="")
    print("that ",end="")
    
