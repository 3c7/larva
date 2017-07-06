from thehive4py import api as thehiveapi


class AuthenticationError(Exception):
    pass


class NoUsernameGivenError(Exception):
    pass


class NoURLGivenError(Exception):
    pass


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
            raise NoUsernameGivenError()

        if not url:
            raise NoURLGivenError()

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
            raise AuthenticationError('Could not login as {}.'.format(self.username))
        return cases.json()
