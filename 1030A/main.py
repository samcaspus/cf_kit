no = int(input())
li = [int(p) for p in input().split()]
li.sort(reverse=True)
if li[0]==0:
    print("EASY")
else:
    print("HARD")