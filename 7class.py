
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
        if(self.thisdirc.get("defence") >= self.thisdirc.get("dexterity")):
            self.thisdirc.update({"defence": self.thisdirc.get(
                "defence")-self.thisdirc.get("attack")})
        self.thisdirc.update({"heal": random.randint})
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
