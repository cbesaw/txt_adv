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
        self.damage = 2
        
class Zombie2(Enemy):
    def __init__(self):
        self.name = "Zombie Guardsman"
        self.hp = 15
        self.damage = 4
        
class Ghoul(Enemy):
    def __init__(self):
        self.name = "Ghoul"
        self.hp = 20
        self.damage = 5

class Wraith(Enemy):
    def __init__(self):
        self.name = "Wraith"
        self.hp = 20
        self.damage = 5
        
            
        
    
    