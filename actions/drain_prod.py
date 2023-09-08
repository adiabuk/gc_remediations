import sys
import subprocess
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["DrainProd"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class DrainProd(Action):
    def run(self, down_device):
        print(f"draining prod env")
        command = f'/opt/nagios_checks/check_nrpe -t30 -H {down_device} -c drain_prod'
        subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        print("Prod drained")
        return 0

