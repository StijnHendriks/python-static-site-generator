from typing import List
from pahtlib import Path

class Parser(object):
    """docstring for Parser."""
    extensions = List[str]

    def __init__(self, arg):
        super(Parser, self).__init__()
        self.arg = arg
