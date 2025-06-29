from part import Part
import configparser
import json


class Door:

    def __init__(self, id, width, length):
        self.id = id
        self.width = width
        self.length = length
        self.parts = []

    def add_part(self, name, length, width, thickness):
        self.parts.append(Part(name, width, length, thickness))

    def junk(self):
        json_string = json.dumps(["names", {"jesse": 34, "rachel": 56}], indent=4)
        print(json_string)


test = Door(123, 1, 2)
test.junk()
