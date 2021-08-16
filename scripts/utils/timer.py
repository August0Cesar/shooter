import time


class Timer:
    def __init__(self, value=0):
        self.start = time.time()
        self.set(value)
    
    def reset(self):
        self.set(0)

    def set(self, value: float):
        self.start = time.time() - value

    def get(self) -> float:
        return time.time() - self.start
    
    def __str__(self):
        value = self.get()
        seconds = int(value)
        milisegundos = int((value - seconds) * 1000)

        minutes = int(seconds / 60)
        seconds -= minutes * 60
        return f'{minutes}m {seconds}s {milisegundos}ms'