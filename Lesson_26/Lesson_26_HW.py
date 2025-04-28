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


@password_cheker(8)
def register_user(password: str):
    return "User registered"

print(register_user('1sRq@werq'))