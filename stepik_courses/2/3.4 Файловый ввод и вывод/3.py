marks = []
math = []
physics = []
rus = []
with open('dataset_3363_4.txt') as inf:
    for s in inf:
        s = s.strip().split(';')
        mark = (int(s[1]) + int(s[2]) + int(s[3])) / 3
        marks.append(mark)
        math.append(int(s[1]))
        physics.append(int(s[2]))
        rus.append(int(s[3]))
s = 0
for i in math:
    s += i
mmath = s / len(math)
s = 0
for i in physics:
    s += i
mphysics = s / len(math)
s = 0
for i in rus:
    s += i
mrus = s / len(math)
sg = [mmath, mphysics, mrus]
out = ''
for mark in marks:
    out += str(mark) + '\n'
out += str(sg[0]) + ' ' + str(sg[1]) + ' ' + str(sg[2])
with open('dataset_3363_4.txt', 'w') as ouf:
    ouf.write(out)