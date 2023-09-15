import sys
import subprocess
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["EnableSwap"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class EnableSwap(Action):
    def run(self, down_device):
        print(f"draining prod env")
        command = f'ssh -p 2222 amro@{down_device} "sudo swapon /swapfile" '
        subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        print("swap enabled")
        return 0

