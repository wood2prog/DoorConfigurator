class Part:

    def __init__(self, name, width, length, thickness):
        self._name = name
        self._length = length
        self._width = width
        self._thickness = thickness

    def name(self):
        return self._name

    def width(self):
        return self._width

    def length(self):
        return self._length

    def thickness(self):
        return self._thickness
