import random

game = int(input('Игра на двоих, введите 1\nИгра против бота, введите 2\n: '))

glob = 250

def inputRock(inputRock):
    while True:
        try:
            Rock = int(input(f'Осталось камней: {glob}\nСколько камней возьмете?: '))
            if Rock in range(1,29):
                return Rock
            else: print('Можно взять от 1 до 28 камня')
        except ValueError:
            print('Это должно быть число')

x = random.randint(1,2)

while glob > 0:
    if game == 1:
        if x == 1:
            print('Ходит Красный игрок')
            glob = glob - inputRock(inputRock)
            if glob <= 0:
                print('Победитель Красный игрок!')
            x = x + 1
        else:
            print('Ходит Синий игрок')
            glob = glob - inputRock(inputRock)
            if glob <= 0:
                print('Победитель Синий игрок!')
            x = x - 1
    else:
        if x == 1:
            print('Ходит компьютер')
            y = random.randint(1,2)
            if glob <= 159 and glob > 132:
                if y == 1:
                    glob = glob - (glob - 132)
                    x = x + 1
                else:
                    glob = glob - random.randint(1,28)
                    x = x + 1
            elif glob <= 131 and glob > 104:
                if y == 1:
                    glob = glob - (glob - 104)
                    x = x + 1
                else:
                    glob = glob - random.randint(1,28)
                    x = x + 1
            elif glob <= 103 and glob > 85:
                if y == 1:
                    glob = glob - (glob - 85)
                    x = x + 1
                else:
                    glob = glob - random.randint(1,28)
                    x = x + 1
            elif glob <= 84 and glob > 57:
                if y == 1:
                    glob = glob - (glob - 57)
                    x = x + 1
                else:
                    glob = glob - random.randint(1,28)
                    x = x + 1
            elif glob <= 56 and glob > 29:
                glob = glob - (glob - 29)
                x = x + 1
            elif glob == 29:
                glob = random.randint(1,28)
                x = x + 1
            elif glob <=28 and x == 1:
                glob = glob - glob
                if glob <= 0:
                    print('Победа за компьютером!')
            else:
                glob = glob - random.randint(1,28)
                x = x + 1
        else:
            glob = glob - inputRock(': ')
            if glob <= 0:
                glob = 0
                print('Вы победили!')
            print(f'Осталось камней: {glob}')
            x = x - 1