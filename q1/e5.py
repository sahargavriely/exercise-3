class LazyExpression:
    def __init__(s, v: str):
        s.v = v

    def __repr__(s):
        return s.v

    def __radd__(s, o):
        return LazyExpression(f'({o} + {s.v})')

    def __add__(s, o):
        return LazyExpression(f'({s.v} + {o})')

    def __rsub__(s, o):
        return LazyExpression(f'({o} - {s.v})')

    def __sub__(s, o):
        return LazyExpression(f'({s.v} - {o})')

    def __rmul__(s, o):
        return LazyExpression(f'({o} * {s.v})')

    def __mul__(s, o):
        return LazyExpression(f'({s.v} * {o})')

    def __rtruediv__(s, o):
        return LazyExpression(f'({o} / {s.v})')

    def __truediv__(s, o):
        return LazyExpression(f'({s.v} / {o})')

    def __neg__(s):
        return LazyExpression(f'-{s.v}')

    def __pos__(s):
        return LazyExpression(f'+{s.v}')

    def evaluate(s, **kwargs):
        exp = s.v
        for k, v in kwargs.items():
            exp = exp.replace(k, str(v))
        return eval(exp)


class LazyVariable(LazyExpression):
    pass  # TODO
