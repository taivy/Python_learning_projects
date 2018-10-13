def checkio(first, second):
    l = []
    first = first.split(',')
    second = second.split(',')
    for i in first:
        if i in second:
            l.append(i)
    l.sort()
    return ','.join(l)

if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
