dict = {}

dict['Tetrahedron'] = 4
dict['Cube'] = 6
dict['Octahedron'] = 8
dict['Dodecahedron'] = 12
dict['Icosahedron'] =20

testcases = int(input())
summ = 0
for i in range(testcases):
    summ += dict[input()]

print(summ)
