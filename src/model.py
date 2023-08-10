import os
from abc import abstractmethod
from dyntastic import Dyntastic
from pydantic import BaseModel, Field
from typing import Optional


class DynamoDbModelBase(Dyntastic):
    __table_region__ = os.environ.get("REGION_NAME")
    __table_host__ = os.environ.get("DYNAMO_ENDPOINT")
    __hash_key__ = "hash_key"
    __range_key__ = "range_key"

    @property
    @abstractmethod
    def __table_name__(self):  # over-ride this on each implementing class
        pass

    # Fields that every DynamoDB item shall have
    # the key fields are marked optional so the object can be created by the dev
    # on new records keys set by the init method to conform with the class partition and sort keys
    hash_key: str = Field(default=None, title="DynamoDB Partition Key")
    range_key: str = Field(default=None, title="DynamoDB Sort Key")


class UserInfo(BaseModel):
    first_name: str
    last_name: str


class User(DynamoDbModelBase):
    __table_name__ = "User"
    info: Optional[UserInfo]


class RecurringOrder(DynamoDbModelBase):
    __table_name__ = "RecurringOrder"
