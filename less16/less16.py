class TxtFileHandler():
    """A class to handle text files."""
    def read_file(self, filepath: str):
        """Read the content of a text file and return it.
           Args:
               :filepath (str): The path to the text file.
               :return str: The content of the text file.
        """
        try:
            with open(filepath, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return ""

    def write_file(self, filepath: str, *data: str):
        """Write data to a text file.
           Args:
               :filepath (str): The path to the text file.
               :*data (str): The data to be written to the file.
        """
        try:
            with open(filepath, 'w') as file:
                file.writelines(data)
            return "Data written successfully"
        except FileNotFoundError:
            return ""

    def append_file(self, filepath: str, *data: str):
        """Append data to a text file.
           Args:
               :filepath (str): The path to the text file.
               :*data (str): The data to be appended to the file.
        """
        try:
            with open(filepath, 'a') as file:
                file.writelines(data)
        except FileNotFoundError:
            return ""


handler = TxtFileHandler()
# content = handler.read_file('txt')
# print(content)

handler.write_file('txt', 'https://github.com/vzorvalpodrugu/Homeworks')
# handler.append_file('txt', 'This is the third line.\n')