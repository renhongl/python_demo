

def log(func):
    print('loged')
    return func()


@log()
def now():
    print('now')