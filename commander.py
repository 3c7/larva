from commands import list, config


class Commander:
    def __init__(self):
        self.commands = {
            'list': list.ListCommand(),
            'config': config.ConfigCommand()
        }

