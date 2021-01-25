import random

"""
TODO
seperate combat to player and dragon combat
then have a combat function call both combats
"""
BLOCK_ACC = 0.05


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


def quick_attack(player, dragon, num):
    if num <= player.quick_attack_acc:
        dragon.current_health = dragon.current_health-player.quick_attack_dmg
        return True
    return False


def heavy_attack(player, dragon, num):
    if num <= player.heavy_attack_acc:
        dragon.current_health = dragon.current_health-player.heavy_attack_dmg
        return True
    return False


def block(player, num):
    if num <= BLOCK_ACC:
        return True
    return False


def dodge(player, num):
    if num <= player.dodge_acc:
        return True
    return False


def claw(player, dragon, block, dodge):
    if dodge:
        return -1
    elif block:
        player.current_health = player.current_health-(dragon.claw * dragon.block_val)
        return 0
    else:
        player.current_health = player.current_health-dragon.claw
        return 1


def breath(player, dragon, block, dodge):
    if dodge:
        return -1
    elif block:
        player.current_health = player.current_health-(dragon.breath * dragon.block_val)
        return 0
    else:
        player.current_health = player.current_health-dragon.breath
        return 1


def tail(player, dragon, block, dodge):
    if dodge:
        return -1
    elif block:
        player.current_health = player.current_health-(dragon.tail * dragon.block_val)
        return 0
    else:
        player.current_health = player.current_health-dragon.tail
        return 1


def player_combat(player, dragon, action):
    rand = random.randint(0, 100)
    if action == "qa":
        return quick_attack(player, dragon, rand)
    elif action == 'ha':
        return heavy_attack(player, dragon, rand)
    elif action == "bl":
        return block(player, rand)
    elif action == 'do':
        return dodge(player, rand)
    else:
        return -1


def dragon_combat(player, dragon, block, dodge):
    drag_action = random.randint(1, 3)
    if drag_action == 1:
        claw(player, dragon, block, dodge)

    elif drag_action == 2:
        tail(player, dragon, block, dodge)

    elif drag_action == 3:
        breath(player, dragon, block, dodge)


def check_deaths(player, dragon, dragons):
    if player.current_health <= 0:
        return 0
    elif dragon.current_health <= 0:
        dragons.clear_dragon(dragon)
        print("Your health: "+str(player.current_health))
        print("Dragons health: 0")
        return 1
    return -1


def combat(player, dragon, dragons, action):
    block = False
    dodge = False
    outcome_player = player_combat(player, dragon, action)
    if outcome_player != -1:
        if action == "bl":
            block = outcome_player
        elif action == "do":
            dodge = outcome_player
        dragon_combat(player, dragon, block, dodge)
        check_deaths(player, dragon, dragons)
