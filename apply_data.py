import argparse
import json
import sys
from models import Ads, db
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


def set_inactive_ads(loaded_json):
    db_ads = Ads.query.filter_by(is_active=True)
    mappings = []
    file_id = []
    for file_ad in loaded_json:
        file_id.append(file_ad['id'])
    ads_for_update = db_ads.filter(Ads.id.notin_(file_id))
    if ads_for_update:
        for ads in ads_for_update:
            mappings.append({
                'is_active': False,
                'id': ads.id
            })
    db.session.bulk_update_mappings(Ads, mappings)
    db.session.commit()


def insert_update_db_data(loaded_json):
    for ad in loaded_json:
        current_ad = Ads.query.filter_by(id=ad['id']).first()
        if current_ad and (ad['id'] == current_ad.id):
            current_ad.settlement = ad['settlement']
            current_ad.under_construction = ad['under_construction']
            current_ad.description = ad['description']
            current_ad.price = ad['price']
            current_ad.oblast_district = ad['oblast_district']
            current_ad.living_area = ad['living_area']
            current_ad.has_balcony = ad['has_balcony']
            current_ad.address = ad['address']
            current_ad.construction_year = ad['construction_year']
            current_ad.rooms_number = ad['rooms_number']
            current_ad.premise_area = ad['premise_area']
            current_ad.is_active = True
        else:
            print('{} Not In Table. Adding...'.format(ad['id']))
            ad_to_insert = Ads(
                settlement=ad['settlement'],
                under_construction=ad['under_construction'],
                description=ad['description'],
                price=ad['price'],
                oblast_district=ad['oblast_district'],
                living_area=ad['living_area'],
                has_balcony=ad['has_balcony'],
                address=ad['address'],
                construction_year=ad['construction_year'],
                rooms_number=ad['rooms_number'],
                premise_area=ad['premise_area'],
                id=ad['id']
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
            insert_update_db_data(loaded_json)
            set_inactive_ads(loaded_json)
        except exc.SQLAlchemyError:
            print('Ошибка при выгрузке данных')
