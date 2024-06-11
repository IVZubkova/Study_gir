#Задание 1 Пользователь вводит с клавиатуры строку. Проверьте, является ли введенная строка палиндромом

some_string = input('Введите строку: ')
some_string = some_string.replace(' ', '')
some_string = some_string.lower()

reversed_string = ''.join(reversed(some_string))
lowercase_string = reversed_string.lower()

if some_string == lowercase_string:
    print(f'Строка {some_string} является палиндромом')
else:
    print(f'Строка {some_string} не является палиндромом')

#Задание 2 Пользователь вводит с клавиатуры некоторый текст,после чего пользователь вводит список зарезервированных
#слов. Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний. Вывести на
#экран измененный текст

text = input('Введите текст: ')

while True:
    reg_word = input('Введите зарезервированное слово: ')
    if reg_word in text:
        reg_word = reg_word.upper()
        print(reg_word)
    else:
        break

#Задание 3 Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный
#результат.

text = ('Гора - форма рельефа, изолированное резкое поднятие местности с выраженными склонами и '
        'подножием или вершина в горной стране. '
        'По характеру вершины выделяют пикообразные, '
        'куполообразные, платообразные и другие горы. Вершины подводных гор могут представлять собой острова.')

sentence_num = 0

for t in text.split('.'):
    for st in t.split(('.')):
        if st != '':
            sentence_num += 1
print(f'Количество предложений - {sentence_num}')


