import os
import time

ret = os.fork()

if ret == 0:
    print('children')
    time.sleep(5)
    print('children over')
else:
    print('parent')
    time.sleep(3)

