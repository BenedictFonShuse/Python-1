import os
from typing import List


class FileUtil:

    @staticmethod
    def write_to_file(file_name: str, add_string: str, mode: str):
        file_path = FileUtil.method_name(file_name)
        with open(file_path, mode, encoding="UTF-8") as file:
            file.write(add_string)

    def generate_file(self, file_name: str, strings: list, mode: str):
        final_string = ""
        for string in strings:
            final_string += str(f"{string}\n")
        self.write_to_file(file_name, final_string, mode)

    @staticmethod
    def read_file(file_name: str) -> List[str]:
        file_path = FileUtil.method_name(file_name)
        temp_list = []
        with open(file_path, "r", encoding="UTF-8") as file:
            for line in file.readlines():
                temp_list.append(line[:-1])
            return temp_list

    @staticmethod
    def method_name(file_name):
        working_directory = os.getcwd()
        file_path = str(f"{working_directory}/text/{file_name}")
        return file_path
