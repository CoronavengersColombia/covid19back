from datetime import datetime, date
from app import db


class Day(db.Model):
    did = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True)
    count = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '{0}: {1}'.format(self.date.strftime("%d %B, %Y"), self.total)

    def get_id(self):
        return self.did

class Store(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), index=True, unique=True)
    description = db.Column(db.String(140), index=True, unique=True)
    store_type = db.Column(db.String(140), index=True)
    store_type_description = db.Column(db.String(140), index=True)
    contact = db.Column(db.String(140), index=True)
    payment = db.Column(db.String(140), index=True)
    city = db.Column(db.String(140), index=True)
    sector = db.Column(db.String(140), index=True)
    coverage = db.Column(db.String(140), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '{0}: {1}'.format(name, description)

    def get_id(self):
        return self.sid
