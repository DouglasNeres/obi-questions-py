idade1 = int(input())
idade2 = int(input())
idade3 = int(input())

if idade1 >= idade2 and idade2 >= idade3 or idade3 >= idade2 and idade2 >= idade1:
    print(idade2)
elif idade2 >= idade1 and idade1 >= idade3 or idade3 >= idade1 and idade1 >= idade2:
    print(idade1)
else:
    print(idade3)