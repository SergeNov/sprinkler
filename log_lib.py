import datetime
import json

def log(message, data = None):
  now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  print(f"{now} {message}")
  if data is not None:
    print(json.dumps(data, indent=2))
