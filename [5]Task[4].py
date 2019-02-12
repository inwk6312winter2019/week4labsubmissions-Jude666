class time(object):
    'this is time'

t1 = time()
t1.hour = 6
t1.minute = 13
t1.second = 45

t2 = time()
t2.hour = 6
t2.minute = 13
t2.second = 44
def is_after(t1, t2):
    t1_total = (t1.hour * 3600) + (t1.minute * 60) + t1.second
    t2_total = (t2.hour * 3600) + (t2.minute * 60) + t2.second
    return t1_total > t2_total

print(is_after(t1, t2))
