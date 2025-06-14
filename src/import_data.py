import csv


class ImportData:

    def __init__(self, file_name: str):
        self.file_name = file_name

    def file_import(self):
        door_list = []
        with open(self.file_name, newline="") as csvfile:
            door_data = csv.reader(csvfile, delimiter=",")
            for row in door_data:
                door_list.append(row)

        return door_list
