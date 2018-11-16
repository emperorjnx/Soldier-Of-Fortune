import sys
import time
import random 

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*0.1)
    print()

def slow_type1(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*0.25)
    print()

slow_type('printing it slow')
slow_type1('printing it slow i know you love to read')