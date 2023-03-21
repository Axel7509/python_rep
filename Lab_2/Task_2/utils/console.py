from utils.user import User
from utils import messages


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
        }

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, new_username):
        self.user = User(new_username)

    @property
    def commands(self):
        return self.__commands

    @staticmethod
    def parse_cmd():
        raw_command = input().split(maxsplit=1)

        return raw_command[0], \
            (raw_command[-1], tuple(raw_command[-1].split()))[' ' in raw_command[-1]] if len(raw_command) > 1 else ''

    def run(self, command, args):
        if command not in self.commands:
            print(messages.INVALID_COMMAND_MESSAGE)
        else:
            self.commands[command](args) if args else self.commands[command]()

    def start_session(self):
        print(messages.WELCOME_MESSAGE)
        print(messages.INFO_MSG)
        while True:
            command, args = self.parse_cmd()
            self.run(command, args)