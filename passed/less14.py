# txt_file = "less14.txt"

# file = open(txt_file, 'a', encoding='utf-8')
#
# file.write('Hello, Yury!')
# file.close()

# with open(txt_file, 'r', encoding='utf-8') as file:
#     lines = file.readline()
#
# print(lines)

def write_to_file(filename: str, *data: str, mode: str = 'a', encoding: str = 'utf-8') -> None:
    with open(filename, mode, encoding= encoding) as file:
        for line in data:
            file.write(line + '\n')


write_to_file('крутой файл', 'первая строка', 'вторая строка', 'третья строка')