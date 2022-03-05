from unittest import result
from app import util
from app.data.db import SubscribersRepository
from app.models.subscriber import Subscriber

repository = SubscribersRepository()


class SubscribersService:

    def subscribe(self, sub: Subscriber):
        results = repository.read()
        sub_dict = util.serialize(sub.dict())
        results.append(sub_dict)
        print(results)
        repository.write(results)
        return sub
