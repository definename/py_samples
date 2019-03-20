menu1 = {
    'breakfast': { 'hours': '7-11' },
    'lunch': { 'hours': '11-3' },
    'dinner': { 'hours': '3-10' }
    }

import json

# serialize dictionary into json string.
jsonMenu = json.dumps(menu1)
print("{}: {}".format(type(jsonMenu), jsonMenu),)

# deserialize json string into dictionary.
menu2 = json.loads(jsonMenu)
print("{}: {}".format(type(menu2), menu2))