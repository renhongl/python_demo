

from collections import ChainMap


default_options = {
    'base_map': 'one_map',
    'title': 'osm_map'
}

extend_options = {
    'title': 'one_map',
    'attribute': 'link to one map'
}

options = ChainMap(extend_options, default_options)

print(options['title'])
print(options['base_map'])
print(options['attribute'])
