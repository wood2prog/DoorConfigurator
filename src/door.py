import part
import configparser


class Door:

    def __init__(self, id, width, length):
        self.id = id
        self.width = width
        self.length = length
        self.parts = []

    def addPart(self, name, length, width, thickness):
        