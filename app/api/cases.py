from datetime import datetime, date
from flask import jsonify, request, url_for
from app import db, ma
from app.api import bp
from app.models import Day


class DaySchema(ma.Schema):
    class Meta:
        fields = ('did', 'date', 'count')

# Model Schemas
day_schema = DaySchema()
all_days_schema = DaySchema(many=True)


@bp.route('/cases/', methods=['GET'])
def cases():
    cases = Day.query.all()

    data = []

    return all_days_schema.jsonify(cases)

@bp.route('/cases/add/', methods=['POST'])
def add_cases():
    date = datetime.strptime(request.json['date'], '%Y/%m/%d')
    total = request.json['total']
    
    day = Day.query.filter_by(date=date).first()

    if day is not None:
        day.date = date
        day.total = total
        db.session.commit()
        return day_schema.jsonify(day)

    day_cases = Day(date=date, total=total)
    
    db.session.add(day_cases)
    db.session.commit()

    return day_schema.jsonify(day_cases)
