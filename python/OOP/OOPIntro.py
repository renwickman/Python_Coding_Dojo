# user = {"name": "AK", "age": 20}
# i = 9
# user2 = {}
# user2['name'] = "AK" 
# user2['age'] = 20
class User:
  def __init__(self, userName, userAge):
    self.name = userName
    self.age = userAge

class Dog:
  def __init__(self, petName, petColor, ownerName, ownerAge):
    #TOY ATTRIBUTES GO HERE (inside __init__ function)
    print("__init__ function has run!")
    self.name = petName 
    self.color = petColor
    self.owner = User(ownerName, ownerAge)

  def bark(self):
    print(self.name + " says OW OW!")

  def play(self, toy):
    #Snoopy loves playing with his bone
    print(self.name + " loves playing with his " + toy)

  def lick(self, other_pet):
    #Pluto has licked Snoopy
    print(self.name + " has licked " + other_pet.name)

  def owner_info(self):
    #Odie's owner is Jon
    print(self.name + "'s owner is " + self.owner.name)
    #Jon is 40
    print(self.owner.name + " is " + str(self.owner.age))
    return self

  #TOY METHODS GO HERE (inside class)

odie = Dog("Odie", "brown", "Jon", 40)
pluto = Dog("Pluto", "yellow", "Goofy", 60)
snoopy = Dog("snoopy", "white", "Charlie Brown", 12)
snoopy.play("bone")
pluto.lick(snoopy)
odie.owner_info().bark()

# {"name": "Odie", "color": "brown", "owner": {"name": "Jon", "age": 40}}

# print(odie.color)
# pluto.bark()
# snoopy.bark()
# {"name": "Odie"}

# instanciating => creating
# instance => one(individual)
# self.name = petName => {"name": petName}
# self.color = petColor => {"name": petName, "color": petColor}

