from thehive4py import api as thehiveapi
from .exceptions import *

class Connector:
    """
    This basically decorates TheHive4Py and adds some functionality in order to slim larva.py

    :param username:
    :param password:
    :param url:
    :param proxies:
    """
    def __init__(self, username, password, url, proxies=None):
        if not username:
            raise NoUsernameGivenError('no username given. Please add an username through the config subcommand.')

        if not url:
            raise NoURLGivenError('no url given. Please add an url through the config subcommand.')

        self.username = username
        self.api = thehiveapi.TheHiveApi(username=username,
                                         password=password,
                                         url=url,
                                         proxies=proxies)

    def list_cases(self, **kwargs):
        """

        :param kwargs:
        :return: list of cases
        :rtype: dict
        """
        cases = self.api.find_cases(query={'_string': 'title: *'},
                                    sort=['-caseId'])

        if cases.status_code != 200:
            raise AuthenticationFailureError('Could not login as {}.'.format(self.username))
        return cases.json()
