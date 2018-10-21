url = 'https://py.checkio.org/en/mission/hacker-language/'

import re


class HackerLanguage:
    def __init__(self):
        self.message = ''
        self.encrypted = ''
        self.exceptions = ['.', ':', '!', '?', '@', '$', '%']
        for i in range(10):
            self.exceptions.append(i)

    def convert(self, text):
        enc = ''
        pattern1 = r'(\d\d:\d\d)'
        pattern2 = r'(\d\d\.\d\d\.\d\d\d\d)'
        patterns = [pattern1, pattern2]
        ranges = []
        i = 0
        for pattern in patterns:
            for m in re.finditer(pattern, text):
                ranges.append(m.span())
        ranges.sort(key=self.sort_start)
        if ranges != []:
            for j in range(len(ranges)):
                r = ranges[j]
                end = r[0]
                next_start = r[1]
                while i < end:
                    if text[i] == ' ':
                        enc += '1000000'
                        i += 1
                    elif text[i] not in self.exceptions:
                        enc += bin(ord(text[i]))[2:]
                        i += 1
                    else:
                        enc += text[i]
                        i += 1
                enc += text[r[0]:r[1]]
                i = next_start
            end = len(text)
            while i < end:
                if text[i] == ' ':
                    enc += '1000000'
                    i += 1
                elif text[i] not in self.exceptions:
                    enc += bin(ord(text[i]))[2:]
                    i += 1
                else:
                    enc += text[i]
                    i += 1
            print(enc)

        else:
            while i < len(text):
                if text[i] == ' ':
                    enc += '1000000'
                    i += 1
                elif text[i] not in self.exceptions:
                    enc += bin(ord(text[i]))[2:]
                    i += 1
                else:
                    enc += text[i]
                    i += 1
        return enc

    def write(self, m):
        msg = self.convert(m)
        self.encrypted += m
        self.message += msg

    def delete(self, n):
        print(self.message)
        n = -n
        symbols = self.encrypted[n:]
        self.encrypted = self.encrypted[:n]
        print(self.encrypted)
        print(symbols)
        enc = self.convert(symbols)
        end = len(self.message) - len(enc)
        print
        self.message = self.message[0:end]

    def send(self):
        print(self.message)
        return self.message

    def convert_bin(self, n):
        result = 0
        power = len(n) - 1
        for i in n:
            result += int(i) * 2 ** power
            power -= 1
        return result

    def sort_start(self, range):
        start, end = range[0], range[1]
        return start

    def read(self, text):
        dec = ''
        pattern1 = r'(\d\d:(?!1000000)\d\d)'
        pattern2 = r'(\d\d\.\d\d\.\d\d\d\d)'
        patterns = [pattern1, pattern2]
        ranges = []
        i = 0
        for pattern in patterns:
            for m in re.finditer(pattern, text):
                ranges.append(m.span())
        ranges.sort(key=self.sort_start)
        if ranges != []:
            for range in ranges:
                while i < range[0]:
                    if text[i] in self.exceptions:
                        dec += text[i]
                        i += 1
                    else:
                        substr = text[i:i + 7]
                        if substr == '1000000':
                            dec += ' '
                        else:
                            dec += str(chr(self.convert_bin(substr)))
                        i += 7
                dec += text[range[0]:range[1]]
                i = range[1]

        else:
            while i < len(text):
                if text[i] in self.exceptions:
                    dec += text[i]
                    i += 1
                else:
                    substr = text[i:i + 7]
                    if substr == '1000000':
                        dec += ' '
                    else:
                        dec += str(chr(self.convert_bin(substr)))
                    i += 7
        return dec


message = HackerLanguage()
message.write('Remember: 21.07.2018')
message.write(' at 11:11AM')
message.delete(1)
message.delete(1)
message.send()

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"
    print("Coding complete? Let's try tests!")
