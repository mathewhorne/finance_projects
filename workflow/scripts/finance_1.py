# Finance projects

import json
import pandas as pd

items = json.loads('[{"id": 1, "text": "Item 1"}, {"id": 2, "text": "Item 2"}]')

for item in items:
    print(item['text'])

def greet(greeting, name):
    """Returns a greeting       

    Args:
        greeting (string): A greet word
        name (string): A persons name

    Returns:
        string -- A greeting with a name
    """
    return f'{greeting} {name}'

print(greet('Dumb dumb', 'McGee'))




