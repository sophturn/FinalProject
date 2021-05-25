#Sophia Turner
"""import random
import time
class Belldolpine:
  #member variables
  hp = 10
  exp = 0
  #basicDamage = int(random(7,9))
  #specialDamage = int(random(11,13))
  #hpRegain = int(random(3,5))
  #constructor

  #methods
  #def basicAttack(self):
    #damage = self.basicDamage
    #print('You did ', self.basicDamage, ' damage!')
  #def specialAttack2(self):
    #damage = self.specialDamage
    #print('You did ', self.specialDamage, ' Electric damage!')
  #def heal(self):
    #regain = self.hpRegain
    #print('You regained ', self.hpRegain, ' health!')
"""

#THIS IS A TEST COMMENT OUT WHEN TRYING THE CODE OUT
#SOMEONE CHECK IF THIS WORKS LATER
#ALSO COMMENT OUT Belldolpin.work() IN MAIN
#RECOMMENT MAIN LATER

import random
class Belldolpine:
  def work():
  #member variables
    
    global hp
    global exp
    global basicDamage
    global specialDamage
    global hpRegain

    hp = 10
    exp = 0

    basicDamage = random.randint(7,9)
    specialDamage = random.randint(11,13)
    hpRegain = random.randint(3,5)

  #constructor

  #methods
  def basicAttack(self):
    damage = self.basicDamage
    print('You did ', self.basicDamage, ' damage!')
  def specialAttack2(self):
    damage = self.specialDamage
    print('You did ', self.specialDamage, ' Electric damage!')
  def heal(self):
    damage = self.hpRegain
    print('You regained ', self.hpRegain, ' health!')