from character_ability import Character, Ability, FireBlast, Heal
from player_enemy import Player, Enemy
import time, random

class GameController:
    def __init__(self):
        self.player = Player("Hero", 100, 50, 15, 5)
        self.player.max_hp = self.player._hp

        self.fireblast = FireBlast()
        self.heal = Heal()

        self.enemy = None

    def find_enemy(self):
        while True:
            encounter = self.player.walk()
            if encounter:
                self.enemy = Enemy.generate_random_enemy()
                print(f"Musuh muncul : {self.enemy.name} (HP: {self.enemy._hp}, Mana: {self.enemy._mana})")
                break
            time.sleep(0.5)

    def player_turn(self):
        action = self.player.choose_action()

        if action == "attack":
            self.player.attack(self.enemy)
        else:
            print("\nPilih Ability:")
            print("1. FireBlast")
            print("2. Heal")
            choice = input("Masukkan pilihan (1/2): ")
            if choice == "1":
                self.fireblast.use(self.player, self.enemy)
            elif choice == "2":
                self.heal.use(self.player, self.player)
            else:
                print("Pilihan tidak valid, giliran dilewati")

    def enemy_turn(self):
        if not self.enemy.is_alive():
            return

        action = self.enemy.choose_action()
        if action == "attack":
            self.enemy.attack(self.player)
        else:
            if random.random() < 0.3 and self.enemy._mana >= 10:
                print(f"{self.enemy.name} mencoba menggunakan serangan spesial!")
                damage = int(self.enemy._attack * 1.2)
                self.player.take_damage(damage)
                self.enemy._mana -= 10
            else:
                self.enemy.attack(self.player)
                
    def end_of_round(self):
        self.fireblast.reduce_cooldown()
        self.heal.reduce_cooldown()

        self.player._mana = min(self.player._mana + 5, 50)
        self.enemy._mana = min(self.enemy._mana + 5, 50)

        print(f"\nEnd of Round - {self.player.name}: {self.player._mana} mana, {self.enemy.name}: {self.enemy._mana} mana\n")

    def battle(self):
        print("\nPertarungan dimulai!")
        while self.player.is_alive() and self.enemy.is_alive():
            print(f"\n{self.player.name}: HP {self.player._hp}/{self.player.max_hp} | Mana {self.player._mana}")
            print(f"{self.enemy.name}: HP {self.enemy._hp} | Mana {self.enemy._mana}")

            self.player_turn()

            if not self.enemy.is_alive():
                print(f"{self.enemy.name} dikalahkan!")
                break

            self.enemy_turn()

            if not self.player.is_alive():
                print(f"{self.player.name} tumbang! Game Over!")
                break

            self.end_of_round()
            time.sleep(0.5)

        if self.player.is_alive():
            print("Kamu menang!")
        else:
            print("Kamu kalah...")
            

    def start_game(self):
        print("=== Game Dimulai ===")
        while True:
            self.find_enemy()
            self.battle()

            if self.player.is_alive() == False:
                break

            cont = input("Lanjutkan perjalanan? (y/n): ").lower()
            while cont != "y" and cont != "n":
                print("Pilihan tidak valid, silahkan pilih ulang")
                cont = input("Lanjutkan perjalanan? (y/n): ").lower()
                

            if cont != "y":
                print("Petualangan berakhir. Terima kasih sudah bermain!")
                break   