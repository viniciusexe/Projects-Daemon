C = input().split()
A, B = C
if A == '1':
    print("Total: R$ {:.2f}".format(4.00*float(B)))
if A == '2':
    print("Total: R$ {:.2f}".format(4.50*float(B)))
if A == '3':
    print("Total: R$ {:.2f}".format(5.00*float(B)))
if A == '4':
    print("Total: R$ {:.2f}".format(2.00*float(B)))
if A == '5':
    print("Total: R$ {:.2f}".format(1.50*float(B)))