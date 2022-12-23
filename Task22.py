desk = list(range(1,10))

def print_desk(desk):
   print('-' * 15)
   for i in range(3):
      print('[', desk[0+i*3], '][', desk[1+i*3], '][', desk[2+i*3], ']')
      print('-' * 15)

def inputM(move_it):
    while True:
        try:
            a = input(move_it + ' в клетку: ')
            a = int(a)
            if a >= 1 and a <= 9:
                if(str(desk[a-1]) not in 'XO'):
                    desk[a-1] = move_it
                    return a
            else: print('Введите число от 1 до 9')
        except ValueError:
            print('Это должно быть число')

def winner(desk):
   win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for i in win:
       if desk[i[0]] == desk[i[1]] == desk[i[2]]:
          return desk[i[0]]
   return False
def game(desk):
    x = 1
    win = False
    while True:
        print_desk(desk)
        if x % 2 == 1:
           inputM('X')
           x = x + 1
        else:
           inputM('O')
           x = x + 1
        if x > 4:
           XO = winner(desk)
           if XO:
              print(XO, 'Победили')
              win = True
              break
        if x == 9:
            print('Ничья')
            break

    print_desk(desk)
game(desk)