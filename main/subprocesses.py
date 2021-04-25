import signal

import os

import time

import subprocess

# able to run shell script

# run on same thread
subprocess.run("ls", stdout=subprocess.PIPE, shell=True)

# run on difference process
process = subprocess.Popen("ls",shell=True, preexec_fn=os.setsid)
time.sleep(20)

# kill process
os.killpg(os.getpgid(process.pid), signal.SIGTERM)