from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Ads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    settlement = db.Column(db.String(64), index=True)
    under_construction = db.Column(db.Boolean, index=True, default=False)
    description = db.Column(db.String(512))
    price = db.Column(db.Numeric, index=True)
    oblast_district = db.Column(db.String(264), index=True)
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean, index=True)
    address = db.Column(db.String(264))
    construction_year = db.Column(db.Integer, index=True)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)
    is_active = db.Column(db.Boolean, default=True, index=True)

