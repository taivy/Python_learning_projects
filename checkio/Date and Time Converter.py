def date_time(time: str) -> str:
    dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    time = time.split(' ')

    ymd = time[0].split('.')
    y = ymd[2]
    month = ymd[1]
    d = ymd[0]

    hm = time[1].split(':')
    hours = hm[0]
    mins = hm[1]

    if hours == '01':
        h = 'hour'
    else:
        h = 'hours'

    if mins == '01':
        m = 'minute'
    else:
        m = 'minutes'

    result = str(int(d)) + ' ' + dict[int(month)] + ' ' + y + ' year ' + str(int(hours)) + ' ' + h + ' ' + str(
        int(mins)) + ' ' + m

    return result