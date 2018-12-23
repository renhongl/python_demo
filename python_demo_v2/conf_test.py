

from configparser import ConfigParser

cf = ConfigParser()
cf.read('./input/config.ini')
print(cf.sections())
print(cf.get('info', 'name'))