class A:
    def f(self):
        return 1

    def g(self):
        return 2


class B(A):
    def f(self):
        return 3


class C:
    def g(self):
        return 4


class D(A):
    def g(self):
        return 5


class X(B, C):
    pass


x = X()
assert x.f() == 3
assert x.g() == 2


class X(C, D):
    pass


x = X()
assert x.f() == 1
assert x.g() == 4


class X(D, C):
    pass


x = X()
assert x.f() == 1
assert x.g() == 5


class X(B, D):
    pass


x = X()
assert x.f() == 3
assert x.g() == 5


class D1:
    def __get__(self, instance, cls):
        return 1


class D2:
    def __get__(self, instance, cls):
        return 2

    def __set__(self, instance, value):
        pass


class A:
    z = 3


class B(A):
    x = D1()
    y = D2()

    def __init__(self):
        self.x = 5
        self.y = 6

    def __getattr__(self, name):
        return 7


b = B()
assert b.x == 5
assert b.y == 2
assert b.z == 3
assert b.w == 7
assert B.x == 1
assert B.y == 2
assert B.z == 3
# assert B.w Error


class Property:
    def __init__(self, f):
        self.f = f
        self.set_f = None

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return self.f(instance)

    def __set__(self, instance, value):
        if self.set_f is None:
            raise RuntimeError('No logic was implemented')
        return self.set_f(instance, value)

    def setter(self, set_f):
        self.set_f = set_f


class Method:
    def __init__(self, f):
        self.f = f

    def __get__(self, instance, cls):
        if instance is None:
            return self.f
        return BoundMethod(instance, self.f)


class BoundMethod:
    def __init__(self, instance, f):
        self.instance = instance
        self.f = f

    def __call__(self, *args, **kwds):
        return self.f(self.instance, *args, **kwds)
