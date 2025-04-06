from file_classes import JsonFile, TxtFile, CsvFile
if __name__ == "__main__":
    # Test JsonFile
    json_file = JsonFile('file.json')
    json_data = json_file.read()
    print('JSON Read:', json_data)
    json_file.append('Alice')
    json_file.write({})

    # Test TxtFile
    txt_file = TxtFile('file')
    txt_data = txt_file.read()
    print('TXT Read:', txt_data)
    txt_file.write('Name,Age Bob,20')
    txt_file.append('Charlie,25')

    # Test CsvFile
    csv_file = CsvFile('file.csv')
    csv_file.write([['Name', 'Age'], ['David', '18']])
    csv_file.append(['Eve', '22'])
    csv_data = csv_file.read()
    print('CSV Read:', csv_data)