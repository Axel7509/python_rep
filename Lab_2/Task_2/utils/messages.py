WELCOME_MESSAGE = "Welcome to CLI! Use ^C to exit."

INVALID_COMMAND_MESSAGE = "Invalid command. Skipping."

CLI_INFO: dict[str, str] = {
    "add": "<key> [key, ...] – adds one or more elements to container;",
    "remove": "<key> – delete key from container;",
    "find": "<key> [key, ...] – checks if the element is presented in the container;",
    "list": "– returns all elements of container;",
    "grep": "<regex> – check the value in the container by regular expression;",
    "save": " – saves container to file;",
    "load": "– loads container from file;",
    "switch": "– switches to another user.",

}

INFO_MSG: str = "\n".join([f"{comm} {CLI_INFO[comm]}" for comm in CLI_INFO.keys()])

END_MESSAGE: str = "\nGoodbye"
SAVE_QUESTION: str = "\nWould you like to save your storage? [y/n]: "
LOAD_QUESTION: str = "Would you like to load storage for user {}? [y/n]: "
INVALID_RESPONSE: str = "Invalid response. Aborting..."
INVALID_ARG_MESSAGE: str = "Invalid arguments: {}. Skipping..."