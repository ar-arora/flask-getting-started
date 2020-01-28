# implementing a model from a json file as we don't have a database right now.

import json

def load_db(): 
    with open('flashcards_db.json') as model:
        return json.load(model)