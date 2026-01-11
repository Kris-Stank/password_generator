import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

pw_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
pw_len = int(input('Какой длины должен быть пароль? '))
pw_digits = input('Включать ли в пароль цифры от 0 до 9? (y/n) ')
pw_uppercase = input('Включать ли в пароль прописные буквы? (y/n) ')
pw_lowercase = input('Включать ли в пароль строчные буквы? (y/n) ')
pw_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? (y/n) ')
pw_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? (y/n) ')

if pw_digits == 'y':
    chars += digits
if pw_uppercase == 'y':
    chars += uppercase_letters
if pw_lowercase == 'y':
    chars += lowercase_letters
if pw_punctuation == 'y':
    chars += punctuation

if pw_exceptions == 'y':
    chars = chars.replace('i', '').replace('l', '').replace('1', '').replace('L', '').replace('o', '').replace('O', '').replace('0', '')

for i in range(pw_quantity):
    password = ''.join(random.choices(chars, k=pw_len))
    print(password)
