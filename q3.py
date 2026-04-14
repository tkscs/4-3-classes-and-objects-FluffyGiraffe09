class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"a Cat named {self.name}"
    def speak(self):
        print(f"{self.name} says meow!")

ella = Cat("Ella")
ella.speak()

class Dog:
    """a dog"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"A Dog named {self.name}"
    def speak(self):
        print(f"{self.name} says meow!")

laila = Dog("Laila")
laila.speak()
print(laila)