import threading 

lock=threading.Lock()
lock.acquire()
print(lock)
lock.release()
print(lock)