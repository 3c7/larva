import click
from sys import exit
import getpass
from color import Colorizer
from configurator import Configurator
from connector import Connector
import json


# LARVA
@click.group()
def larva():
    """
    The commandline client to TheHive.

    If you find any bugs, please make sure to report them on https://github.com/3c7/larva/issues
    """
    pass


@click.command(name='list')
def list_cases():
    """This lists all cases. Some options will get added, soon."""
    lconf = Configurator()

    if not lconf.get_value('username'):
        click.echo('No username given. Please set an username via `larva config username [USER]`')
        exit(1)

    if not lconf.get_value('url'):
        click.echo('No url given. Please set an username via `larva config url [URL]`')
        exit(1)

    cases = Connector(username=lconf.get_value('username'),
                      url=lconf.get_value('url'),
                      password=getpass.getpass(prompt='Enter password for user: ')).list_cases()

    click.echo('TLP\t\tSev.\tOwner\t\tTitle')
    click.echo('---\t\t----\t-----\t\t-----')
    for case in cases:
        click.echo('{}\t{}\t{}\t\t{}'.format(Colorizer.tlp(case.get('tlp')),
                                             Colorizer.severity(case.get('severity')),
                                             case.get('owner'),
                                             case.get('title')))


@click.group()
def config():
    """Manage larva configuration"""
    pass


# CONFIG
@click.command()
@click.option('--set', type=str, help='Set an username', default='')
def username(set):
    """Get and set username"""
    lconf = Configurator()

    if set == '':
        click.echo(lconf.get_value('username'))
        return

    lconf.set_value('username', set)
    lconf.save()


@click.command()
@click.option('--set', type=str, help='Set an url', default='')
def url(set):
    """Get and set url"""
    lconf = Configurator()

    if set == '':
        click.echo(lconf.get_value('url'))
        return

    lconf.set_value('url', set)
    lconf.save()


@click.command(name='get')
def get_config():
    """Dump the configuration file"""
    click.echo(json.dumps(Configurator().config, indent=4))



# Add cmds to groups
larva.add_command(list_cases)
larva.add_command(config)
config.add_command(username)
config.add_command(url)
config.add_command(get_config)

if __name__ == '__main__':
    larva()
