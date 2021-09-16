import time


class Timer:
    def __init__(self, value=0):
        self._stop = False
        self._current_time = None
        self.start = time.time()
        self.set(value)
    
    @property
    def current_time(self):
        return int(self._current_time)

    @property
    def stop(self):
        return  self._stop

    @stop.setter
    def stop(self, stop):
         self._stop = stop


    def reset(self):
        self.set(0)

    def set(self, value: float):
        self.start = time.time() - value

    def get(self) -> float:
        if not  self._stop:
            self._current_time = time.time() - self.start
        return self._current_time
    
    def __str__(self):
        value = self.get()
        seconds = int(value)
        # milisegundos = int((value - seconds) * 1000)

        minutes = int(seconds / 60)
        seconds -= minutes * 60
        # return f'{minutes}m {seconds}s {milisegundos}ms'
        if minutes < 10:
            minutes_str = f'0{minutes}'
        else:
            minutes_str = str(minutes)
        if seconds < 10:
            seconds_str = f'0{seconds}'
        else:
            seconds_str = str(seconds)
        return f'{minutes_str}:{seconds_str}'