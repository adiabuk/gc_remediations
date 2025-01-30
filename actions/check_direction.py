import sys
import subprocess
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["CheckDirection"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class CheckDirection(Action):
    def run(self, direction):
        print(f"Try to determine direction")
        url = "http://jenkins:9090/api/v1/query"
        query = 'sum({__name__ =~ "tv_all_value_.*"})'
        value = requests.post(f'{url}?query={query}',
                              timeout=10).json()['data']['result'][0]['value'][-1]

        if direction == 'long':
            return float(value) > 0
        if direction == 'short':
            return float(value) < 0
        if direction == 'neutral':
            return float(value) == 0
