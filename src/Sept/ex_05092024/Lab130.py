class Grandparents:
    key_gold = "2kg"

    def grandparents_method(self):
        return "Grandparents method"


class Parents(Grandparents):
    def parents_method(self):
        return "parents method"


class Son(Parents):
    mac_m3_apple = "M3 Max"

    def son_method(self):
        return "Son's method"


s = Son()
print(s.grandparents_method())
print(s.parents_method())
print(s.son_method())
