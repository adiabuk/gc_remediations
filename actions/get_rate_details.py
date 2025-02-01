import sys
from st2common.runners.base_action import Action
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


__all__ = ["GetRateDetails"]

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class GetRateDetails(Action):

    def run(self, service):
        print("Fetching details from service name")
        direction, env, _ = service.split('_')
        class dictObject(object): pass
        my_dict = dictObject()
        my_dict.direction = direction
        my_dict.env = env
        results = dict(my_dict)
        for k, v in my_dict.items():
            print(f"Found {k}, {v}")
        return mydict.__dict__
