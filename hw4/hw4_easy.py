import concurrent
import time
from concurrent.futures import ThreadPoolExecutor


def fib(x):
    if x < 0:
        return None
    fibs = [0] * (x + 1)
    fibs[0] = 0
    fibs[1] = 1
    for i in range(2, x + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[x]


def runThreads(n):
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        fs = []
        for i in range(10):
            fs.append(executor.submit(fib, n))
        return f"Threads: {time.time() - start}\n"


def runProc(n):
    start = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        fs = []
        for i in range(10):
            fs.append(executor.submit(fib, n))
        return f"Processes: {time.time() - start}\n"


if __name__ == "__main__":
    w = int(1e5)
    with open("artifacts/easy", 'w') as f:
        f.write(runThreads(w))
        f.write(runProc(w))
