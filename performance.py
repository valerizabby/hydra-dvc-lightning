import numpy as np 
import time
from typing import Callable

from meanvector import MeanVector

def test_timings(func: Callable, *args):
    _ = func(*args)
    start_time = time.time()
    _ = func(*args)
    end_time = time.time()
    return round(end_time - start_time, 5)


if __name__ == "__main__":
    for length in [5, 25, 125, 625, 3125, 15625, 78125]:
        v = np.random.rand(length)
        print("Mean vector (Pure C++), size={0}: {1} seconds".format(length, test_timings(MeanVector.meanVector, v)))
        print("Mean vector (Python numpy), size={0}: {1} seconds\n".format(length, test_timings(np.mean, v)))