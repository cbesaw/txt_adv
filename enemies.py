from die_roll import gen_roll

class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects!")
        
    def __str__(self):
        return self.name
    
    def is_alive(self):
        return self.hp > 0


#basic enemies    
class Zombie(Enemy):
    def __init__(self):
        self.name = "Zombie Townsperson"
        self.hp = 5
        self.damage = gen_roll(1, 4, 1)
        
class Zombie2(Enemy):
    def __init__(self):
        self.name = "Zombie Guardsman"
        self.hp = 10
        self.damage = gen_roll(1, 6, 1)
        
class Ghoul(Enemy):
    def __init__(self):
        self.name = "Ghoul"
        self.hp = 15
        self.damage = gen_roll(1, 4, 2)

class Wraith(Enemy):
    def __init__(self):
        self.name = "Wraith"
        self.hp = 10
        self.damage = gen_roll(1, 8, 1)
        
            
        
    
    