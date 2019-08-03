class Pets:

    def __init__(self, name, nick, age, fur, feet, tail, speech):
        self.name = name
        self.nick = nick
        self.age = age
        self.fur = fur
        self.feet = feet
        self.tail = tail
        self.speech = speech

    def nickname(self):
        return'{}{}'.format(self.name, self.nick)


cats = Pets('Kittie', 'Kit', 7, 'True', 4, 'True', 'Says : meow')
dogs = Pets('Doggy', 'Dog', 2, 'True', 4, 'True', 'Says: awwww')

print(cats.speech)
print(dogs.speech)
print(cats.nickname())
print(dogs.nickname())