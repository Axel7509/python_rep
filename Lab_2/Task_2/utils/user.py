from utils.storage import Storage
from typing import NoReturn


class User:
    def __init__(self, username: str | None = None):
        self.__username = username
        self.__container = Storage()

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, new_username: str) -> NoReturn:
        self.username = new_username

    @property
    def container(self) -> Storage:
        return self.__container

    def add_keys(self, *keys: tuple[str]) -> NoReturn:
        self.container.add(keys)

    def remove_key(self, key: str) -> NoReturn:
        self.container.remove(key)

    def list_data(self) -> NoReturn:
        print(self.container.list())

    def find_key(self, key: str) -> NoReturn:
        print(self.container.find(key))

    def grep_keys(self, regex: str) -> NoReturn:
        print(self.container.grep(regex))

    def save_data(self) -> NoReturn:
        self.container.save(self.username)

    def load_data(self) -> NoReturn:
        self.container.load(self.username)

    def switch(self, new_username: str) -> NoReturn:
        self.username = new_username
        self.container.load(new_username)