import signal

import os

import time

import subprocess

# able to run shell script

def run_on_same_thread():
    subprocess.run("ls", stdout=subprocess.PIPE, shell=True)

# run on difference process
def run_on_different_process():
    process = subprocess.Popen("ls && sleep 5",shell=True, preexec_fn=os.setsid)
    time.sleep(1)
    poll = process.poll()
    if poll is None:
        print("running")
    else:
        print(f"not running {poll}")
    # kill process
    os.killpg(os.getpgid(process.pid), signal.SIGTERM)




if __name__ == '__main__':
    run_on_different_process()