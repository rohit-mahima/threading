from multiprocessing import RLock
import threading
from xml.dom.expatbuilder import theDOMImplementation

rlock=threading.RLock()

rlock.acquire()
rlock.acquire()

rlock.release()
print(rlock)

print(threading.current_thread())