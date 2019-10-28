bills = [100,20,10,5,1]
amount = int(input())
count = 0
for i in bills:
    count += amount//i
    amount = amount%i
    
print(count)
