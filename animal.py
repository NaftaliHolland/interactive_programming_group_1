#!/usr/bin/python3

class Animalia:
    """ Kingdom animalia class """

    def __init__(self, move_by):
        self.set_move_by(move_by)

    def get_move_by(self):
        return self.move_by

    def set_move_by(self, value):
        self.move_by = value

    def eat(self):
        print("Animal eats")

    def move(self):
        print("Animal moves")

    def __str__(self):
        return "I am an animal"

class Mammal(Animalia):
    """ Mammal class """

    def __init__(self, move_by, food):
        super().__init__(move_by)

        self.set_food(value)

    def set_food(self, value):
        self.food = value

    def get_food(self):
        return self.food
    
    def suckle(self):
        print("suckle young ones")

class EggLaying(Animalia):
    """ Egg laying """
    def __init__(self, move_by, food, egg_colour):
        super(Mammal).__init__(move_by, food)
        super(Animalia).__init__(move_by)

        self.set_egg_colour(egg_colour)
        
    def lay(self):
        print("Laying eggs")

    def __str__(self):
        return "I lay eggs"

class DuckBilled(EggLaying, Mammal):
    
    def __str__(self):
        return "I am a Duck Billed Platypus and I am an egg laying mammal"

animal_1 = Animalia()
animal_2 = Mammal()
animal_3 = DuckBilled()

print(animal_1)
print(animal_2)
print(animal_3)
