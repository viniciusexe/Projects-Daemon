A,B = input().split()
A = int(A)
B = int(B)
if A == '1':
    print("Total: R$ {:.2}".format(4.00*float(B)))
if A == '2':
    print("Total: R$ {:.2}".format(4.50*float(B)))
if A == '3':
    print("Total: R$ {:.2}".format(5.00*float(B)))
if A == '4':
    print("Total: R$ {:.2}".format(2.00*float(B)))
if A == '5':
    print("Total: R$ {:.2}".format(1.50*float(B)))