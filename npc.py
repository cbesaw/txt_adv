import items


def trade(self, buyer, seller):
    for i, item in enumerate(seller.inventory, 1):
        print("{}. {} - {} Gold".format(i, item.name,
                                        item.value))
    while True:
        user_input = input("Choose an item or press Q to exit: ")
        if user_input in ['Q', 'q']:
            return
        else:
            try:
                choice = int(user_input)
                to_swap = seller.inventory[choice - 1]
                self.swap(seller, buyer, to_swap)
            except ValueError:
                print("Invalid choice!")

def swap(self,  seller, buyer, item):
    if item.value > buyer.gold:
        print("You don't have enough gold.")
        return 
    seller.inventory.remove(item)
    buyer.inventory.append(item)
    seller.gold = seller.gold + item.value
    buyer.gold = buyer.gold - item.value
    print("You bought a {} for {} gold.".format(item.name,
                                                item.value))
    
def check_if_trade(self, player):
    while True:
        print("Would you like to (B)uy, (S)ell or (Q)uit?")
        user_input = input()
        if user_input in ['Q', 'q']:
            return
        elif user_input in ['B', 'b']:
            print("What'a buyin? ")
            self.trade(buyer=player, seller=self.trader)
        elif user_input in ['S', 's']:
            print("What'a sellin? ")
            self.trade(buyer=self.trader, seller=player)
        else:
            print("Invalid choice!")
            
            
            
            


class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects!")
        
    def __str__(self):
        return self.name
    
class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.gold = 100
        self.inventory = [items.CrustyBread(),
                          items.Dagger(),
                          items.HealingPotion()]


