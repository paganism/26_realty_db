from flask import Flask, render_template, redirect, flash, url_for, current_app, request
from flask_paginate import Pagination, get_page_parameter
from app.models import Ads
from app.main import bp
from datetime import datetime
from sqlalchemy import or_


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def ads_list():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    oblast_district = request.args.get('oblast_district')
    new_building = request.args.get('new_building', False)
    min_price = request.args.get('min_price', 0)
    max_price = request.args.get('max_price')
    if not min_price:
        min_price = 0
    ads_max_price = Ads.query.filter_by(is_active=True).order_by(Ads.price.desc()).first()
    if not max_price:
        max_price = ads_max_price.price
    current_year = datetime.today().year
    if oblast_district:
        ads = Ads.query.filter(Ads.is_active,
                               Ads.oblast_district == oblast_district,
                               Ads.price >= min_price,
                               Ads.price <= max_price,
                               )
    else:
        ads = Ads.query.filter(Ads.is_active,
                               Ads.price >= min_price,
                               Ads.price <= max_price,
                               )
        oblast_district = ''
    if new_building:
        ads = ads.filter(or_(Ads.under_construction, Ads.construction_year >= current_year-2))
    ads = ads.paginate(page, current_app.config['ADS_PER_PAGE'], False)
    pagination = Pagination(page=page,
                            total=ads.total,
                            per_page=current_app.config['ADS_PER_PAGE'],
                            css_framework='foundation',
                            record_name='ads')
    return render_template('ads_list.html',
                           ads=ads.items,
                           pagination=pagination,
                           oblast_district=oblast_district
                           )

