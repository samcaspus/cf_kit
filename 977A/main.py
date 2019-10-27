no, times = [int(p) for p in input().split()]
for i in range(times):
    if no%10==0:
        no//=10
    else:
        no-=1
print(no)