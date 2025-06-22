import part
import configparser


class Door:

    def __init__(self, id, width, length):
        self.id = id
        self.width = width
        self.length = length
        self.parts = []

    def generate(self, thickness, material, name):
        pass

    def calc_left_stile(self):
        parser = configparser.ConfigParser()
        parser.read_file("src/door_config.ini")

        return self.length + parser["MACHINE"]["trim"] * 2
