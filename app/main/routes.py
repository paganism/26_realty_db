from flask import Flask, render_template, redirect, flash, url_for, current_app, request
from app.models import Ads
from app import db
from app.main import bp
# from apply_data import


@bp.before_request
def before_request():
    db.session.commit()



@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def ads_list():
    oblast_district = request.args.get('oblast_district')
    new_building = request.args.get('new_building')
    min_price = request.args.get('min_price')
    max_price = request.args.get('max_price')
    print(oblast_district, new_building, min_price, max_price)
    if not min_price:
        print('HVG')
    adss = Ads.query.filter_by(oblast_district=oblast_district, construction_year='2010')
    # print(adss)
    page = request.args.get('page', 1, type=int)
    print_ads = Ads.query.order_by(Ads.construction_year.desc())
    ads = Ads.query.order_by(Ads.construction_year.desc()).paginate(
        page, current_app.config['ADS_PER_PAGE'], False)
    print(print_ads)
    next_url = url_for('main.ads_list', page=ads.next_num) if ads.has_next else None
    prev_url = url_for('main.ads_list', page=ads.prev_num) if ads.has_prev else None

    # ads = [{
    #         "settlement": "Череповец",
    #         "under_construction": False,
    #         "description": '''Квартира в отличном состоянии. Заезжай и живи!''',
    #         "price": 2080000,
    #         "oblast_district": "Череповецкий район",
    #         "living_area": 17.3,
    #         "has_balcony": True,
    #         "address": "Юбилейная",
    #         "construction_year": 2001,
    #         "rooms_number": 2,
    #         "premise_area": 43.0,
    #     }]*10
    return render_template('ads_list.html', ads=ads.items,
                           next_url=next_url,
                           prev_url=prev_url
                           )

