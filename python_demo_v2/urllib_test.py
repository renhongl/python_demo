

from urllib import request

response = request.urlopen('https://www.python.org')
data = response.read().decode('utf-8')
with open('./output/urllib_test.txt', 'w') as f:
    f.write(data)
    print('write complete')