x = float (input('Введите x '))
y = float (input('Введите y '))

if x == 0 or y == 0:
    print('Координата лежит на оси')
elif x > 0 and y > 0 :
    print(f' 1 четверть');
elif x < 0 and y > 0:
    print(f' 2 четверть');
elif x < 0 and y < 0 :
    print(f' 3 четверть');
elif x >0 and y < 0:
    print(f' 4 четверть');