from app.src import util
from app.src.data.db import SubscribersRepository
from app.src.models.subscriber import Subscriber

repository = SubscribersRepository()


class SubscribersService:

    def subscribe(self, sub: Subscriber):
        results = repository.read()
        sub_dict = util.serialize(sub.dict())
        results.append(sub_dict)
        repository.write(results)
        return sub

    def get_all(self):
        return repository.read()

    @staticmethod
    def get_weekly_subscribers():
        subs = repository.read()
        weekly_subs = [
            sub for sub in subs if util.check_last_week(sub["created_at"])]
        return weekly_subs

