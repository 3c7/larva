from termcolor import colored


TLP = ['TLP:WHITE', 'TLP:GREEN', 'TLP:AMBER', 'TLP:RED\t']
SEVERITY = ['LOW', 'MID', 'HIGH']


class Colorizer:


    @staticmethod
    def red(string):
        return colored(string, 'red')

    @staticmethod
    def amber(string):
        return colored(string, 'yellow')

    @staticmethod
    def green(string):
        return colored(string, 'green')

    @staticmethod
    def white(string):
        return colored(string, 'white')

    @staticmethod
    def tlp(tlp_num):
        colors = [Colorizer.white, Colorizer.green, Colorizer.amber, Colorizer.red]
        return colors[tlp_num](TLP[tlp_num])

    @staticmethod
    def severity(s_num):
        colors = [Colorizer.white, Colorizer.green, Colorizer.amber, Colorizer.red]
        return colors[s_num](SEVERITY[s_num-1])