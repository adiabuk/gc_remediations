import sys
import subprocess
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["Swap"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Swap(Action):
    def run(self, down_device):
        print(f"Checking to see if swap is available")
        command = f"/opt/nagios_checks/check_nrpe -t30 -H {down_device} -c check_swap -a 30 10|awk {'print $4'}|tr -d %"
        results = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        swap = float(results.stdout.read().decode())
        result = bool(swap > 0)  # > 0% available
        print(f"swap is {swap}, result={result}")

        if not result:
            sys.exit(1)

        return result

