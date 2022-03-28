year = input()

year = int(year)

if year%4 == 0:
    if (year%4 == 0)and(year%100 != 0) == 0:
        if (year%4 ==0)and(year%400 ==0)== 1:
            print('1')
        else :
            print('0')
    elif (year%4 == 0)and(year%100 != 0) == 1:
        print('1')
else:
    print('0')

