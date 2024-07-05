class Animal:
    sound = " "
    def _init_(self,name):
        self.name = name
    def speak(self):
        print("{sound} i'm {name} ! {sound}" . format(name=self.name , sound=self.sound))

class piglet(Animal):
    sound = "oink!"
hamlet = piglet("hamletbrown")
piglet.speak()

class cow(Animal):
    sound = "moooo!"
milky = cow(milkywhite)
milkywhite.speak()

