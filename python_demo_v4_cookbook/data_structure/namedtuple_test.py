

from collections import namedtuple



Student = namedtuple('Student', ['name', 'age'])

s = Student('renhong', 19)

print(s)
print(s[0])
print(s.age)