import unittest
from task1 import OpenFile


class OpenTestCase(unittest.TestCase):

    def test_writer(self):
        file_path = "example.txt"
        mode = "w"
        with OpenFile(file_path, mode) as f:
            self.assertEqual(f.mode, mode)
            self.assertEqual(f.name, file_path)

    def test_close(self):
        file_path = "example.txt"
        mode = 'w'
        with OpenFile(file_path, mode) as f:
            pass
        self.assertTrue(f.closed)

unittest.main


