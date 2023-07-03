import sys
import json
import time

from log_lib import log
from gpio_lib import set_pin


def flip(device_name, desired_state):
  log(f"Switching device {device_name} to status {desired_state}") 
  pin = config[device_name]['pin']
  on_state = config[device_name]['on_state']

  if desired_state == 'on':
    value = on_state
  elif desired_state.isdigit():
    value = on_state
  else:
    value = not on_state

  set_pin(pin, value)

  if desired_state.isdigit():
    time.sleep(int(desired_state))
    set_pin(pin, not value)


fh = open('/opt/relay/relays.json', 'r')
config = json.loads(fh.read())
fh.close()

try:
  device_name = sys.argv[1]
except:
  device_name = None

try:
  desired_state = sys.argv[2]
except:
  desired_state = 'off'

if device_name is None:
  for device_name in config:
    flip(device_name, desired_state)
else:
  flip(device_name, desired_state)
