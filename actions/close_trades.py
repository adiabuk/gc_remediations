import sys
import time
import subprocess
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["CloseTrades"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class CloseTrades(Action):
    def run(self, down_device, environment, direction):
        threshold = 1
        print(f"closing {direction} trades in {environment} over {threshold}%")
        command = (f'/opt/nagios_checks/check_nrpe -2 -t30 -H {down_device} -c close_trades '
                   f'-a {environment} {direction} {threshold}')
        p = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            # Filter stdout
            for line in iter(p.stdout.readline, ''):
                sys.stdout.flush()
                # Print status
                print(">>> " + line.rstrip())
                sys.stdout.flush()
        except:
            sys.stdout.flush()

        # Wait until process terminates (without using p.wait())
        while p.poll() is None:
            # Process hasn't exited yet, let's wait some
            time.sleep(0.5)
        return {'return_code': p.returncode, 'stdout': p.stdout,  'stderr': p.stderr}
