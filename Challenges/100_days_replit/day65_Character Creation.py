class Character:
    def __init__(self, name: str, health: int, magicPoints: int):
        self.name = name
        self.health = health
        self.magicPoints = magicPoints


class Player(Character):
    def __init__(
        self, name: str, health: int, magicPoints: int, nickname: str, lives: int
    ):
        super().__init__(name, health, magicPoints)
        self.health = health
        self.nickname = nickname
        self.lives = lives

    def isAlive(self):
        if self.lives >= 1:
            return "Yes"
        else:
            return "No"

    def display(self):
        _ = f"""
Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
Lives: {self.lives}
Alive?: {self.isAlive()}
    """
        print(_)


class Enemy(Character):
    type: str = None
    strength: int = None

    def __init__(
        self, name: str, health: int, magicPoints: int, type: str, strength: int
    ):
        super().__init__(name, health, magicPoints)
        self.type = type
        self.strength = strength


class Vampire(Enemy):
    def __init__(
        self, name: str, health: int, magicPoints: int, strength: int, day: bool
    ):
        super().__init__(name, health, magicPoints, type, strength)
        self.type = "Vampire"
        self.day = day

    def isDay(self):
        if self.day == True:
            return "Day"
        else:
            return "Night"

    def display(self):
        _ = f"""
Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
Type: {self.type}
Strength: {self.strength}
Day/Night?: {self.isDay()}
    """
        print(_)


class Orc(Enemy):
    def __init__(
        self, name: str, health: int, magicPoints: int, strength: int, speed: int
    ):
        super().__init__(name, health, magicPoints, "Orc", strength)
        self.speed = speed

    def display(self):
        _ = f"""
Name: {self.name}
Health: {self.health}
Magic Points: {self.magicPoints}
Type: {self.type}
Strength: {self.strength}
Speed: {self.speed}
    """
        print(_)


# Player Init
tinapyp = Player(
    name="Fathin Afif", health=100, magicPoints=50, nickname="tinapyp", lives=3
)

# Vampire Init
boris = Vampire(name="Boris", health=45, magicPoints=70, strength=3, day=False)

rishi = Vampire(name="Rishi", health=70, magicPoints=10, strength=75, day=False)

# Orc Init
bill = Orc(name="Bill", health=60, magicPoints=5, strength=75, speed=90)
ted = Orc(name="Ted", health=75, magicPoints=40, strength=80, speed=45)
station = Orc(name="Station", health=35, magicPoints=40, strength=49, speed=50)

print("🌟Generic RPG🌟\nPlayer")
tinapyp.display()

print("Enemy\n")
boris.display()
rishi.display()

bill.display()
ted.display()
station.display()
