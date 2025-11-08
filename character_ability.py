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
        print(f"{self.name} menyerang {target.name} dengan {damage} poin kerusakan!")
        return damage  
    
    def take_damage(self, amount): # Reduce HP given the amount of attack.
        self._hp -= amount
        if self._hp < 0:
            self._hp = 0
        print(f"{self.name} menerima {amount} poin kerusakan! poin nyawa sekarang: {self._hp}")
     
    def is_alive(self): # Check if the character is still alive. If HP > 0, yes.
        return self._hp > 0

# ========== ABILITY SUBCLASSES ==========

class FireBlast(Ability):
    def __init__(self):
        self.mana_cost = 10
        self.cooldown = 0
        self.max_cooldown = 2
        self.uses_left = 3
        self.max_uses = 3
    
    def use(self, caster, target):
        # Check if ability is on cooldown
        if self.cooldown > 0:
            print(f"FireBlast sedang dalam waktu jeda, ({self.cooldown} giliran lagi)")
            return False
        
        # Check if uses are exhausted
        if self.uses_left <= 0:
            print(f"Pengunaan FireBlast telah habis! (0/{self.max_uses})")
            return False
        
        # Check if caster has enough mana
        if caster._mana < self.mana_cost:
            print(f"Mana tidak cukup! membutuhkan {self.mana_cost}, yang dipunya {caster._mana}")
            return False
        
        # Execute FireBlast
        damage = int(caster._attack * 1.5)
        caster._mana -= self.mana_cost
        target.take_damage(damage)
        self.uses_left -= 1
        self.cooldown = self.max_cooldown
        
        print(f"{caster.name} menggunakan FireBlast ke {target.name}!")
        print(f"Memberikan {damage} poin kerusakan! sisa penggunaan: {self.uses_left}/{self.max_uses}")
        return True
    
    def reduce_cooldown(self):
        # Reduce cooldown by 1 each turn
        if self.cooldown > 0:
            self.cooldown -= 1


class Heal(Ability):
    def __init__(self):
        self.mana_cost = 20
        self.cooldown = 0
        self.max_cooldown = 2
    
    def use(self, caster, target):
        # Check if ability is on cooldown
        if self.cooldown > 0:
            print(f"Heal sedang dalam waktu jeda, ({self.cooldown} giliran lagi)")
            return False
        
        # Check if caster has enough mana
        if caster._mana < self.mana_cost:
            print(f"Mana tidak cukup! membutuhkan {self.mana_cost}, yang dipunya {caster._mana}")
            return False
        
        # Check if HP is below 30%
        max_hp = caster._hp + 100  # Assuming max HP, you might need to track this properly
        hp_percentage = (caster._hp / max_hp) * 100
        if hp_percentage >= 30:
            print(f"Heal hanya bisa digunakan saat poin nyawa di bawah 30%, persentase poin nyawa sekarang: {hp_percentage:.1f}%")
            return False
        
        # Execute Heal
        heal_amount = int(caster._attack * 0.8)
        caster._mana -= self.mana_cost
        caster._hp += heal_amount
        self.cooldown = self.max_cooldown
        
        print(f"{caster.name} menggunakan Heal!")
        print(f"Menyembuhkan {heal_amount} poin nyawa! poin nyawa sekarang: {caster._hp}")
        return True
    
    def reduce_cooldown(self):
        # Reduce cooldown by 1 each turn
        if self.cooldown > 0:
            self.cooldown -= 1