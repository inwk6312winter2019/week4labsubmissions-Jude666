class time:
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

def int_to_time(seconds):
    time1 = time()
    minutes, time1.second = divmod(seconds, 60)
    time1.hour, time1.minute = divmod(minutes, 60)
    return time1

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def increment(time, seconds):
    assert valid_time(time)
    seconds += time.time_to_int()
    return int_to_time(seconds)

def main():
    t=time()
    t.hour=9
    t.minute=36
    t.second=27
    time1=increment(t,150)
    print("Incremented time is : %.2d:%.2d:%.2d" %(time1.hour,time1.minute,time1.second))


if __name__ == '__main__':
main()
