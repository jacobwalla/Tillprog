""" import utime
print("Loop starting!")
while True:
    print("Loop running!")
    utime.sleep(1)
print("Loop finished!") """

""" user_name = input ("What is your name?")
if user_name == "Clark Kent":
 print("You are Superman!")
else:
 print("You are not Superman!") """

""" user_name = input ("What is your name?")
while user_name != "Clark Kent":
    print("You are not Superman - try again!")
    user_name = input("What is your name? ")
print("You are Superman!") """

import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    led_onboard.toggle()
    utime.sleep(0.5)