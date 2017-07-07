from .command import Command
from configurator import Configurator
from connector import Connector
from writer import Writer
from click import echo
import getpass


class ListCommand(Command):
    def run(self, **kwargs):
        lconf = Configurator()
        writer = Writer()

        if not lconf.get_value('username'):
            echo('No username given. Please set an username via `larva config username [USER]`')
            exit(1)

        if not lconf.get_value('url'):
            echo('No url given. Please set an username via `larva config url [URL]`')
            exit(1)

        cases = Connector(username=lconf.get_value('username'),
                          url=lconf.get_value('url'),
                          password=getpass.getpass(prompt='Enter password for user: ')).list_cases()

        writer.write_cases(cases)