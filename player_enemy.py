from character_ability import Character
import random

class Player(Character):
    def __init__(self, name, hp, mana, attack, defense):
        super().__init__(name, hp, mana, attack, defense)
        self.steps = 0
        self.cooldowns = {"FireBlast": 0, "Heal": 0}

    def walk(self):
        #menambah langkah player
        self.steps += 1
        print(f"{self.name} berjalan... Langkah ke-{self.steps}")

        #musuh muncul jika langkah kelipatan 3 dan bukan kelipatan 5
        if self.steps % 3 == 0 and self.steps % 5 != 0:
            print("⚔️  Musuh muncul di depanmu!")
            return True
        else:
            print("Tidak ada musuh di sekitar.")
            return False

    def choose_action(self):
        while True:
            print("\n=== Your Turn ===")
            print("1. Attack")
            print("2. Ability")
            choice = input("Pilih aksi (1/2): ")

            if choice in ["1", "2"]:
                break
            else:
                print("Pilihan tidak valid, coba lagi.")

        if choice == "1":
            return "attack"
        else:
            return "ability"
                


class Enemy(Character):
    def __init__(self, name, hp, mana, attack, defense):
        super().__init__(name, hp, mana, attack, defense)

    @staticmethod
    def generate_random_enemy():
        enemy_data = [
            ("Goblin", 60, 30, 8, 3),
            ("Slime", 50, 25, 6, 2),
            ("Skeleton", 70, 20, 10, 4),
            ("Wolf", 80, 15, 12, 5),
        ]
        name, hp, mana, attack, defense = random.choice(enemy_data)
        return Enemy(name, hp, mana, attack, defense)

    def choose_action(self):
        #action musuh dipilih secara acak
        return random.choice(["attack", "ability"])
