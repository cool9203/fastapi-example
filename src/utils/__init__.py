# write reference: https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
from .log import *  # noqa:F403
from .util import *  # noqa:F403

try:
    config = load_config()  # noqa:F405
except Exception as e:
    config = dict()
    print(e)
