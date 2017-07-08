from click import echo
from termcolor import colored


class Writer:
    """This class handles output"""

    def __init__(self):
        self.tlps = ['TLP:WHITE', 'TLP:GREEN', 'TLP:AMBER', 'TLP:RED\t']
        self.severities = ['LOW', 'MID', 'HIGH']
        self.colormap = [self.white, self.green, self.amber, self.red]

    def write_cases(self, cases):
        echo('####\tTLP\t\tSev.\tOwner\t\tTitle')
        echo('----\t---\t\t----\t-----\t\t-----')
        for case in cases:
            echo('{}\t{}\t{}\t{}\t\t{}'.format(case.get('caseId'),
                                               self.tlp(case.get('tlp')),
                                               self.severity(case.get('severity')),
                                               case.get('owner'),
                                               case.get('title')))

    def tlp(self, t_num):
        return self.colormap[t_num](self.tlps[t_num])

    def severity(self, s_num):
        return self.colormap[s_num](self.severities[s_num-1])

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
