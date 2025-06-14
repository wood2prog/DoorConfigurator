from import_data import ImportData


class Doors:

    def __init__(self):
        self.header = []
        self.door_list = []

    def add_doors_from_file(self, file_name: str):
        door_list = ImportData(file_name)
        self.header = door_list.get_header()
        self.door_list = door_list.get_data()

    def clear_list(self):
        pass


mydoors = Doors()

mydoors.add_doors_from_file("tests/testdata.csv")
print(mydoors.header)
print(mydoors.door_list)
