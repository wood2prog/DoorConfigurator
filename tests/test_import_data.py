import unittest
from src.import_data import ImportData


class TestImportData(unittest.TestCase):

    def setUp(self):
        self.data = ImportData("tests/testdata.csv")

    def test_returns_list(self):
        self.assertIs(type(self.data.file_import()), list)


if __name__ == "__main__":
    unittest.main()
