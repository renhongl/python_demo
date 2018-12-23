

from collections import deque


def search(lines, pattern, history=5):
    ret = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            ret.append(line)

    return ret

if __name__ == '__main__':
    with open('../input/d1.txt') as f:
        result = search(f, 'python', 5)
        print(result)