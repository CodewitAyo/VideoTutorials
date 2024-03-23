class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print("Speak", self.name)

    def move(self):
        print("Move", self.name)


animal = Animal('Tom', 'cat')
animal.speak()
animal.move()
