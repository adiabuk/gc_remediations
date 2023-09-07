import sys
import subprocess
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["NetDevAlive"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class NetDevAlive(Action):
    def run(self, down_device):
        print(f"Checking to see if risk is too high")
        command = '/opt/nagios_checks/check_nrpe -t30 -H {down_device} -c get_risk'
        results = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        risk = float(results.stdout.read().decode())

        return int(risk < 2)

