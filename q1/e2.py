from pathlib import Path


class WTFIsFlavour:
    def __init__(self, p: Path):
        self.p = p
        self.name = p.name
        self._skip = False
        self.type = 'directory' if p.is_dir() else 'file'

    def skip(self):
        self._skip = True


def walk(root):
    if not isinstance(root, WTFIsFlavour):
        root = WTFIsFlavour(root)
    if root._skip:
        return
    dirs = list()
    for item in sorted([WTFIsFlavour(i) for i in Path(root.p).iterdir()], key=lambda e: e.name):
        if item.p.is_dir():
            dirs.append(item)
        if not item._skip:
            yield item
    for d in dirs:
        for thingy in walk(d):
            yield thingy
