import commands
import time
from datetime import datetime

LOCK_FILE = "/var/log/auth.log"
LAST_LOCK_TIME_STR = "unlocked login keyring"
HOSTNAME = "brownrp1-mint-dev"
SLEEP_SEC = 40
LOCK_INTERVAL_MIN = 20
LOCK_CMD = "gnome-screensaver-command -l"

def parseDateFromLine(line):
    index = line.find(HOSTNAME)
    if(index == -1):
        return ""

    line = line[:index].strip()
    return line

def readLockFile():
    f = open(LOCK_FILE, "r")
    lines = f.readlines()
    f.close()
    return lines

def findLastUnlockTime():
    lines = readLockFile()
    lines.reverse()
    for i in lines:
        if(i.find(LAST_LOCK_TIME_STR) != -1):
            return parseDateFromLine(i)

def lockComputer():
    print commands.getoutput(LOCK_CMD)

def main():
    while(1):
        last = findLastUnlockTime()
        lastDate = datetime.strptime(last + " 2017", '%b %d %H:%M:%S %Y')
        now = datetime.now()
        diff = now - lastDate
        lastMin = diff.total_seconds() / 60
        print("It is currently %s and the last unlock was at %s, %d minutes ago." % (now, last, lastMin))
        if(lastMin > LOCK_INTERVAL_MIN):
            print("Time for a break!")
            time.sleep(2)
            lockComputer()
        time.sleep(SLEEP_SEC)

main()
