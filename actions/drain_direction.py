import sys
import time
import subprocess
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["DrainDirection"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class DrainDirection(Action):
    def run(self, direction, down_device, action):
        print(f"setting drain for {direction} to {action}")
        command = f'/opt/nagios_checks/check_nrpe -2 -t30 -H {down_device} -c drain_direction -a {str(action} {direction}'
        p = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            # Filter stdout
            for line in iter(p.stdout.readline, ''):
                sys.stdout.flush()
                # Print status
                print(">>> " + line.rstrip())
                sys.stdout.flush()
        except Exception:
            sys.stdout.flush()

        # Wait until process terminates (without using p.wait())
        while p.poll() is None:
            # Process hasn't exited yet, let's wait some
            time.sleep(0.5)
        return_code = p.returncode
        return return_code
