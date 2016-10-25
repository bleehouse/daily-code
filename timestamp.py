from datetime import datetime
import time

#def log(message, when=datetime.now()):
#    print('%s: %s' %(when, message))

def log(message, when=None):
    when = datetime.now() if when is None else when
    print('%s: %s' %(when, message))

log('Hi there!')
time.sleep(0.1)
log('Hi again!')
