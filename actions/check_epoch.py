import sys
import subprocess
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["EpochFresh"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class EpochFresh(Action):
    def run(self, down_device, down_service):
        print(f"Checking if epoch of stream data is fresh")
        interval = down_service.split()[-1]
        port_mapping = {"1m":  [5001,60,120],
                        "5m":  [5002,300,350],
                        "15m": [5003,910,940],
                        "30m": [5004,1830,1900],
                        "1h":  [5005,3600,3660],
                        "4h":  [5006,14400,1460]}
                        #"12h": [5007,
                        #"1d":  [5007}
        port, warning, critical = port_mapping[interval]
        command = f'/opt/nagios_checks/check_milliepoch -u https://{down_device}:{port} -w {warning} -c {critical}'
        results = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        outcome = results.stdout.read().decode().split[0]
        result = bool(outcome == 'OK')

        if not result:
            sys.exit(1)

        return result