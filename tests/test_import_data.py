import unittest
from src.file_io import ImportData


class TestImportData(unittest.TestCase):

    def setUp(self):
        self.data = ImportData("tests/testdata.csv")


if __name__ == "__main__":
    unittest.main()
