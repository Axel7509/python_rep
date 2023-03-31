
import os
import re
import pickle
from typing import NoReturn


class Storage:
    __SAVE_FOLDER = os.path.relpath("data/")

    def __init__(self):
        self.__data = set()

    @property
    def data(self) -> set[str]:
        return self.__data

    @data.setter
    def data(self, new_data: set[str]) -> NoReturn:
        self.__data = new_data

    @classmethod
    def __verify_path(cls, path: str | os.PathLike | bytes) -> bool:
        """Checks if the given path exists.
        :param path: path to check"""
        return os.path.lexists(path)

    @classmethod
    def pathify(cls, name: str | os.PathLike) -> str:
        """Creates a path by concatenating __SAVE_FOLDER with the given name
        :param name: typically storage owner's name to pathify"""
        return os.path.join(cls.__SAVE_FOLDER, name)

    def add(self, *keys: tuple[str]) -> NoReturn:
        self.data.update(*keys)

    def remove(self, key: str) -> NoReturn:
        try:
            self.data.remove(key)
        except KeyError:
            print(f"No such key: {key}. Skipping.")

    def list(self) -> list:
        return list(self.data)

    def find(self, key: str) -> str:
        return key if key in self.data else "No such elements."

    def grep(self, regex: str | bytes | re.Pattern[bytes]) -> list:
        """Regex to find elements in storage"""
        try:
            return list(filter(lambda k: re.match(regex, k), self.data))
        except os.error:
            return []

    def save(self, destination: str):
        """Saves data to file"""

        path: str = self.pathify(f"{destination}.pkl")

        with open(path, 'wb+') as save_file:
            pickle.dump(self.data, save_file)

    def load(self, source: str, switch=False) -> NoReturn:

        path: str = self.pathify(f"{source}.pkl")

        if not self.__verify_path(path):
            if switch:
                self.data = set()
            return

        with open(path, 'rb') as load_file:
            try:
                new_data: set = pickle.load(load_file)
            except pickle.UnpicklingError:
                new_data = set()

        self.data = (self.data | new_data) if not switch else new_data

