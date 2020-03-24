from datetime import datetime, date
from app import db


class Day(db.Model):
    did = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True)
    total = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '{0}: {1}'.format(self.date.strftime("%d %B, %Y"), self.total)

    def get_id(self):
        return self.did
