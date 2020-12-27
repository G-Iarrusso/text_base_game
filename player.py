class Player:
    def __init__(self, starting_health, current_health, player_x, player_y):
        self.starting_health = starting_health
        self.current_health = current_health
        self.player_x = player_x
        self.player_y = player_y

    def take_damage(self, damage):
        if self.current_health - damage <= 0:
            print("You've died")
        else:
            self.current_health = self.current_health - damage

    def heal_all(self):
        self.current_health = self.starting_health

    def heal(self, amount):
        self.current_health = self.current_health + amount

    def gain_armor(self, armour):
        self.starting_health = self.starting_health + armour
        self.current_health = self.current_health + armour

    def print_player(self):
        print("Starting health: " + str(self.starting_health) + " Current Health: " + str(self.current_health))
        print("X: " + str(self.player_x + 1) + " Y: " + str(self.player_y + 1))
