from pathlib import Path

class Site(object):
    """docstring for Site."""

    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
