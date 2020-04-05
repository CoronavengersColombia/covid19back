from datetime import datetime, date
from flask import jsonify, request, url_for
from app import db, ma
from app.api import bp
from app.models import Store


class DaySchema(ma.Schema):
    class Meta:
        fields = (
            'sid',
            'name',
            'description',
            'store_type',
            'store_type_description',
            'contact',
            'payment',
            'city',
            'sector',
            'coverage',
            'hours',
            'timestamp'
        )

# Model Schemas
store_schema = DaySchema()
all_stores_schema = DaySchema(many=True)


@bp.route('/stores/', methods=['GET'])
def stores():
    cases = Day.query.all()

    data = []

    return all_stores_schema.jsonify(cases)

@bp.route('/stores/add/', methods=['POST'])
def add_stores():
    name = request.json['name']
    description = request.json['description']
    store_type = request.json['store_type']
    store_type_description = request.json['store_type_description']
    contact = request.json['contact']
    payment = request.json['payment']
    city = request.json['city']
    sector = request.json['sector']
    coverage = request.json['coverage']
    hours = request.json['hours']
    timestamp = datetime.strptime(request.json['timestamp'], '%Y/%m/%d')
    
    store = Store(
        name=name,
        description=description,
        store_type=store_type,
        store_type_description=store_type_description,
        contact=contact,
        payment=payment,
        city=city,
        sector=sector,
        coverage=coverage,
        hours=hours,
        timestamp=timestamp
    )
    
    db.session.add(store)
    db.session.commit()

    return store_schema.jsonify(store)
