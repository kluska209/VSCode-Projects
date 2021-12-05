from rich.console import Console
import rich.traceback
import time
import functools
import numpy as np
import random

console = Console()
console.clear()
rich.traceback.install()

def upper_decorator(reps = 1):
    def lower_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            avg = np.array([])

            for rep in range(reps):
                start_time = time.time()
                func(*args, **kwargs)
                finish_time = time.time()-start_time
                console.print('Function took ', finish_time, ' sec')
                avg = np.append(avg, finish_time)
            
            console.print('Average time: ', np.average(avg), ' sec')

        return wrapper
    return lower_decorator

@upper_decorator(reps = 3)
def func(): #funkcja tworząca losową siatkę spinów
    lattice = np.zeros((1000,1000))
    options = [-1,1]

    for i in range(1000):
        for j in range(1000):
            result = random.choices(options, weights=[8,2])
            lattice[i][j] = int("".join([str(e) for e in result])) 

func()
