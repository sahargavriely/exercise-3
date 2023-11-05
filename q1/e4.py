class MultiDict(dict):
    def __getitem__(self, __key):
        ret, *_ = super().__getitem__(__key)
        return ret

    def get_all(self, __key):
        return super().__getitem__(__key)

    def __setitem__(self, __key, __value) -> None:
        if __key in self:
            return super().__getitem__(__key).append(__value)
        return super().__setitem__(__key, [__value])

    def __delitem__(self, __key):
        if len(super().__getitem__(__key)) == 1:
            return self.delete_all(__key)
        return super().__getitem__(__key).pop(0)

    def delete_all(self, __key):
        return super().__delitem__(__key)
