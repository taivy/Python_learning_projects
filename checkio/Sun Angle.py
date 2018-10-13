def sun_angle(time):
    time = time.split(':')
    h = int(time[0]) - 6
    m = int(time[1])
    if 0 <= h < 12:
        h = h * 60
        ttime = h + m
        angle = ttime * 0.25
        return angle
    elif h == 12 and m == 0:
        return 180
    else:
        s = """I don't see the sun!"""
        return s


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"