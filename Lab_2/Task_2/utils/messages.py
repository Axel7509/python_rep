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