
normal = []
emergency = []


while True:
    print('ثبت نام:1')
    print('پذیرش:2')
    print('بیمار فوری:3')
    print('بیمار بعدی:4')
    print('لیست انتظار:5')
    print('لغو نوبت:6')
    print('استعلام نوبت:7')
    print('خروج:8')

    n = int(input('enter a number :'))
    if n == 1:   #ثبت نام
        name = input('enter your name :')
        if name in normal or name in emergency:
            print('your name is repated')
        else:
            normal.append(name)
            print('sabt shod')


    elif n == 2:    #پذیرش
        if emergency:
            print(emergency.pop(0))
        elif normal:
            print(normal.pop(0))
        else:
            print('empty')

    elif n == 3:   #بیمار فوری
        name = input('enter your name :')
        if name in emergency or name in normal:
            print('your name is repated')
        else:
            emergency.append(name)

    elif n == 4:   #بیمار بعدی
        if emergency:
            print(emergency[0])
        elif normal:
            print(normal[0])
        else:
            print('empity')


    elif n == 5:   #لیست انتظار
        print('emergency')
        for i in emergency:
            print(i)
        print('normal')
        for i in normal:
            print(i)

    elif n == 6:    #لغو نوبت
        name = input('enter your name :')
        if name in emergency :
            emergency.remove(name)
        else:
            normal.remove(name)
            print('your name removed')


    elif n == 7:   #استعلام نوبت
        name = input('enter your name :')
        if name in emergency:
            print('nobat', emergency.index(name) + 1)
        else:
            print('nobat', normal.index(name) + 1)

    elif n == 8:
        print('exit')
        break

