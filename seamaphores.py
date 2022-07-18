from pprint import pprint
import threading


sem=threading.Semaphore(value=10)

sem.acquire()
sem.acquire()

print(sem._value)

sem.release()

print(sem._value)