from abc import ABC, abstractmethod

class Ability(ABC): # Abstract base class for all abilities, each of them must implement the use method.
    @abstractmethod
    def use(self, caster, target): # To execute the ability from caster to target, override in subclasses.
        pass

class Character:
    def __init__(self, name, hp, mana, attack, defense): # Initialize the character basic attributes.
        self.name = name
        self._hp = hp
        self._mana = mana
        self._attack = attack   
        self._defense = defense 

    def attack(self, target): # To attack another character.
        damage = max(0, self._attack - target._defense) # Damage = attack - target defense. Minimum damage is set to 0.
        target._hp -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        return damage  
    
    def take_damage(self, amount): # Reduce HP given the amount of attack.
        self._hp -= amount
        if self._hp < 0:
            self._hp = 0
        print(f"{self.name} takes {amount} damage! HP is now: {self._hp}")
     
    def is_alive(self): # Check if the character is still alive. If HP > 0, yes.
        return self._hp > 0