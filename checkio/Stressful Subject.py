import re

def is_stressful(subj):
    uppercase = subj.upper()
    if subj == uppercase:
        return True
    if subj[-3: len(subj)] == '!!!':
        return True
    str = subj.lower()
    print(str)
    result1 = re.search(r'h[^\s]{0,}e[^\s]{0,}l[^\s]{0,}p', str)
    result2 = re.search(r'a[^\s]{0,}s[^\s]{0,}a[^\s]{0,}p', str)
    result3 = re.search(r'u[^\s]{0,}r[^\s]{0,}g[^\s]{0,}e[^\s]{0,}n[^\s]{0,}t', str)
    if result1 or result2 or result3:
        return True
    return False

is_stressful("something is gona happen")

is_stressful("I neeed HELP")

if __name__ == '__main__':
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')