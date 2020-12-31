import threading
from threading import Lock

class Counter:
    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        for _ in range(200000):
            # カウントアップが必ず同期される
            with self.lock:
                self.count += 1

counter = Counter()

def do_increment(counter):
    counter.increment()

threads = []

for _ in range(5):
    x = threading.Thread(target=do_increment, args=(counter, ))
    threads.append(x)
    x.start()

for t in threads:
    t.join()

print(counter.count)