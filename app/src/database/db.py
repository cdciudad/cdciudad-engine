import json
import os
from typing import List
from dotenv import dotenv_values
from pymongo import MongoClient


class Repository:

    def read(self) -> List:
        with open(self.file_path, "r+", encoding="utf-8") as f:
            users = json.loads(f.read())
            return users

    def write(self, data: List):
        with open(self.file_path, "r+", encoding="utf-8") as f:
            f.seek(0)  # Moving to first byte of the file
            f.write(json.dumps(data))


class SubscribersRepository(Repository):

    def __init__(self) -> None:
        super().__init__()
        self.file_path = os.getenv("SUBS_DB")
