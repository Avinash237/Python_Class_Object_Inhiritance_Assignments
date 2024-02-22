# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived classes
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"

# Example usage
if __name__ == "__main__":
    dog = Dog("Buddy")
    print(dog.speak())  # Output: Buddy says Woof!

    cat = Cat("Whiskers")
    print(cat.speak())  # Output: Whiskers says Meow!

    cow = Cow("Bessie")
    print(cow.speak())  # Output: Bessie says Moo!
