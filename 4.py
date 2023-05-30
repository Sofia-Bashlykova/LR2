from random import randint
i = 0
j = 0
while i < 3:
    x = randint(1, 100)
    y = randint(1, 100)
    z = int(input(str(x) + '+' + str(y) + '='))
    if z != x + y:
        print('ответ неверный')
        i += 1
    else:
        print('правильно!')
        j += 1
    if i == 3:
        print('игра окончена. правильных ответов:', j)
