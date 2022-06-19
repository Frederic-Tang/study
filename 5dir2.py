import random

keys =["strength",
  "dexterity", 
  "constitution",
  "intelligence",
  "wisdom",
  "charisma"]

thisdirc={}

for i in keys:
    thisdirc[i] = random.randint(1, 20)

x=thisdirc.items() 
print(x)