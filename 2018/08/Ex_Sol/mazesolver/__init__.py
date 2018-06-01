from . import fileIO
from . import userIO
from . import solver


name = "mazesolver"

__all__ = [
    "fileIO", "userIO", "solver",
    "__title__", "__summary__", "__version__", "__author__",
    "__email__"
]

__title__ = "mazesolver"
__summary__ = "This package can solve mazes by backtracking with neat user IO."

__version__ = "0.1.0"
__author__ = "Moritz Nipshagen, Antonia Hain"
__email__ = "mnipshagen@uos.de"

