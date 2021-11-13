import os


class FileResult():
    def __init__(self) -> None:
        self.filename = "data.csv"
        self.path = os.path.dirname(os.path.realpath(__file__)) + '/result/'
        if os.path.exists(self.path + self.filename):
            os.remove(self.path + self.filename)
        try:
            os.makedirs(self.path)
        except OSError:
            print(f'Already exists path: {self.path}')

    def insert_file(self, line):
        f = open(f"{self.path}/{self.filename}", "a")
        f.write(line + '\n')
        f.close()
