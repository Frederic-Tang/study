thisdict = {
  "strength":1,
  "dexterity":1, 
  "constitution":1,
  "intelligence":1,
  "wisdom":1,
  "charisma":1
}

print(thisdict)

for i in thisdict:
    print(i)

if("speed" in thisdict):
    print(thisdict.get("speed"))
else:
    print("speed isn't a character stat")

if("strength" in thisdict):
    print(thisdict.get("strength"))
else:
    print("strength isn't a character stat")