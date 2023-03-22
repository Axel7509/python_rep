from utils.user import User
from utils import messages
import sys


class Console:
    def __init__(self):
        self.__user = User(input("Username: "))
        self.__commands = {
            "add": self.__user.add_keys,
            "remove": self.__user.remove_key,
            "find": self.__user.find_key,
            "list": self.__user.list_data,
            "grep": self.__user.grep_keys,
            "save": self.__user.save_data,
            "load": self.__user.load_data,
            "switch": self.__user.switch,
        }

    @property
    def user(self) -> User:
        return self.__user

    @user.setter
    def user(self, new_username: str):
        self.user = User(new_username)

    @property
    def commands(self):
        return self.__commands

    @staticmethod
    def parse_cmd() -> tuple[str, tuple[str]]:
        raw_input = input().split(maxsplit=1)

        try:
            return (
                raw_input[0],
                ('', raw_input[-1].split())[len(raw_input) > 1]
            )
        except IndexError:
            return '', tuple('')

    def run(self, command, args):
        if command not in self.commands:
            print(messages.INVALID_COMMAND_MESSAGE)
        else:
            self.commands[command](args) if args else self.commands[command]()

    def start_session(self):
        print(messages.WELCOME_MESSAGE)
        print(messages.INFO_MSG)
        while True:
            try:
                self.run(*self.parse_cmd())
            except KeyboardInterrupt:
                self.stop_session()

    def stop_session(self):
        """Makes necessary preparations before stopping a session."""

        try:
            ans = input(messages.SAVE_QUESTION)
        except KeyboardInterrupt:
            sys.exit()

        if not ans or ans not in ['y', 'n']:
            print(messages.INVALID_RESPONSE)
            sys.exit()

        self.run('save' if ans == 'y' else '', tuple(''))
        print(messages.END_MESSAGE)
        sys.exit()