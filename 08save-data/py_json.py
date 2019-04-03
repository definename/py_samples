menu1 = {
    'breakfast': { 'hours': '7-11' },
    'launch': { 'hours': '11-3' },
    'dinner': { 'hours': '3-10' }
    }

import json

# serialize dictionary into json string.
jsonMenu = json.dumps(menu1)
print("Serialize:\n{}: {}".format(type(jsonMenu), jsonMenu),)

# deserialize json string into dictionary.
menu2 = json.loads(jsonMenu)
print("Deserialize:\n{}: {}".format(type(menu2), menu2))

print("Pretty:\n{}".format(json.dumps(menu1, indent=2)))