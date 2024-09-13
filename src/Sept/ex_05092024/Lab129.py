class A:
    def method(self):
        return "method A"


class B:
    def method(self):
        return "method B"


class C(B, A):
    pass


c = C()
print(c.method())
