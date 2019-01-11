"""
@author: P_k_y
"""


class Timer:
    def __init__(self):
        self._second = 0
        self._minute = 0
        self._hour = 0
        self.time_passed = 0

    def elapse_second(self, second):
        self._second += second
        if self._second >= 60:
            self._minute += 1
            self._second -= 60
        if self._minute == 60:
            self._hour += 1
            self._minute = 0

    def update_timer(self, time_passed):
        self.time_passed += time_passed
        self.elapse_second(self.time_passed // 1000)
        self.time_passed %= 1000

    def get_second(self):
        return self._second

    def get_minute(self):
        return self._minute

    def get_hour(self):
        return self._hour

    def set_time(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second



