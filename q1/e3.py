from typing import Any


class FuncDict:
    def __init__(self, f):
        self.f = f


class TransformDict(FuncDict, dict):
    def __getitem__(self, __key: Any) -> Any:
        return super().__getitem__(self.f(__key))

    def __contains__(self, __key: object) -> bool:
        return super().__contains__(self.f(__key))

    def __setitem__(self, __key: Any, __value: Any) -> None:
        return super().__setitem__(self.f(__key), __value)
