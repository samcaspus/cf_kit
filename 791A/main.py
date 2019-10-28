b1,b2 = [int(p) for p in input().split()]
counter = 0
while b1<=b2:
    b1*=3
    b2*=2
    counter+=1

print(counter)
    
