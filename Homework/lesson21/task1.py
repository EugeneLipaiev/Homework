import logging
import pytest

class OpenFile():
    count = 0

    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode
        self.file = open(file_path, mode)
        OpenFile.count += 1

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        logging.info(f"File {self.file_path} is closed")

    @classmethod
    def get_count(cls):
        return cls.count

with OpenFile("example.txt", "w") as f:
    f.write("Ukraine will win the war")

print(OpenFile.get_count())

#task3

@pytest.fixture
def my_file():
    file = "example.txt"
    with open("example.txt", "w") as f:
        f.write("Don't worry")
    with open(file, "r") as f:
        yield f

my_file
