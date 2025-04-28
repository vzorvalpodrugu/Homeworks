import csv
special_symbol = '!@#$%^&*()_+"№;%:?-=/";:<>,. '
passw = 'fdsf32f@$1fs;'

# Короче хотел сделать проверку отдельными функциями, но понял что 4 цикла это перебор
# но всё же решил оставить их, чтобы показать что я это пытался сделать
# def letter_in_word(word: str):
#     """
#     check if letter in word
#     """
#     for letter in word:
#         if letter.isalpha():
#             return True
#     return False
#
#
# def title_in_word(word: str):
#     """
#     check if title in word
#     """
#     for letter in word:
#         if letter.istitle():
#             return True
#     return False
#
#
# def num_in_word(word: str):
#     """
#     check if number in word
#     """
#     for letter in word:
#         if letter.isdigit():
#             return True
#     return False
#
#
# def spec_in_word(word: str):
#     """
#     check if special symbol in word
#     """
#     for letter in word:
#         if letter in special_symbol:
#             return True
#     return False


def password_cheker(min_len: int = 8, spec_symbol: str = special_symbol):
    def decorator(func):
        def wrapper(password: str):
            if len(password) < min_len:
                raise ValueError('Password is too short')
            else:
                # Теперь здесь 1 цикл, ну кроме letter in spec_symbol, и вроде всё четко
                isDigit = isTitle = isSpecial = isLower = False
                for letter in password:
                    if letter.isdigit(): isDigit = True
                    if letter.istitle(): isTitle = True
                    if letter.islower(): isLower = True
                    if letter in spec_symbol: isSpecial = True
                if isDigit and isTitle and isLower and isSpecial:
                    return func(password)
                else:
                    raise ValueError('Password is too weak')
        return wrapper
    return decorator


@password_cheker()
def register_user(password: str):
    return "User registered"

# print(register_user('1sRq@werq'))

def password_validator(min_length: int = 8, min_uppercase: bool = False, min_lowercase:bool = False, min_special_chars:bool = False):
    def decorator(func):
        def wrapper(username: str, password: str):
            if len(password) < min_length:
                raise ValueError('Password is too short')
            else:
                # Теперь здесь 1 цикл, ну кроме letter in spec_symbol, и вроде всё четко
                for letter in password:
                    if letter.istitle(): min_uppercase = True
                    if letter.islower(): min_lowercase = True
                    if letter in special_symbol: min_special_chars = True
                if min_uppercase and min_lowercase and min_special_chars:
                    return func(username, password)
                else:
                    raise ValueError('Password is too weak')
        return wrapper
    return decorator

def username_validator():
    def decorator(func):
        def wrapper(username: str, password: str):
            for letter in username:
                if letter == " ":
                    raise ValueError('Username contains space')
            return func(username, password)
        return wrapper
    return decorator

@password_validator()
@username_validator()
def register_user(username: str, password: str):
    with open('file.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(username)
        writer.writerows(password)
    return "User registered"

# print(register_user("makaka", "1sS$rsfew"))

try:
    register_user("JohnDoe", "Password123!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

