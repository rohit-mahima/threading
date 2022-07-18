import concurrent.futures
import time
import threading


class Account:
    def __init__(self):
        self.balance=1000
        self.lock=threading.Lock()

    def update(self, transaction, amount):
        print(f'{transaction} thread updating....')
        with self.lock:
            local_copy=self.balance
            local_copy+=amount
            time.sleep(1)
            self.balance=local_copy
        print(f'{transaction} thread finishing....')

if __name__=='__main__':
    account=Account()
    print(f'staring with balance of {account.balance}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:
        for transaction, amount in [('deposit', 2000),('withdraw',-150)]:
            e.submit(account.update, transaction, amount)

    print(f'ending balance of {account.balance}')