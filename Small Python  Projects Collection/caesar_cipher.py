"""Implementation of the Caesar Encryption Algorithm"""

import string

def caesar(letter, shift, operation_type):
    message = []
    letters = list(string.ascii_lowercase)
    for let in letter.lower():
        if not let.isalpha():
            message.append(let)
        else:
            position = letters.index(let)
            if operation_type=='encode':
                message.append(letters[(position+shift)%25])
            else:
                message.append(letters[(position-shift)%25])
    return ''.join(message)


print(caesar("hello world!", 9, 'encode'))

print(caesar(caesar("hello world!", 9, 'encode'), 9, 'decode'))