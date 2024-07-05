class fruit:
    def __init__(self,color,flavor):
        self.color = color
        self.flavor = flavor
class Apple(fruit):
    pass
class Grape(fruit):
    pass

granny_smith = Apple("green","tart")
carnelian = Grape("purple", "sweet")

print(granny_smith.flavor)
print(carnelian.color)
