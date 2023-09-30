# This solution uses Open Closed Pronciple

from abc import ABC


class BaseFileType(ABC):
    @staticmethod
    def save_filenames(base_name: str, filenames_list: list, file_type: str):
        file_name: str = file_type[1:] + '_' + base_name
        with open(file_name, 'w') as f:
            for fname in filenames_list:
                f.write(fname)


class CFileType(BaseFileType):
    def __init__(self):
        self.filenames: list = []
        self.file_type: str = '.c'

    def meets_condidition(self, filename: str) -> bool:
        return filename.endswith(self.file_type)


class CPPFileType(BaseFileType):
    def __init__(self):
        self.filenames: list = []
        self.file_type: str = '.cpp'

    def meets_condidition(self, filename: str) -> bool:
        return filename.endswith(self.file_type)


class CSFileType(BaseFileType):
    def __init__(self):
        self.filenames: list = []
        self.file_type: str = '.cs'

    def meets_condidition(self, filename: str) -> bool:
        return filename.endswith(self.file_type)


def main():
    # base_filename: str = input()
    base_filename: str = 'mf.txt'
    objects: list = []
    for cls in BaseFileType.__subclasses__():
        objects.append(cls())

    with open(base_filename) as file:
        filename: str = ''
        for line in file:
            filename = line.rstrip().lower()
            for o in objects:
                if o.meets_condidition(filename):
                    o.filenames.append(line)

    for o in objects:
        BaseFileType.save_filenames(base_filename, o.filenames, o.file_type)


if __name__ == '__main__':
    main()
