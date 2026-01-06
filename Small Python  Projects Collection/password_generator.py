import random
import string


def password_generator(nr_letters, nr_digits, nr_symbols):
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+']
    print("Welcome to the Password Generator!")
    password = []
    for _ in range(nr_letters):
        password.append(random.choice(letters))
    for _ in range(nr_digits):
        password.append(random.choice(numbers))
    for _ in range(nr_symbols):
        password.append(random.choice(symbols))
    random.shuffle(password)
    return ''.join(password)


print(password_generator(4,3,2))