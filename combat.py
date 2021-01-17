import random


def is_in_combat(player, room):
    dragons = ["earth", "water", "fire"]
    # adjacents
    if room.room[player.player_x][player.player_y] in dragons:
        return True
    elif room.room[player.player_x+1][player.player_y] in dragons:
        return True
    elif room.room[player.player_x-1][player.player_y] in dragons:
        return True
    elif room.room[player.player_x][player.player_y+1] in dragons:
        return True
    elif room.room[player.player_x][player.player_y-1] in dragons:
        return True

    # diagonals
    elif room.room[player.player_x+1][player.player_y+1] in dragons:
        return True
    elif room.room[player.player_x+1][player.player_y-1] in dragons:
        return True
    elif room.room[player.player_x-1][player.player_y+1] in dragons:
        return True
    elif room.room[player.player_x-1][player.player_y-1] in dragons:
        return True

    else:
        return False


def quick_attack(player, dragon, dragons, num):
    if num <= quick_attack_acc:
        print("You hit with a quick attack")
        dragon.current_health = dragon.current_health-quick_attack_dmg
    else:
        print("You miss with a quick attack")


def heavy_attack(player, dragon, dragons, num):
    if num <= heavy_attack_acc:
        print("You hit with a heavy attack for big damage")
        dragon.current_health = dragon.current_health-heavy_attack_dmg
    else:
        print("You swing for a big attack but the dragon moves and you miss")


def block(player, dragon, dragons, num):
    if num <= block_acc:
        print("You raise your shield")
        return True
    else:
        print("The dragon goes around your shield")


def dodge(player, dragon, dragons, num):
    if num <= dodge_acc:
        print("You get ready to dodge the next attack")
        return True
    else:
        print("You trip while trying to get out of the way")


def combat(player, dragon, dragons):

    while player.current_health > 0 and dragon.current_health > 0:
        block = False
        dodge = False
        """
        TODO we should move this interaction outside of the class
        """
        print("\nYour health: " + str(player.current_health))
        print("Dragons health: " + str(dragon.current_health))
        print("Enter one of these commands\n'qa' for quick attack\n'ha' for heavy attack\n'do' for dodge\n'bl' for block.")
        action = input('')
        rand = random.randint(0, 100)
        if action == "qa":
            player.quick_attack(dragon, dragons, rand)

        elif action == 'ha':
            player.heavy_attack(dragon, dragons, rand)

        elif action == "bl":
            block = player.block(dragon, dragons, rand)

        elif action == 'do':
            dodge = player.dodge(dragon, dragons, rand)

        else:
            print("Invalid command")
            continue

        drag_action = random.randint(1, 3)

        if drag_action == 1:
            if dodge:
                print("You get out of the way of the claw")
            elif block:
                print("Your shield aborbs most of the claw attack")
                player.current_health = player.current_health-(claw_dmg * block_val)
            else:
                print("The dragon swipes with its claws and hits you")
                player.current_health = player.current_health-claw_dmg

        elif drag_action == 2:
            if dodge:
                print("You get out of the way of the breath attack")
            elif block:
                print("Your shield aborbs most of the breath attack")
                player.current_health = player.current_health-(breath_dmg * block_val)
            else:
                print("The dragon uses its dragon breath to hurt you")
                player.current_health = player.current_health-breath_dmg

        elif drag_action == 3:
            if dodge:
                print("You get out of the way of the tail attack")
            elif block:
                print("Your shield aborbs most of the force of the tail")
                player.current_health = player.current_health-(tail_dmg * block_val)
            else:
                print("The dragon uses its dragon breath to hurt you")
                player.current_health = player.current_health-tail_dmg

        if player.current_health <= 0:
            return False
        elif dragon.current_health <= 0:
            dragons.clear_dragon(dragon)
            print("Your health: "+str(player.current_health))
            print("Dragons health: 0")

            return True
