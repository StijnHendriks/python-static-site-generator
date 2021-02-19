import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    """docstring for Content."""
    __regix = re.compile(__delimiter, re.MULTILINE)

    def __init__(self, arg):
        super(Content, self).__init__()
        self.arg = arg
