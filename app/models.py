from app import db
from flask import current_app


class Ads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    settlement = db.Column(db.String(64), index=True)
    under_construction = db.Column(db.Boolean, index=True, default=False)
    description = db.Column(db.String(264))
    price = db.Column(db.Numeric, index=True)
    oblast_district = db.Column(db.String(264))
    living_area = db.Column(db.Float)
    has_balcony = db.Column(db.Boolean, index=True)
    address = db.Column(db.String(80))
    construction_year = db.Column(db.Date)
    rooms_number = db.Column(db.Integer)
    premise_area = db.Column(db.Float)
    is_active = db.Column(db.Boolean, default=True)

    # def add_ad(self, settlement,
    #            under_construction,
    #            description,
    #            price,
    #            oblast_district,
    #            living_area,
    #            has_balcony,
    #            address,
    #            construction_year,
    #            rooms_number,
    #            premise_area
    #            ):
    #     self.settlement = settlement
    #     self.under_construction = under_construction
    #     self.description = description
    #     self.price = price
    #     self.oblast_district = oblast_district
    #     self.living_area = living_area
    #     self.has_balcony = has_balcony
    #     self.address = address
    #     self.construction_year = construction_year
    #     self.rooms_number = rooms_number
    #     self.premise_area = premise_area
    #     db.session.add()

