#! python3
# coding: utf-8

import sys
from pathlib import Path

sys.path.append(str(Path("../").resolve()))

from typing import Dict

import yaml


def load_config(path: str = "./config.yaml") -> Dict[str, str]:
    with Path(path).open("r", encoding="utf8") as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
    input("press Enter to continue...")
