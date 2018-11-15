import sys
import time
import random 
typing_speed = 50 #typing speed
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
        #time.sleep(0.2)
    print()

slow_type('printing it slow')