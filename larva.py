import click
from configurator import Configurator
import json
from commander import Commander

commander = Commander()

# LARVA
@click.group()
def larva():
    """
    The commandline client to TheHive.

    If you find any bugs, please make sure to report them on https://github.com/3c7/larva/issues
    """
    pass


@click.command(name='list')
def list_cases(**kwargs):
    """This lists all cases. Some options will get added, soon."""
    commander.commands['list'].run()



@click.group()
def config():
    """Manage larva configuration"""
    pass


# CONFIG
@click.command()
@click.option('--set', 'mode_set', type=str, help='Set an username', default=False)
def username(mode_set):
    """Get and set username"""
    commander.commands['config'].run(type='username',
                                     mode_set=mode_set)


@click.command()
@click.option('--set', 'mode_set', type=str, help='Set an url', default=False)
def url(mode_set):
    """Get and set url"""
    commander.commands['config'].run(type='url',
                                     mode_set=mode_set)


@click.command(name='get')
def get_config():
    """Dump the configuration file"""
    commander.commands['config'].run(dump=True)

@click.command(name='clear')
def clear_config():
    """Clears the configuration file"""
    commander.commands['config'].run(clear=True)


# Add cmds to groups
larva.add_command(list_cases)
larva.add_command(config)
config.add_command(username)
config.add_command(url)
config.add_command(get_config)
config.add_command(clear_config)

if __name__ == '__main__':
    larva()
