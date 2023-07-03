import RPi.GPIO as GPIO

from log_lib import log

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def set_pin(pin_id, value):
  GPIO.setup(pin_id, GPIO.OUT)
  log(f"  Pin {pin_id} set to {value}")
  GPIO.output(pin_id, value)
