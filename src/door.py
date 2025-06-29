from part import Part
import configparser


class Door:

    def __init__(self, id, width, length):
        self.id = id
        self.width = width
        self.length = length
        self.parts = []

    def add_part(self, name, length, width, thickness):
        self.parts.append(Part(name, width, length, thickness))

    def junk(self):
        config = configparser.ConfigParser()
        config.read_file("door_config.ini")
        print(config.sections())


test = Door(123, 1, 2)
test.junk()
