#! python3
# coding: utf-8

import sys
from pathlib import Path

sys.path.append(str(Path("../").resolve()))

import logging
import logging.config
from typing import Optional

FORMAT_STD = "%(asctime)s %(levelname)s %(pathname)s.%(lineno)d %(message)s"
FORMAT_DEBUG = "%(levelname)s %(pathname)s.%(lineno)d %(message)s"
FORMAT_MESSAGE = "%(message)s"
DATEFMT_STD = "%Y/%m/%d %I:%M:%S"


def get_logger(
    logger_name: str = "root",
    propagate: bool = False,
    log_level: Optional[str] = None,
    log_fmt: str = "STD",
    log_path: str = "./",
    file_name: Optional[str] = None,
    file_mode: str = "w",
) -> logging.Logger:
    """Get logging.logger from set params

    Args:
        logger_name (str, optional): set logger name. Defaults to "root".
        propagate (bool, optional): set logger propagate, if True, will propagate to root, else will not propagate.
        log_level (str, optional): set log show level, if None will set "INFO". Defaults to None.
        log_fmt (str, optional): set show format, choices=["STD", "DEBUG", other]. Defaults to "STD".
        log_path (str, optional): set log save file path. Defaults to "./".
        file_name (str, optional): set log save file name. Defaults to None.
        file_mode (str, optional): set file mode, choices=["w", "a"]. Defaults to "w".

    Raises:
        Exception: _description_

    Returns:
        logging.Logger: logger, use logger.info(), logger.debug(), logger.error(), logger.warning(), logger.exception() to show message


    """
    log_level = "INFO" if log_level is None else log_level.upper()
    log_fmt = log_fmt.upper()

    if file_mode not in ["w", "a"]:
        raise Exception(f"error: argument file_mode: invalid choice: {file_mode} (choose from 'w', 'a')")

    if log_fmt == "STD":
        log_fmt = FORMAT_STD
    elif log_fmt == "DEBUG":
        log_fmt = FORMAT_DEBUG
    else:
        log_fmt = FORMAT_MESSAGE

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.getLevelName(log_level))
    formatter = logging.Formatter(log_fmt, datefmt=DATEFMT_STD)
    logger.propagate = propagate

    handler = logging.StreamHandler()
    handler.setLevel(logging.getLevelName(log_level))
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    if file_name is not None and Path(log_path).exists():
        handler = logging.FileHandler(str(Path(log_path, f"{file_name}.log")), mode=file_mode)
        handler.setLevel(logging.getLevelName(log_level))
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    else:
        logger.warning("Not use log file")

    return logger


def main() -> None:
    pass


if __name__ == "__main__":
    main()
