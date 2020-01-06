A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)

if A > B and A > C:
    print("{} eh o maior".format(A))
elif B > A and B > C:
    print("{} eh o maior".format(B))
elif C > A and C > B:
    print("{} eh o maior".format(C))
