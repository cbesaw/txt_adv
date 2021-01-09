from die_roll import gen_roll



class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")
        
    def __str__(self):
        return self.name
    
class Utility:
    def __init__(self):
        raise NotImplementedError("Do not create raw Utility objects."
                                  )
    def __str__(self):
        return self.name
    
class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects")
        
    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.healing_value)

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small old dagger. " \
                           "Better than nothing..."
        self.damage = gen_roll(1, 4, 1)
        self.value = 10
        

class Longsword(Weapon):
    def __init__(self):
        self.name = "Longsword"
        self.description = "An old trainee's longsword. " \
                           "It was passed on to you by your lord."
        self.damage = gen_roll(1, 8, 1)
        self.value = 35
        

        
class HolySymbol(Utility):
    def __init__(self):
        self.name = "Holy Symbol"
        self.description = "A worn holy symbol of your god" \
                           "Given to you by the head cleric of your order."
        self.value = 5


class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = gen_roll(1, 4, 1)
        self.value = 2.5
        
class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.healing_value = gen_roll(1, 8, 1)
        self.value = 60
                           
                           

        
