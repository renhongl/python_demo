

def frange(start, stop, step):
    st = start
    while st < stop:
        yield st
        st += step
    

for i in frange(2, 10, 0.5):
    print(i)



def count_down(n):
    start = n
    while start > 0:
        yield start
        start -= 1
    print('Done')

c = count_down(4)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
