import importlib
import traceback
import time


my_module = importlib.import_module('printstuff')
while 1:
    try:
        # python 2 way to do this
        reload(my_module)
        print("Trying to print stuff..")
        my_module.printstuff()
    except Exception as e:
        exc = traceback.format_exc()
        print(exc)
    time.sleep(5)
