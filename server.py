from models import Ads, db
from flask_migrate import Migrate
from config import Config
from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime
from sqlalchemy import or_


app = Flask(__name__)

app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def ads_list():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    oblast_district = request.args.get('oblast_district')
    new_building = request.args.get('new_building', False)
    min_price = request.args.get('min_price', 0, type=int)
    max_price = request.args.get('max_price', type=int)
    ads = Ads.query.filter_by(is_active=True).order_by(Ads.price.desc())
    ads_max_price = ads.first()
    if not max_price:
        max_price = ads_max_price.price
    current_year = datetime.today().year
    if oblast_district:
        ads = ads.filter(
            Ads.oblast_district == oblast_district,
                               Ads.price >= min_price,
                               Ads.price <= max_price,
            )
    else:
        ads = ads.filter(Ads.price >= min_price,
                               Ads.price <= max_price,
                         )
        oblast_district = ''
    if new_building:
        ads = ads.filter(
            or_(Ads.under_construction,
                Ads.construction_year >= current_year-2)
        )
    ads = ads.paginate(page, app.config['ADS_PER_PAGE'], False)
    pagination = Pagination(page=page,
                            total=ads.total,
                            per_page=app.config['ADS_PER_PAGE'],
                            css_framework='foundation',
                            record_name='ads')
    return render_template('ads_list.html',
                           ads=ads.items,
                           pagination=pagination,
                           oblast_district=oblast_district
                           )


if __name__ == "__main__":
    app.run()
