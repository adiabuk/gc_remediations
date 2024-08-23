import sys
import subprocess
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["Check137"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Check137(Action):
    def run(self, down_device):
        print(f"Checking to see if any containers exited with 137")
        command = f'/opt/nagios_checks/check_nrpe -2 -t30 -H {down_device} -c check_container_status'
        results = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        stdout = results.stdout.read().decode()
        results.wait()
        try:
            containers = float(stdout.split()[-1])
        except ValueError:
            print(f"Unable to decode output: {stdout}")
            sys.exit(9)
        result = bool(containers == 0)
        print(f"Number of is 137 containers is {containers}")

        if not result:
            sys.exit(1)

        return result
