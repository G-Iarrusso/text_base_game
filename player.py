# player stats
quick_attack_dmg = 15
quick_attack_acc = 95

heavy_attack_dmg = 30
heavy_attack_acc = 75

dodge_acc = 75

block_acc = 95
block_val = 0.05


class Player:
    def __init__(self, starting_health, current_health, player_x, player_y):
        """
        single player
        """
        self.starting_health = starting_health
        self.current_health = current_health
        self.starting_bandage = 3
        self.current_bandage = 3
        self.player_x = player_x
        self.player_y = player_y

        self.quick_attack_dmg = 15
        self.quick_attack_acc = 95
        self.heavy_attack_dmg = 30
        self.heavy_attack_acc = 75
        self.dodge_acc = 75
        self.block_acc = 95

    def is_dead(self):
        return self.current_health <= 0

    def take_damage(self, damage):
        """
        adjusts health based on damage taken
        """
        if self.current_health - damage <= 0:
            print("You've died")
        else:
            self.current_health = self.current_health - damage

    def heal_all(self):
        """
        heals the player to their starting health
        """
        self.current_health = self.starting_health

    def heal(self, amount):
        """
        heals player by the given amount
        """
        self.current_health = self.current_health + amount

    def gain_armour(self, armour):
        """
        gaining armor adds an amount to the players starting and current health
        """
        self.starting_health = self.starting_health + armour
        self.current_health = self.current_health + armour

    def bandage(self):
        if self.bandage > 0:
            self.bandage = self.bandage - 1
            self.heal(5)
            return True
        return False

    def gain_damage(self, amount):
        self.heavy_attack_dmg = self.heavy_attack_dmg + amount
        self.quick_attack_dmg = self.quick_attack_dmg + amount

    def add_bandage(self, amount):
        self.current_bandage = self.current_bandage + amount
        self.starting_bandage = self. starting_bandage + amount

    def reset_bandage(self):
        self.current_bandage = self.add_bandage

    def get_player_x(self):
        return self.player_x

    def get_player_y(self):
        return self.player_y

    def get_player_health(self):
        return self.current_health

    def get_player_qa_dmg(self):
        return self.quick_attack_dmg

    def get_player_qa_acc(self):
        return self.quick_attack_acc

    def get_player_ha_dmg(self):
        return self.heavy_attack_dmg

    def get_player_ha_acc(self):
        return self.heavy_attack_acc

    def get_player_do_acc(self):
        return self.dodge_acc

    def get_player_bl_acc(self):
        return self.block_acc
