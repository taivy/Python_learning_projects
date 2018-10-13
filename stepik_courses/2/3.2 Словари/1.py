def update_dictionary(d, key, value):
    value = [value]
    if key in d:
        dl = d[key]
        dl.append(value[0])
    elif key not in d:
        key2 = key * 2
        if key2 in d:
            dl = d[key2]
            dl.append(value[0])
        else:
            d[key2] = value
