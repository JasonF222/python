# class Parent:
#     def method_a(self):
#         print("invoking PARENT method_a!")
# class Child(Parent):
#     def method_a(self):
#         print("invoking CHILD method_a!")
# dad = Parent()
# son = Child()
# dad.method_a()
# son.method_a() # notice this overrides the Parent method!

# # We'll use the Person class to demonstrate polymorphism
# # in which multiple classes inherit from the same class but behave in different ways

# class Person:
#     def pay_bill(self):
#         raise NotImplementedError
# # Millionaire inherits from Person
# class Millionaire(Person):
#     def pay_bill(self):
#         print("Here you go! Keep the change!")
# # Grad Student also inherits from the Person class
# class GradStudent(Person):
#     def pay_bill(self):
#         print("Can I owe you ten bucks or do the dishes?")


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} walks {self.pet.name}")
        self.pet.play()

    def feed(self):
        print(f"{self.first_name} feeds {self.pet.name}")
        self.pet.eat(self.pet_food)

    def bathe(self):
        print(f"{self.first_name} bathes {self.pet.name}")
        self.pet.noise()


class Pet(Ninja):
    def __init__(self, pet_name, breed, tricks, health, energy):
        self.name = pet_name
        self.breed = breed
        self.tricks = tricks
        self.health = 0
        self.energy = 0

    def sleep(self):
        print(f"{self.name} energy increased by 25!")

    def eat(self, pet_food): # Eat method
        print(f"{self.name} eats {pet_food}")


    def play(self): # Play method
        print(f"{self.name} plays with intensity and excitement")

    def noise(self):  # Noise method
        print(f"{self.name} barks with enthusiasm!")


Milo = Pet("Milo", "Beagador", "Roll Over", 100, 100 )
Jason = Ninja("Jason", "Frantz", "Puperoni", "Beef", Milo)

Jason.walk()
Jason.feed()
Jason.bathe()
# Jason.walk()
# Milo.walk()

# Jason.feed()
# Milo.feed()

# Jason.bathe()
# Milo.bathe()