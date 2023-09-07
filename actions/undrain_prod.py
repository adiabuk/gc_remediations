import sys
import subprocess
from st2common.runners.base_action import Action
from nornir import InitNornir
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["UndrainProd"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class UndrainProd(Action):
    def run(self, down_device):
        print(f"draining prod env")
        command = '/opt/nagios_checks/check_nrpe -t30 -H {down_device} -c undrain_prod'
        subprocess.Popen(command.split(), stdout=subprocess.PIPE)

        return 0

