import sys
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["CheckDirection"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class CheckDirection(Action):

    @staticmethod
    def check_result(result):
        """
        get exit code from bool result
        """
        return 0 if result else 9

    def run(self, direction):
        print("Try to determine direction")
        url = "http://jenkins:9090/api/v1/query"
        query = 'sum({__name__ =~ "tv_all_value_.*"})'
        value = requests.post(f'{url}?query={query}',
                              timeout=10).json()['data']['result'][0]['value'][-1]
        result = False
        if direction == 'long':
            result = float(value) > 0
        if direction == 'short':
            result = float(value) < 0
        if direction == 'neutral':
            result = float(value) == 0

        print(f"result is {str(result)}")
        sys.exit(self.check_result(result))
