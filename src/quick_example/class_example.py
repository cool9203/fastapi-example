#! python3
# coding: utf-8
# Reference-1: https://stackoverflow.com/questions/63853813/how-to-create-routes-with-fastapi-within-a-class
# Reference-2: https://fastapi-utils.davidmontague.xyz/user-guide/class-based-views/
# Another write class base view see this answer: https://stackoverflow.com/questions/63853813/how-to-create-routes-with-fastapi-within-a-class/70563827#70563827 # noqa:E501

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


app = FastAPI()
router = InferringRouter(prefix="/foo")  # Step 1: Create a router
user_router = InferringRouter(tags=["user"])  # Step 1: Create a router


@cbv(router)  # Step 2: Create and decorate a class to hold the endpoints
class Foo:
    # Step 3: Add dependencies as class attributes
    # Depends 介紹: https://blog.csdn.net/NeverLate_gogogo/article/details/112472480
    x: int = Depends(get_x)

    @router.get("/")
    def bar(self) -> int:
        # Step 4: Use `self.<dependency_name>` to access shared dependencies
        return self.x


@cbv(user_router)
class User:
    @user_router.get("/user/{uuid}", description="get user data")
    def get(self, uuid: Union[int, str]) -> Union[str, None]:
        return fake_db.get(uuid, None)

    @user_router.post("/user/{uuid}")
    def post(self, uuid: Union[int, str], value: Union[int, str]) -> bool:
        try:
            fake_db[uuid] = value
            return True
        except Exception as e:
            return False

    @user_router.put("/user/{uuid}")
    def put(self, uuid: Union[int, str], value: Union[int, str]) -> bool:
        return self.post(uuid, value)

    @user_router.delete("/user/{uuid}")
    def delete(self, uuid: Union[int, str]) -> bool:
        try:
            del fake_db[uuid]
            return True
        except Exception as e:
            return False


app.include_router(user_router)
app.include_router(router)
