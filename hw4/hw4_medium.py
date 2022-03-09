from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import time
import math
from copy import copy


def integrate(f, a, b, *, n_jobs=1, n_iter=10 ** 7):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrateThreads(f, a, b, n_jobs=1):
    fs = []
    executor = ThreadPoolExecutor(max_workers=n_jobs)
    intervals = (b - a) / n_jobs
    left = a
    right = a + intervals

    for i in range(n_jobs):
        fs.append(executor.submit(integrate, f, left, right))
        left = copy(right)
        right = right + intervals
    return sum([fut.result() for fut in fs])


def integrateProcesses(f, a, b, n_jobs=1):
    fs = []
    executor = ProcessPoolExecutor(max_workers=n_jobs)
    intervals = (b - a) / n_jobs
    left = a
    right = a + intervals

    for i in range(n_jobs):
        fs.append(executor.submit(integrate, f, left, right))
        left = copy(right)
        right = right + intervals
    return sum([fut.result() for fut in fs])


if __name__ == "__main__":
    l = 0
    r = math.pi / 2
    p = 1
    fun = math.cos
    with open("artifacts/medium", 'w') as file:
        for p in range(1, 24):
            file.write(f"jobs: {p}\n")
            start = time.time()
            file.write(f"basic: {integrate(fun, l, r)}\n")
            basic = time.time()
            file.write(f"thread: {integrateThreads(fun, l, r, p)}\n")
            threading = time.time()
            file.write(f"process: {integrateProcesses(fun, l, r, p)}\n")
            processing = time.time()
            file.write(f'basic: {basic - start}\n')
            file.write(f'threading: {threading - basic}\n')
            file.write(f'processing: {processing - threading}\n')
