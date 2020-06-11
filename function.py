#урок Python - функции
my_friends={'Cаша', 'Костя', 'Миша', 'Катя', 'Захар'}
my_friends2=set(my_friends)
def message(message):
    mess_set=set(message)
    mess=message.split(',')
    return mess

def summa(a,b):
    return a+b
def digit10():
    return 'digit>10' 

def function1(digit):
    if digit<10:
        return summa(1,1)
    else:
        return digit10()

mess_finish=message('Саша, как дела?')
if mess_finish[0] in my_friends:
    print('Всё ок')
else:
    print('такого имени нет')
print(mess_finish[0])


