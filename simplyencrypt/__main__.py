
import os
from rich import print as richprint

path = os.path.abspath(__file__)
EASY__doc__ = open(path[:-11] + "EASY__doc__.txt", "r")
richprint(EASY__doc__.read())
