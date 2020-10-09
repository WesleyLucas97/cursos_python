v = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0 ]]
c = 0
print(type(v))
for i in range(0, 3):
    for j in range(0, 4):
        v[i][j] = int(input('numero:'))
for i in range(0, 3):
    for j in range(0, 4):
        print(f'[{v[i][j]}]', end= '')
        if v[i][j] > 10:
            c = c + 1
    print()
print(c)