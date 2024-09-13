# reverse Single In inheritance(Do not work with real scenario)
class Son:
    gold = "1kg"


class Father(Son):
    diamond = "22karat"


class GrandFather(Father):
    btc = "1btc"


gf = GrandFather()
