import sys
import subprocess
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["TestRule"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class TestRule(Action):
    def run(self, result):
        print(f"Rule to test result")
        return result

