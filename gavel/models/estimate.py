from gavel.models import db

class Estimate(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True, nullable=False)
    estimate = db.Column(db.Integer)

    def __init__(self, estimate):
        self.estimate = estimate
