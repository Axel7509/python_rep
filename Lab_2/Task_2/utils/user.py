from utils.storage import Storage
from typing import NoReturn
from utils import messages
from re import Pattern


class User:
    def __init__(self, username: str | None = None):
        self._username = username
        self._container = Storage()
        self._container.load(username)

    @property
    def username(self) -> str | None:
        return self._username

    @username.setter
    def username(self, new_username: str) -> NoReturn:
        self._username = new_username

    @property
    def container(self) -> Storage:
        return self._container

    def add_keys(self, *keys: tuple[str]) -> NoReturn:
        self.container.add(*keys)

    def remove_key(self, key: tuple[str]) -> NoReturn:
        self.container.remove(*key)

    def list_data(self) -> NoReturn:
        print(f"[{', '.join(self.container.list())}]")

    def find_key(self, key: str) -> NoReturn:
        print(self.container.find(key))

    def grep_keys(self, regex: tuple[str | bytes | Pattern[bytes]]) -> NoReturn:
        print(self.container.grep(*regex))

    def save_data(self) -> NoReturn:
        self.container.save(self.username)

    def load_data(self) -> NoReturn:
        self.container.load(self.username)

    def switch(self, new_username: tuple[str]) -> NoReturn:
        ans: str = input(messages.LOAD_QUESTION.format(new_username[0]))

        if ans == 'y':
            self._container.load(new_username[0], switch=True)
        elif ans != 'n':
            print(messages.INVALID_RESPONSE)

        self.username = new_username[0]