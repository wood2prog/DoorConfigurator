import csv


class ImportData:

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.file_header = None
        self.data = []
        self.file_import()

    def file_import(self):
        read_header = False

        with open(self.file_name, newline="") as csvfile:
            door_data = csv.reader(csvfile, delimiter=",")
            for row in door_data:
                if read_header:
                    self.data.append(row)
                else:
                    self.file_header = row
                    read_header = True

    def get_header(self):
        return self.file_header

    def get_data(self):
        return self.data
