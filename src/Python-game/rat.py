#alan pham
import random
class Rat:
  def work():
  #member variables
    
    global hp
    global exp
    global basicDamage
    global specialDamage

    hp = 8
    exp = random.randint(4,7)

    basicDamage = random.randint(3,5)
    specialDamage = random.randint(8,10)

  #constructor

  #methods
  def basicAttack(self):
    damage = self.basicDamage
    print('You did ', self.basicDamage, ' damage!')
  def specialAttack2(self):
    damage = self.specialDamage
    print('You did ', self.specialDamage, ' Electric damage!')
  def dropExp(self):
    exp = self.exp
    print('Rat dropped' self.exp,' exp!')