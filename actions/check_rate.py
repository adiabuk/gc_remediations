#pylint: disable=syntax-error
import sys
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["CheckRate"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class CheckRate(Action):

    @staticmethod
    def check_result(result):
        """
        get exit code from bool result
        """
        return 0 if result else 9

    def run(self, environment, direction):
        print("Check current rate")
        url = "http://jenkins:9090/api/v1/query"
        query = f'rate({__name__=~"open_net_perc_{direction}_trades_{env}"}[10m])'
        value = requests.post(f'{url}?query={query}',
                              timeout=10).json()['data']['result'][0]['value'][-1]
        print(value)
        return value
