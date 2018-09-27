import argparse
import json
import sys
from app import db
from app.models import Ads
from server import app
import os
from sqlalchemy import exc


def load_data(filepath):
    with open(filepath, 'r') as f:
        raw_data = f.read()
    return json.loads(raw_data)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        dest='path',
        required=True,
        help='Path to json file'
    )
    return parser.parse_args()


def update_old_ads_before_insert():
    old_ads = Ads.query.filter_by(is_active=True)
    if old_ads:
        for ads in old_ads:
            ads.is_active = False
    db.session.commit()


def insert_data_to_db(loaded_json):
    for ad in loaded_json:
        print(ad['settlement'])
        ad_to_insert = Ads(settlement=ad['settlement'],
                           under_construction=ad['under_construction'],
                           description=ad['description'],
                           price=ad['price'],
                           oblast_district=ad['oblast_district'],
                           living_area=ad['living_area'],
                           has_balcony=ad['has_balcony'],
                           address=ad['address'],
                           construction_year=ad['construction_year'],
                           rooms_number=ad['rooms_number'],
                           premise_area=ad['premise_area']
                           )
        db.session.add(ad_to_insert)
        db.session.commit()


if __name__ == '__main__':
    args = parse_arguments()
    if not os.path.exists(args.path) or not args.path:
        sys.exit('Некорректно указан аргумент')
    with app.app_context():
        try:
            loaded_json = load_data(args.path)
            update_old_ads_before_insert()
            insert_data_to_db(loaded_json)
        except exc.SQLAlchemyError:
            print('Ошибка при выгрузке данных')
