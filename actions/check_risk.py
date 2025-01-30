import sys
import subprocess
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["CheckRisk"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class CheckRisk(Action):
    def run(self, down_device, env):
        print(f"Checking to see if risk is too high in {env}")
        command = f'/opt/nagios_checks/check_nrpe -2 -t10 -H {down_device} -c get_risk_{env}'
        results = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        stdout = results.stdout.read().decode()
        results.wait()
        try:
            risk = float(stdout.split()[-1])
        except ValueError:
            print(f"Unable to decode output: {stdout}")
            sys.exit(9)
        result = bool(risk > 1.5)
        print(f"Risk is {risk}, result={result} for {env}")

        if not result:
            sys.exit(1)

        return result
