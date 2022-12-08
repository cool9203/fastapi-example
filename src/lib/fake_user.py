#! python3
# coding: utf-8
# Reference-1: https://stackoverflow.com/questions/63853813/how-to-create-routes-with-fastapi-within-a-class
# Reference-2: https://fastapi-utils.davidmontague.xyz/user-guide/class-based-views/

from typing import Union

from fastapi import Depends, FastAPI
from fastapi_restful.cbv import cbv
from fastapi_restful.inferring_router import InferringRouter

import lib
import utils

logger = utils.get_logger(logger_name=__name__)


def get_x(value: int):
    return value


fake_db = dict()


router = InferringRouter(prefix="/user", tags=["user"])


@cbv(router)
class User:
    @router.get("/{uuid}", description="get user data")
    def get(self, uuid: Union[int, str]) -> Union[str, None]:
        return fake_db.get(uuid, None)

    @router.post("/{uuid}")
    def post(self, uuid: Union[int, str], value: Union[int, str]) -> bool:
        try:
            fake_db[uuid] = value
            return True
        except Exception as e:
            return False

    @router.put("/{uuid}")
    def put(self, uuid: Union[int, str], value: Union[int, str]) -> bool:
        return self.post(uuid, value)

    @router.delete("/{uuid}")
    def delete(self, uuid: Union[int, str]) -> bool:
        try:
            del fake_db[uuid]
            return True
        except Exception as e:
            return False
