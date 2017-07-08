from .command import Command
from ..configurator import Configurator
from click import echo
import json


class ConfigCommand(Command):
    def run(self, **kwargs):
        config_type = kwargs.get('type', None)
        mode_set = kwargs.get('mode_set', False)
        dump = kwargs.get('dump', False)
        clear = kwargs.get('clear', False)
        configurator = Configurator()

        if dump:
            echo(json.dumps(configurator.config, indent=4))
            return

        if clear:
            configurator.config = {}
            configurator.save()
            echo('config cleared')
            return

        if not mode_set:
            echo(configurator.get_value(config_type))
            return

        configurator.set_value(config_type, mode_set)
        configurator.save()
        echo('{} set'.format(mode_set))
