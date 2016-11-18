import time

class Time(object):

    @classmethod
    def fromtimestamp(cls, t):
        y, m, d, hh, mm, ss, weekday, jday, dst = time.localtime(t)
        return hh, mm, ss

    @classmethod
    def today(cls):
        t = time.time()
        return cls.fromtimestamp(t)

while True:
    print(Time.today())
    time.sleep(1)
