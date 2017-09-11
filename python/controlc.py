#!/usr/bin/env python
import signal, sys, time
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
while True:
    print("waiting for control c...")
    time.sleep(1)
#signal.pause()
