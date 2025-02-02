from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["CheckRate"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class CheckRate(Action):

    def run(self, environment, direction):
        print(f"Check current rate for {direction} in {environment} env")
        url = "http://jenkins:9090/api/v1/query"
        query = f'rate({{__name__=~"open_net_perc_{direction}_trades_{environment}"}}[10m])'
        value = requests.post(f'{url}?query={query}',
                              timeout=10).json()['data']['result'][0]['value'][-1]
        print(value)
        return float(value)
