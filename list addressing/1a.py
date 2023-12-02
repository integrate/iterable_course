"""
создать два списка: А и Б. каждый список заполнить случайными числами от 1 до 10.
две команды играли матч в футбол. число в списке означает количество голов, которое команда забила в каком-то тайме.
превое число в списке А означает, сколько голов забила команда А в первом тайме. второе число - во втором тайме.

Например, выпали такие списки:
a=[1,8,4]
b=[4,2,6]
Вывести в консоль следующий текст:
  В первом тайме победила команда Б со счетом 1:4
  Во втором тайме победила команда А со счетом 8:2
  В третьем тайме победила команда Б со счетом 4:6
  Во всей игре победила команда Б со счетом по таймам 2:1
"""

import random

a=[random.randint(1,10),random.randint(1,10),random.randint(1,10)]
b=[random.randint(1,10),random.randint(1,10),random.randint(1,10)]
print(a)
print(b)

schetA = 0
schetB = 0
if a[0]>b[0]:
    print("В первом тайме победила команда А со счетом",str(a[0])+":"+str(b[0]))
    schetA+=1
elif a[0]<b[0]:
    print("В первом тайме победила команда Б со счетом",str(a[0])+":"+str(b[0]))
    schetB += 1
else:
    print("В первом тайме команды сыграли в ничью со счетом",str(a[0])+":"+str(b[0]))

if a[1]>b[1]:
    print("Во втором тайме победила команда А со счетом",str(a[1])+":"+str(b[1]))
    schetA+=1
elif a[1]<b[1]:
    print("Во втором тайме победила команда Б со счетом",str(a[1])+":"+str(b[1]))
    schetB += 1
else:
    print("Во втором тайме команды сыграли в ничью со счетом",str(a[1])+":"+str(b[1]))

if a[2]>b[2]:
    print("В третьем тайме победила команда А со счетом",str(a[2])+":"+str(b[2]))
    schetA+=1
elif a[2]<b[2]:
    print("В третьем тайме победила команда Б со счетом",str(a[2])+":"+str(b[2]))
    schetB += 1
else:
    print("В третьем тайме команды сыграли в ничью со счетом",str(a[2])+":"+str(b[2]))

if schetA>schetB:
    print("В игре одержала победу команда А со счетом по таймам", str(schetA)+":"+str(schetB))
elif schetB>schetA:
    print("В игре одержала победу команда Б со счетом по таймам", str(schetA)+":"+str(schetB))
else:
    print("Команды сыграли вничью со счетом по таймам", str(schetA)+":"+str(schetB))