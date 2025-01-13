# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("This animal makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

# Child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Output: Buddy says Woof!
cat.speak()  # Output: Whiskers says Meow!
