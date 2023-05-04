import random
import string
import sys

first_question = input('Хотите надёжный пароль? ')
if first_question == 'Да':
    # length = int(input('Впишите длинну желаемого пароля. '))
    length = 15
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)
    second_question = input('Хотите пароль подлиннее? ')
    if second_question == 'Да':
        length += 10
        chars = string.ascii_letters + string.digits
        password = ''.join(random.choice(chars) for _ in range(length))
        print(password)
        third_question = input('Хотите ещё длиннее? ')
        if third_question == 'Да':
            length = int(input('Впишите длинну желаемого пароля. '))
            chars = string.ascii_letters + string.digits
            password = ''.join(random.choice(chars) for _ in range(length))
            print(password)
            print('История ваших ответов:', first_question, second_question, third_question)
        else:
            print('История ваших ответов:', first_question, second_question, third_question)
            sys.exit(0)
    else:
        sys.exit(0)
else:
    sys.exit(0)