from abc import ABC, abstractmethod

class Ability(ABC): 
    @abstractmethod
    def use(self, caster, target): 
        pass

class Character:
    def __init__(self, name, hp, mana, attack, defense): 
        self.name = name
        self._hp = hp
        self._mana = mana
        self._attack = attack   
        self._defense = defense 

    def attack(self, target): # Menyerang target
        damage = max(0, self._attack - target._defense) # Damage = attack - target defense. Minimum damage disetting ke 0
        target._hp -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        return damage  
    
    def take_damage(self, amount): # Mengurangi HP karaker sebesar amount
        self._hp -= amount
        if self._hp < 0:
            self._hp = 0
        print(f"{self.name} takes {amount} damage! HP is now: {self._hp}")
     
    def is_alive(self): # Cek apakah karakter masih hidup
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
        # Cek apakah ability masih di cooldown
        if self.cooldown > 0:
            print(f"FireBlast masih cooldown! ({self.cooldown} giliran tersisa)")
            return False
        
        # Cek apakah masih ada giliran tersisa
        if self.uses_left <= 0:
            print(f"FireBlast tidak memiliki giliran tersisa! (0/{self.max_uses})")
            return False
        
        # Cek apakah caster memiliki cukup mana
        if caster._mana < self.mana_cost:
            print(f"Mana tidak cukup! Butuh {self.mana_cost}, memiliki {caster._mana}")
            return False
        
        # Fireblast dieksekusi
        damage = int(caster._attack * 1.5)
        caster._mana -= self.mana_cost
        target.take_damage(damage)
        self.uses_left -= 1
        self.cooldown = self.max_cooldown
        
        print(f"{caster.name} menyerang {target.name} dengan FireBlast!")
        print(f"Memberikan {damage} damage api! Sisa penggunaan: {self.uses_left}/{self.max_uses}")
        return True
    
    def reduce_cooldown(self):
        # Mengurangi cooldown sebanyak 1 setiap giliran
        if self.cooldown > 0:
            self.cooldown -= 1


class Heal(Ability):
    def __init__(self):
        self.mana_cost = 20
        self.cooldown = 0
        self.max_cooldown = 2
    
    def use(self, caster, target):
        # Cek apakah ability masih di cooldown
        if self.cooldown > 0:
            print(f"Heal masih cooldown! ({self.cooldown} giliran tersisa)")
            return False
        
        # Cek apakah caster memiliki cukup mana
        if caster._mana < self.mana_cost:
            print(f"Mana tidak cukup! Butuh {self.mana_cost}, memiliki {caster._mana}")
            return False
        
        # Cek apakah HP caster < 30%
        max_hp = caster._hp + 100  # Anggap HP maksimum adalah 100 lebih dari HP saat ini
        hp_percentage = (caster._hp / max_hp) * 100
        if hp_percentage >= 30:
            print(f"Heal hanya bisa digunakan ketika HP < 30%! HP sekarang: {hp_percentage:.1f}%")
            return False
        
        # Execute Heal
        heal_amount = int(caster._attack * 0.8)
        caster._mana -= self.mana_cost
        caster._hp += heal_amount
        self.cooldown = self.max_cooldown
        
        print(f"{caster.name} menggunakan Heal!")
        print(f"Mengembalikan {heal_amount} HP! HP sekarang: {caster._hp}")
        return True
    
    def reduce_cooldown(self):
        # Mengurangi cooldown sebanyak 1 setiap giliran
        if self.cooldown > 0:
            self.cooldown -= 1