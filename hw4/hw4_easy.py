import time
from threading import Thread
from multiprocessing import Process


def fib(x):
    if x < 0:
        return None
    fibs = [0] * (x + 1)
    fibs[0] = 0
    fibs[1] = 1
    for i in range(2, x + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[x]


def runSimple(n):
    start = time.time()
    for _ in range(10):
        fib(n)
    return f"Simple: {time.time() - start}\n"


def runThreads(n):
    thds = []
    start = time.time()
    for _ in range(10):
        t = Thread(target=fib, args=(n,))
        thds.append(t)
        t.start()
    for thd in thds:
        thd.join()
    return f"Threads: {time.time() - start}\n"


def runProc(n):
    pcs = []
    start = time.time()
    for _ in range(10):
        t = Process(target=fib, args=(n,))
        pcs.append(t)
        t.start()
    for pc in pcs:
        pc.join()
    return f"Processes: {time.time() - start}\n"


if __name__ == "__main__":
    w = int(10 ** 5)
    with open("artifacts/easy", 'w') as f:
        f.write(runSimple(w))
        f.write(runThreads(w))
        f.write(runProc(w))
