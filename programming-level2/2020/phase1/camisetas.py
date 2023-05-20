N = int(input())
T = input().split()
qp = T.count('1')
qm = T.count('2')
Tp = int(input())
Tm = int(input())

if Tp >= qp and Tm >= qm:
    print('S')
else:
    print('N')

#Outro Exemplo
""" N = int(input())

cp = []
cm= []

for i in range(N):
    sizes = int((input()))
    if sizes == 1:
        cp.append(sizes)
    elif sizes == 2:
        cm.append(sizes)

p = int(input())        
m = int(input())

if len(cp) == p and len(cm) == m:
    print('S')
else:
    print('N') """