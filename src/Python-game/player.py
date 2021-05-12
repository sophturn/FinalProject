import random
class Player:
  #member variables
  inventory = 1
  #constructor

  #methods
  def travel(self):
    bokemonFind = int(random(1,3))
  def catch(self):
    if(self.inventory >= 3):
      print()
    bokemonCatch = int(random(1,3))
    if(bokemonCatch == 3):
      print()
    elif (self.inventory < 3):
      self.inventory += 1
      print('Bokémon captured!\nYou have ', self.inventory, 'Bokémon in your inventory')