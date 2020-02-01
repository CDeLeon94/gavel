from gavel import app
from gavel.models import *
from flask import session

@app.route('/status', methods=['GET'])
# TODO: add auth
def fetch_status():
    # TODO: for hacker interface, add item (team) ID to session on login
    item = Item.by_id(session.get(ITEM_ID, None))
    return item.estimate
