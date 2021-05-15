# player stats


class Player:
    def __init__(self, starting_health, current_health, player_x, player_y):
        """
        Intiilize the player
        args:
            starting_health - player starting health - int
            current_helth -  the players current health - int
            player_x - the players current x - int
            player_y - the players current y - int
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
        """
        checks if the player is dead
        returns:
            True if the player is dead, false if alive
        """
        return self.current_health <= 0

    def take_damage(self, damage):
        """
        adjusts health based on damage taken
        args:
            damage - the damage the player has just taken - int
        returns:
            True if the player is dead, false if alive
        """
        self.current_health = self.current_health - damage
        return self.is_dead()

    def heal_all(self):
        """
        heals the player to their starting health
        """
        self.current_health = self.starting_health

    def heal(self, amount):
        """
        heals player by the given amount
        args:
            amount - how much they are getting healed by - int
        """
        self.current_health = self.current_health + amount

    def gain_armour(self, armour):
        """
        gaining armor adds an amount to the players starting and current health
        args:
            armour - the armour they are gaining - int
        """
        self.starting_health = self.starting_health + armour
        self.current_health = self.current_health + armour

    def bandage(self):
        """
        the user healing for a predetermined value
        returns:
            True if heal successful, False if not
        """
        if self.current_bandage > 0:
            self.current_bandage = self.current_bandage - 1
            self.heal(5)
            return True
        return False

    def gain_damage(self, amount):
        """
        the use gains base damage
        args: 
            amount - the amount of damage they gain - int
        """
        self.heavy_attack_dmg = self.heavy_attack_dmg + amount
        self.quick_attack_dmg = self.quick_attack_dmg + amount

    def add_bandage(self, amount):
        """
        add a bandage to the bandage count
        args:
            amount - gain a number of bandages - int
        """
        self.current_bandage = self.current_bandage + amount
        self.starting_bandage = self. starting_bandage + amount

    def reset_bandage(self):
        """
        reste the user to their total amount of bandages
        """
        self.current_bandage = self.add_bandage

    def get_player_x(self):
        """
        get the players x value
        returns:
            players x value
        """
        return self.player_x

    def get_player_y(self):
        """
        get the players y value
        returns:
            players y value
        """
        return self.player_y

    def get_player_health(self):
        """
        get the players current health
        returns:
            player health
        """
        return self.current_health

    def get_player_starting_health(self):
        """
        get the players starting health
        returns:
            player starting health
        """
        return self.starting_health

    def get_player_qa_dmg(self):
        """
        get the players quick attack damage
        returns:
            quick attack damage
        """
        return self.quick_attack_dmg

    def get_player_qa_acc(self):
        """
        get the players quick attack accuracy
        returns:
            quick attack accuracy
        """
        return self.quick_attack_acc

    def get_player_ha_dmg(self):
        """
        get the players heavy attack damage
        returns:
            heavy attack damage
        """
        return self.heavy_attack_dmg

    def get_player_ha_acc(self):
        """
        get the players heavy attack accuracy
        returns:
            heavy attack accuracy
        """
        return self.heavy_attack_acc

    def get_player_do_acc(self):
        """
        get the players dodge accuracy
        returns:
            dodge accuracy
        """
        return self.dodge_acc

    def get_player_bl_acc(self):
        """
        get the players block accuracy
        returns:
            block accuracy
        """
        return self.block_acc

    def set_player_x(self, x):
        """
        set the players x value
        args:
            x -  new x value - int
        """
        self.player_x = x

    def set_player_y(self, y):
        """
        set the players y value
        args:
            y -  new y value - int
        """
        self.player_y = y

    def set_player_health(self, health):
        """
        set the players health
        args:
            health -  new health value - int
        """
        self.current_health = health
