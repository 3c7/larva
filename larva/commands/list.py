from .command import Command
from ..configurator import Configurator
from ..connector import Connector
from ..writer import Writer
from click import echo
import getpass


class ListCommand(Command):
    def run(self, **kwargs):
        lconf = Configurator()
        writer = Writer()

        cases = Connector(username=lconf.get_value('username'),
                          url=lconf.get_value('url'),
                          password=getpass.getpass(prompt='Enter password for user: ')).list_cases()

        writer.write_cases(cases)
