#!/usr/bin/env python3

from subprocess import run, PIPE
from time import strftime

run(["paru", "-Syuu"])

username = run(['whoami'], stdout=PIPE, text=True).stdout.strip()
time_now = strftime("%H:%M:%S")

print(f"Hello, {username}!")
print(f"Current time: {time_now}")
