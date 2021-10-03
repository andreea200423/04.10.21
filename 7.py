X = [[1, 21, -45, 67, 89]
    [23, 46, 43, 65, 2]
    [42, 88, 23, 12, 33]
    [-77, 65, -91, 27, 34]
    [5, 6, 78, 95, 54, -76]]
print('suma 1 rând e', sum(X[0]))
print('suma 2 rând e', sum(X[1]))
print('suma 3 rând e', sum(X[2]))
print('suma 4 rând e', sum(X[3]))
print('suma 5 rând e', sum(X[4]))
c1=0
c2=0
c3=0
c4=0
c5=0
for i in X:
    c1+=[0]
    c2+=[1]
    c3+=[2]
    c4+=[3]
    c5+=[4]
print('suma 1 coloane e', c1)
print('suma 2 coloane e', c2)
print('suma 3 coloane e', c3)
print('suma 4 coloane e', c4)
print('suma 5 coloane e', c5)
p = X[0][0]+X[1][1]+X[2][2]+X[3][3]+X[4][4]
s = X[0][4]+X[1][3]+X[2][2]+X[3][1]+X[4][0]
print('suma diagonalei principale e', p, 'suma diagonalei secundare e ', s)