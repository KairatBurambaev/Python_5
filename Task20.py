text = str(input('Введите текст: '))

if not str(text):
    exit()

text = text.split(' ')

new_text = ' '

for i in text:
    if 'абв' in i:
        i = ' '
    else:
        new_text = new_text + ' ' + i

print(new_text)