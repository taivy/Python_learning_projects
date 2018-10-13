VOWELS = "aeiou"

class Chat:
    def __init__(self):
        self.dialog = []

    def connect_human(self, obj):
        self.human = obj
        obj.chat = self

    def connect_robot(self, obj):
        self.robot = obj
        obj.chat = self

    def show_human_dialogue(self):
        out = []
        for i in self.dialog:
            out += [i[0][0] + ' said: ' + i[1][0]]
        out = '\n'.join(out)
        return out

    def show_robot_dialogue(self):
        out = []
        bin = ''
        for i in self.dialog:
            for j in i[1][0]:
                if j in 'aeiouAEIOU':
                    bin += '0'
                else:
                    bin += '1'
            out += [i[0][0] + ' said: ' + bin]
            bin = ''
        out = '\n'.join(out)
        return out


class Human:
    def __init__(self, name):
        self.name = name

    def send(self, message):
        self.chat.dialog += [[[self.name], [message]]]


class Robot:
    def __init__(self, name):
        self.name = name

    def send(self, message):
        self.chat.dialog += [[[self.name], [message]]]


if __name__ == '__main__':

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    karl.send("Hi! What's new?")
    bot.send("Hello, human. Could we speak later about it?")
    assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""

