from .commands import list, config
from .exceptions import LarvaException, CommandNotAvailableError
from click import echo


class Commander:
    def __init__(self):
        self.commands = {
            'list': list.ListCommand(),
            'config': config.ConfigCommand()
        }

    def invoke(self, cmd, **kwargs):
        command = self.commands.get(cmd, None)
        if command:
            try:
                command.run(**kwargs)
            except LarvaException as exc:
                echo('Error: {}'.format(exc))
            return

        raise CommandNotAvailableError('The command called is not available.')
