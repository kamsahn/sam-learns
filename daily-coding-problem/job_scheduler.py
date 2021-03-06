"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""

import time

class JobScheduler():
    def __init__(self, f, n):
        """
        :param f: function,
        :param n: int, time in milliseconds
        """
        self.f = f
        self.n = n

    def schedule(self):
        time.sleep(n/1000)  # python wait n milliseconds
        self.f()


def say_hello():
    print('Hello!')

n = 1000

js = JobScheduler(say_hello, n)
js.schedule()