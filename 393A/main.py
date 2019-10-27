s = input()
n = (s.count('n') - 1)/2
i = s.count('i')
e = s.count('e')/3 
t = s.count('t')
print(int(min(n, i, e, t)))