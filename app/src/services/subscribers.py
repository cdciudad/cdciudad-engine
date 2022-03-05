from app.src import util
from app.src.data.db import SubscribersRepository
from app.src.models.subscriber import Subscriber

repository = SubscribersRepository()


class SubscribersService:

    def subscribe(self, sub: Subscriber):
        results = repository.read()
        sub_dict = util.serialize(sub.dict())
        results.append(sub_dict)
        print(results)
        repository.write(results)
        return sub
