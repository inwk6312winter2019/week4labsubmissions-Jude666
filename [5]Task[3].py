class time(object):
    "this is class time"

def print_time(timer):
    print('hour:%2d, minute:%2d, second:%2d' %(timer.hour,timer.minute,timer.second))
timer = time()
time.hour = 7
time.minute = 34
time.second = 59
print_time(timer)
