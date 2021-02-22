import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    """docstring for Content."""
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def __init__(self, arg):
        super(Content, self).__init__()
        self.arg = arg

    def load(self, cls, string):
        _, fm, content = __regex.split(string, 2)
        
