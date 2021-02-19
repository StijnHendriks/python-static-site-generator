from typing import List
from pathlib import Path

class Parser(object):
    """docstring for Parser."""
    extensions: List[str] = []

    def __init__(self, arg):
        super(Parser, self).__init__()
        self.arg = arg

    def valid_extension(self, extension):
        return extension in self.extensions
