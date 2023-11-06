#!/usr/bin/python3
class Bird:
    def __init__(self, colour, beak_type, species):
        self.colour = colour
        self.beak_type = beak_type
        self.species = species

    def chirp(self):
        print("crcrcrcrcr")

    def walk(self):
        print("I am walking")

    def eat(self):
        print("I am eating")

    def lay(self):
        print("I am laying an egg")

    def __str__(self):
        return f"I am a {self.colour}, I am just a normal bird"

class Fly(Bird):
    
    def __init__(self, colour, beak_type, species):
        super().__init__(colour, beak_type, species)

    def fly(self):
        print("I am flying")

    def __str__(self):
        return f"I am a {self.colour} and I can fly"

class Swim(Bird):
    
    def __init__(self, colour, beak_type, species):
        super().__init__(colour, beak_type, species)

    def swim(self):
        print("I am swiming")

    def __str__(self):
        return f"I am a {self.colour} and I can swim"

bird_1 = Bird("blue", "serated", "we")
bird_2 = Fly("Black", "small", "Common cuckoo")
bird_3 = Swim("White", "serated", "Mallard")

print(bird_1)
print(bird_2)
print(bird_3)
