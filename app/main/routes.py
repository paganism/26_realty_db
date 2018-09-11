from flask import Flask, render_template, redirect, flash, url_for, current_app
from app.models import Ads
from app import db
from app.main import bp
# from apply_data import


@bp.before_request
def before_request():
    db.session.commit()



@bp.route('/', methods=['GET', 'POST'])
# @app.route('/index', methods=['GET', 'POST'])
def ads_list():
    return render_template('ads_list.html', ads=[{
            "settlement": "Череповец",
            "under_construction": False,
            "description": '''Квартира в отличном состоянии. Заезжай и живи!''',
            "price": 2080000,
            "oblast_district": "Череповецкий район",
            "living_area": 17.3,
            "has_balcony": True,
            "address": "Юбилейная",
            "construction_year": 2001,
            "rooms_number": 2,
            "premise_area": 43.0,
        }]*10
    )
