#threadsafe consumer producer pipeline

from random import random
import random
import time
import concurrent.futures
import threading

FINISH='the end'

class Pipeline:
    def __init__(self,capacity):
        self.capacity=capacity
        self.message=None
        self.producer_lock=threading.Lock()
        self.consumer_lock=threading.Lock()
        self.consumer_lock.acquire()
        
    def set_message(self, message):
        print(f'producing message of {message}')
        producer_pipeline.append(message)
        self.producer_lock.acquire()
        self.message=message
        self.consumer_lock.release()

    def get_message(self):
        print(f'cosuming message of {self.message}')
        self.consumer_lock.acquire()
        message=self.message
        self.producer_lock.release()
        consumer_pipeline.append(message)
        return message


def Producer(pipeline):
    for _ in range(pipeline.capacity):
        message=random.randint(1,100)
        pipeline.set_message(message)
    
    pipeline.set_message(FINISH)

def Consumer(pipeline):
    message=None
    while message is not FINISH:
        message=pipeline.get_message()
        if message is not FINISH:
            time.sleep(random.random())

producer_pipeline=[]
consumer_pipeline=[]
if __name__=="__main__":
    pipeline=Pipeline(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:
        e.submit(Producer, pipeline)
        e.submit(Consumer, pipeline)

    print(f'producer:{producer_pipeline}')
    print(f'consumer:{consumer_pipeline}')