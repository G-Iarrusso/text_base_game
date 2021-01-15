import random
# player stats
quick_attack_dmg = 15
quick_attack_acc = 95

heavy_attack_dmg = 30
heavy_attack_acc = 75

dodge_acc = 75

block_acc = 95
block_val = 0.05

# dragon stats
claw_dmg = 5
breath_dmg = 10
tail_dmg = 15


class Player:
    def __init__(self, starting_health, current_health, player_x, player_y):
        """
        single player
        """
        self.starting_health = starting_health
        self.current_health = current_health
        self.player_x = player_x
        self.player_y = player_y

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
        heals the player to their startign health
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

    def is_in_combat(self, room):
        dragons = ["earth", "water", "fire"]
        # adjacents
        if room.room[self.player_x][self.player_y] in dragons:
            return True
        elif room.room[self.player_x+1][self.player_y] in dragons:
            return True
        elif room.room[self.player_x-1][self.player_y] in dragons:
            return True
        elif room.room[self.player_x][self.player_y+1] in dragons:
            return True
        elif room.room[self.player_x][self.player_y-1] in dragons:
            return True

        # diagonals
        elif room.room[self.player_x+1][self.player_y+1] in dragons:
            return True
        elif room.room[self.player_x+1][self.player_y-1] in dragons:
            return True
        elif room.room[self.player_x-1][self.player_y+1] in dragons:
            return True
        elif room.room[self.player_x-1][self.player_y-1] in dragons:
            return True

        else:
            return False

    def quick_attack(self, dragon, dragons, num):
        if num <= quick_attack_acc:
            print("You hit with a quick attack")
            dragon.current_health = dragon.current_health-quick_attack_dmg
        else:
            print("You miss with a quick attack")

    def heavy_attack(self, dragon, dragons, num):
        if num <= heavy_attack_acc:
            print("You hit with a heavy attack for big damage")
            dragon.current_health = dragon.current_health-heavy_attack_dmg
        else:
            print("You swing for a big attack but the dragon moves and you miss")

    def block(self, dragon, dragons, num):
        if num <= block_acc:
            print("You raise your shield")
            return True
        else:
            print("The dragon goes around your shield")

    def dodge(self, dragon, dragons, num):
        if num <= dodge_acc:
            print("You get ready to dodge the next attack")
            return True
        else:
            print("You trip while trying to get out of the way")

    def combat(self, dragon, dragons):

        while self.current_health > 0 and dragon.current_health > 0:
            block = False
            dodge = False
            """
            TODO we should move this interaction outside of the class
            """
            print("\nYour health: " + str(self.current_health))
            print("Dragons health: " + str(dragon.current_health))
            print("Enter one of these commands\n'qa' for quick attack\n'ha' for heavy attack\n'do' for dodge\n'bl' for block.")
            action = input('')
            rand = random.randint(0, 100)
            if action == "qa":
                self.quick_attack(dragon, dragons, rand)

            elif action == 'ha':
                self.heavy_attack(dragon, dragons, rand)

            elif action == "bl":
                block = self.block(dragon, dragons, rand)

            elif action == 'do':
                dodge = self.dodge(dragon, dragons, rand)

            else:
                print("Invalid command")
                continue

            drag_action = random.randint(1, 3)

            if drag_action == 1:
                if dodge:
                    print("You get out of the way of the claw")
                elif block:
                    print("Your shield aborbs most of the claw attack")
                    self.current_health = self.current_health-(claw_dmg * block_val)
                else:
                    print("The dragon swipes with its claws and hits you")
                    self.current_health = self.current_health-claw_dmg

            elif drag_action == 2:
                if dodge:
                    print("You get out of the way of the breath attack")
                elif block:
                    print("Your shield aborbs most of the breath attack")
                    self.current_health = self.current_health-(breath_dmg * block_val)
                else:
                    print("The dragon uses its dragon breath to hurt you")
                    self.current_health = self.current_health-breath_dmg

            elif drag_action == 3:
                if dodge:
                    print("You get out of the way of the tail attack")
                elif block:
                    print("Your shield aborbs most of the force of the tail")
                    self.current_health = self.current_health-(tail_dmg * block_val)
                else:
                    print("The dragon uses its dragon breath to hurt you")
                    self.current_health = self.current_health-tail_dmg

            if self.current_health <= 0:
                return False
            elif dragon.current_health <= 0:
                dragons.clear_dragon(dragon)
                print("Your health: "+str(self.current_health))
                print("Dragons health: 0")

                return True

