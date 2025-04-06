from abc import ABC, abstractmethod
import json, csv

class AbstractFile(ABC):
    """
    Abstract base class for files.
    """
    def __init__(self, filepath: str):
        """
        Initialize the file with its filepath.
        :param filepath: Path to the file.
        """
        self.filepath = filepath

    @abstractmethod
    def read(self):
       pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def append(self, data):
        pass

    def __str__(self):
        return f"Class: {self.__class__.__name__} \nFile: {self.filepath}"

class JsonFile(AbstractFile):
    """
    Class for JSON files.
    """
    def __init__(self, filepath: str):
        super().__init__(filepath)

    def read(self):
        """
        Read and return the content of the JSON file.
        :return: JSON data loaded from the file.
        """
        with open(self.filepath, 'r') as file:
            return json.load(file)

    def write(self, data):
        """
        Write the given JSON data to the file.
        :param data: JSON data to be written.
        """
        with open(self.filepath, 'w') as file:
            json.dump(data, file)

    def append(self, data):
        """
        Append the given JSON data to the file.
        :param data: JSON data to be appended.
        """
        with open(self.filepath, 'a') as file:
            json.dump(data, file)

class TxtFile(AbstractFile):
    """
    Class for TXT files.
    """
    def __init__(self, filepath: str):
        super().__init__(filepath)

    def read(self):
        """
        Read and return the content of the TXT file.
        :return: Contents of the TXT file.
        """
        with open(self.filepath, 'r') as file:
            return file.read()

    def write(self, data):
        """
        Write the given data to the file.
        :param data: Data to be written.
        """
        with open(self.filepath, 'w') as file:
            file.write(data)

    def append(self, data):
        """
        Append the given data to the file.
        :param data: Data to be appended.

        Args:
            *data:
        """
        with open(self.filepath, 'a') as file:
            file.write(data)

class CvsFile(AbstractFile):
    """
    Class for CSV files.
    """
    def __init__(self, filepath: str):
        super().__init__(filepath)

    def read(self):
        """
        Read and return the content of the CSV file.
        :return: List of rows in the CSV file.
        """
        with open(self.filepath, 'r') as file:
            return csv.reader(file)

    def write(self, data):
        """
        Write the given data to the file as a CSV file.
        :param data: List of rows to be written.
        """
        with open(self.filepath, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def append(self, data):
        """
        Append the given data to the file as a CSV file.
        :param data: List of rows to be appended.
        """
        with open(self.filepath, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)