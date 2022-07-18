import time
import threading
import concurrent.futures

def myfunc(name):
    print(f'my func1 started with {name}')
    time.sleep(10)
    print('myfunc1 ended')


if __name__=='__main__':
    print('main begin')
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
        e.map(myfunc, ['foo', 'bar', 'bash',])
    print('main ends')