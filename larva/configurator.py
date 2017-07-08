from os.path import expanduser, join, isdir, isfile, dirname
from os import makedirs
import io
import json


class Configurator:
    """
    Configurator manages settings for larva and removes that ugly ini file
    """

    def __init__(self):
        self.configfile = join(expanduser('~'), '.config', 'larva', 'settings.json')
        self.config = {}
        self.load()

    def initfile(self):
        if isfile(self.configfile):
            return

        if not isdir(dirname(self.configfile)):
            makedirs(dirname(self.configfile))

        with io.open(self.configfile, 'w') as cfile:
            cfile.write(u'{}')

    def load(self):
        if not isfile(self.configfile):
            self.initfile()

        with io.open(self.configfile, 'r', encoding='utf8') as cfile:
            self.config = json.loads(cfile.read())

    def save(self):
        with io.open(self.configfile, 'w', encoding='utf8') as cfile:
            data = json.dumps(self.config, indent=4, ensure_ascii=False)
            cfile.write(unicode(data))

    def get_value(self, key):
        return self.config.get(key, None)

    def set_value(self, key, val):
        self.config.update({
            key: val
        })
