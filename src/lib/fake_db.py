#! python3
# coding: utf-8

from typing import Union

from fastapi import APIRouter

import utils

logger = utils.get_logger(logger_name=__name__)

router = APIRouter(prefix="/db", tags=["db"])

fake_db = dict()


@router.get("/{uuid}")
def get(uuid: Union[str, int]) -> Union[str, None]:
    return fake_db.get(uuid, None)


@router.put("/{uuid}")
def put(uuid: Union[str, int], value: str) -> bool:
    if uuid not in fake_db:
        return False
    else:
        fake_db[uuid] = value
    return True


@router.post("/{uuid}")
def post(uuid: Union[str, int], value: str) -> bool:
    if uuid in fake_db:
        return False
    else:
        fake_db[uuid] = value
    return True


@router.delete("/{uuid}")
def delete(uuid: Union[str, int]) -> bool:
    if uuid not in fake_db:
        return False
    else:
        del fake_db[uuid]
        return True
