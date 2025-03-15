def print_user_info(**user_info):
    print(user_info)
    for key, value in user_info.items():
        print(f"{key} = {value}")

print_user_info(name="Иван", last_name="Морозов", age=25)

user_info = {"name":"Катя", "last_name":"Блохова"}
print_user_info(**user_info)
