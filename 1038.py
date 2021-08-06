a, b = input().split(' ')
a = int(a)
b = int(b)
l1 = 1
l2 = 2
l3 = 3
l4 = 4
l5 = 5
if a == l1:
    t = 4.00 * b
    print(f'Total: R$ {t:.2f}')
elif a == l2:
    t = 4.50 * b
    print(f'Total: R$ {t:.2f}')
elif a ==l3:
    t = 5.00 * b
    print(f'Total: R$ {t:.2f}')
elif a == l4:
    t = 2.00 * b
    print(f'Total: R$ {t:.2f}')
elif a == l5:
    t = 1.50 * b
    print(f'Total: R$ {t:.2f}')