
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'

word = line.split(' ')

print(word)

word2 = re.split('[;,\s]\s*', line)
print(word2)