#! python3
# coding: utf-8

from typing import Union

from fastapi import APIRouter, FastAPI

import lib
import utils

logger = utils.get_logger(logger_name=__name__)


app = FastAPI()
router = APIRouter(prefix="/items")


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


app.include_router(router)
