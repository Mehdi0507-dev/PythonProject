x = int(input('pls enter height: '))
for i in range(1,x+1):      #تعداد سطر ها

    for j in range(x - i):
        print(' ',end='')     # فاصله ها

    for k in range(2*i - 1):
        print("*",end='')      #تعداد ستاره ها

    print()     #رفتن به خط بعدی بعد از اتمام هر سطر

