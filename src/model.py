import os
from abc import abstractmethod
from dyntastic import Dyntastic
from pydantic import BaseModel, Field
from typing import Optional


class DynamoDbModelBase(Dyntastic):
    __table_region__ = os.environ.get("AWS_REGION")
    __table_host__ = os.environ.get("DYNAMO_ENDPOINT")
    __hash_key__ = "hash_key"
    __range_key__ = "range_key"

    @property
    @abstractmethod
    def __table_name__(self):  # over-ride this on each implementing class
        pass

    hash_key: str = Field(default=None, title="DynamoDB Partition Key")
    range_key: str = Field(default=None, title="DynamoDB Sort Key")


"""TODO
Architect a data structure for storing user's recurring orders. Two tables have already been setup for you,
User and RecurringOrder. It is up to you how you want to structure the data, so feel free to user both tables
or only one based on your strategy.

Don't forget to checkout the full requirements in the README or in api.py as those will pertain relevant information that
will apply to this file.
"""


class UserInfo(BaseModel):
    first_name: str
    last_name: str


class User(DynamoDbModelBase):
    __table_name__ = "User"
    info: Optional[UserInfo]


class RecurringOrder(DynamoDbModelBase):
    __table_name__ = "RecurringOrder"
