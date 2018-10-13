def time_converter(time):
    time = time.split(' ');
    hours = time[0].split(':')[0]
    mins = time[0].split(':')[1]
    if time[1] == 'p.m.':
        if hours == '12':
            result = hours + ':' + mins
        else:
            result = str(12 + int(hours)) + ':' + mins
    elif time[1] == 'a.m.':
        if len(str(hours)) == 1:
            hours = '0' + hours
        if hours == '12':
            result = '00:' + mins
        else:
            result = hours + ':' + mins
    print(time, result)
    return result