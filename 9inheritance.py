import random


class Character:
    keys = ["strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma"]
    thisdirc = {}

    def __init__(self) -> None:
        for i in self.keys:
            self.thisdirc[i] = random.randint(1, 20)
        self.thisdirc.update(
            {"attack": random.randint(1, self.thisdirc.get("strength"))})
        self.thisdirc.update({"defence": random.randint(1, 20)})
        if(self.thisdirc.get("defence") >= self.thisdirc.get("dexterity") and self.thisdirc.get("defence") >= self.thisdirc.get("attack")):
            self.thisdirc.update({"defence": self.thisdirc.get(
                "defence")-self.thisdirc.get("attack")})
        self.thisdirc.update({"heal": random.randint(1, 20)})
        self.hitpoint = self.thisdirc.get(
            "constitution")*30+50+self.thisdirc.get("heal")

    def printstats(self):
        print(self.thisdirc.items())

    def printHit(self):
        print(self.hitpoint)


if __name__ == "__main__":
    character = Character()
    character.printstats()
    character.printHit()
    
class MagicCharacter(Character):
    def __init__(self):
     super().__init__()
     self.mana=self.thisdirc.get('intelligence')*30+50
    
    def printstats(self):
        print("Hit:",end="")
        super().printHit()
        print("Mana:"+(str)(self.mana))
    
    
    def magicMissile(self):
        self.mana-=5
        return random.randint(5,10)  
    
    def fireball(self):
        self.mana-=10
        return random.randint(10,20) 
    
    def healMana(self,number):
        self.mana+=number


if __name__ == "__main__":
    magicCharacter = MagicCharacter()
    magicCharacter.printstats()
    
    
