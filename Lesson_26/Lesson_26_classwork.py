# still not homework, just for practice
print()
# from typing import Callable
shop_list = ["Banana", "Apple", "Juice", "Water", "Bread"]

def cash_sorter():
    cash = []
    def sorter(data):
        nonlocal cash
        print(cash + data)
        if cash != data:
            cash = data.copy()
            print("Cash has been saved and sorted.")
            return sorted(cash)
        print("Its cash!")
        return sorted(cash)
    return sorter

# sorter_ = cash_sorter()
# print(sorter_(shop_list))
# print(sorter_(shop_list))
# shop_list.append("Milk")
# print(sorter_(shop_list))
# print(sorter_(shop_list))


# def decorator(func: Callable[[str], str]) -> Callable[[str], str]:
#     print("Decorator has been called")
#     def wrapper(s: str):
#         print("This is wrapper")
#         return func(s)
#     return wrapper

def print_hello(s: str):
    return f"Hello, {s}\n"

# decorated = decorator(print_hello)
# print(decorated('Vlad'))

# @decorator
# def print_ggwp(s: str):
#     return f"ggwp, {s}\n"

# print(print_ggwp('Lanaya'))

def decorator_root(rule: int = 5):
    def decoratornew(func):
        print('Decorator has been called')
        def wrapper(*args, **kwargs):
            print('Wrapper has been called')
            if len(args) and len(kwargs) > rule:
                raise ValueError(f"Too many arguments. Max: {rule}")
            else: return func(*args, **kwargs)
        return wrapper
    return decoratornew

@decorator_root(2)
def print_wp(*args, **kwargs):
    return f"wp, {args, kwargs}\n"

print(print_wp('Lanaya', 'Vlad', sex='15 times'))