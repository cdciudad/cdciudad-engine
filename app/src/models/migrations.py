import json
import sys
from uuid import uuid4
from fastapi.encoders import jsonable_encoder

# Pymongo
from pymongo import MongoClient
from app.src.models.history import HistoryPost, HistoryVideo
from app.src.models.service import Service

from app.src.models.staff import Staff, Teacher
from app.src.models.payment import Payment

from app import logger

db = MongoClient('mongodb://db:27017')['cdciudad']
seeds_path = 'app/src/models/seeds'


def migrate_teachers():
    """
    It opens the teachers_seeds.json file, reads the data, and inserts it into the teachers collection
    """
    with open(f'{seeds_path}/teachers_seeds.json', 'r', encoding='utf-8') as file:
        logger.info(f"Teachers migration...")
        data = json.load(file)

        for teacher in data['data']:
            teacher_obj = Teacher(**teacher)
            teacher_obj.id = uuid4()
            teacher_id = db['teachers'].insert_one(
                jsonable_encoder(teacher_obj)).inserted_id
            print(teacher_id)


def migrate_staff():
    """
    It opens the teachers_seeds.json file, reads the data, and inserts it into the staff collection
    """
    with open(f'{seeds_path}/staff_seeds.json', 'r', encoding='utf-8') as file:
        logger.info(f"Staff migration...")
        data = json.load(file)

        for staff in data['data']:
            staff_obj = Staff(**staff)
            staff_obj.id = uuid4()
            staff_id = db['staff'].insert_one(
                jsonable_encoder(staff_obj)).inserted_id
            print(staff_id)


def migrate_services():
    """
    It opens the teachers_seeds.json file, reads the data, and inserts it into the service collection
    """
    with open(f'{seeds_path}/services_seeds.json', 'r', encoding='utf-8') as file:
        logger.info(f"services migration...")

        data = json.load(file)

        for service in data['data']:
            service_obj = Service(**service)
            service_obj.id = uuid4()
            service_id = db['services'].insert_one(
                jsonable_encoder(service_obj)).inserted_id
            print(service_id)


def migrate_payments():
    """
    It opens the teachers_seeds.json file, reads the data, and inserts it into the payments collection
    """
    with open(f'{seeds_path}/payments_seeds.json', 'r', encoding='utf-8') as file:
        logger.info(f"Payments migration...")
        data = json.load(file)

        for payment in data['data']:
            payment_obj = Payment(**payment)
            payment_obj.id = uuid4()
            payment_id = db['payments'].insert_one(
                jsonable_encoder(payment_obj)).inserted_id
            print(payment_id)


def migrate_history_posts():
    """
    It opens the teachers_seeds.json file, reads the data, and inserts it into the history collection
    """
    with open(f'{seeds_path}/history_post_seeds.json', 'r', encoding='utf-8') as file:
        logger.info(f"Posts migration...")
        data = json.load(file)

        for post in data['data']:
            post_obj = HistoryPost(**post)
            post_obj.id = uuid4()
            post_id = db['history'].insert_one(
                jsonable_encoder(post_obj)).inserted_id
            print(post_id)


def migrate_history_videos():
    """
    It opens the teachers_seeds.json file, reads the data, and inserts it into the history-videos collection
    """
    with open(f'{seeds_path}/history_video_seeds.json', 'r', encoding='utf-8') as file:
        logger.info(f"Videos migration...")
        data = json.load(file)

        for video in data['data']:
            video_obj = HistoryVideo(**video)
            video_obj.id = uuid4()
            video_id = db['history-videos'].insert_one(
                jsonable_encoder(video_obj)).inserted_id
            print(video_id)


def migrate():
    migrate_teachers()
    migrate_staff()
    migrate_services()
    migrate_payments()
    migrate_history_posts()
    migrate_history_videos()


def drop():
    collections = db.list_collection_names()
    for collection in collections:
        if collection == 'subscribers':
            pass
        else:
            db.drop_collection(collection)


if __name__ == '__main__':
    if sys.argv[1] == '--drop':
        drop()
    elif sys.argv[1] == '--migrate':
        drop()
        migrate()
