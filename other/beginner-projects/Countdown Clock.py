import time
import re

def clock(t):
    current_time = time.time()
    while clock_t > current_time:
        delta = clock_t - current_time
        hours_to = delta // (60*60)
        mins_to = delta // 60 - hours_to*60
        sec_to = delta - hours_to*60*60 - mins_to*60
        sec_to = round(sec_to)
        print('Hours: ' + str(hours_to) + '. Mins: ' + str(mins_to) + '. Seconds: ' + str(sec_to))
        time.sleep(5)
        current_time = time.time()

print('Enter time: ')
inp = input()

tmatch = re.search(r'(\d\d)[:.](\d\d)', inp)
hours = int(tmatch[1])
mins = int(tmatch[2])

t = time.localtime()
clock_t = time.mktime((t[0], t[1], t[2], hours, mins, 0, t[6], t[7], t[8]))

current_time = time.time()
if clock_t < current_time:
    print('Overdue')
else:
    clock(clock_t)
