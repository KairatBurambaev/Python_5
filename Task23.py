def RLE(text):

    code = ''
    i = 0

    while i < len(text):
        count = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            count = count + 1
            i = i + 1
 
        code += str(count) + text[i]
        i += 1
 
    return code
 
text = str(input('Введите текст: '))
print(RLE(text))