import random

BLOCK_VAL = 0.05
"""
    TODO
    add docstrings to each function/flush it out
"""


def is_in_combat(player, room):
    dragons = ["earth", "water", "fire"]
    """
    TODO:
    remove the dragons check here move it to room
    have it called is_dragon_near
    """
    # adjacents
    if room.room[player.get_player_x()][player.get_player_y()] in dragons:
        return True
    elif room.room[player.get_player_x()+1][player.get_player_y()] in dragons:
        return True
    elif room.room[player.get_player_x()-1][player.get_player_y()] in dragons:
        return True
    elif room.room[player.get_player_x()][player.get_player_y()+1] in dragons:
        return True
    elif room.room[player.get_player_x()][player.get_player_y()-1] in dragons:
        return True

    # diagonals
    elif room.room[player.get_player_x()+1][player.get_player_y()+1] in dragons:
        return True
    elif room.room[player.get_player_x()+1][player.get_player_y()-1] in dragons:
        return True
    elif room.room[player.get_player_x()-1][player.get_player_y()+1] in dragons:
        return True
    elif room.room[player.get_player_x()-1][player.get_player_y()-1] in dragons:
        return True
    else:
        return False


def quick_attack(player, dragon, num):
    if num <= player.get_player_qa_acc():
        dragon.set_drag_health(dragon.get_drag_health() -
                               player.get_player_qa_dmg())
        return True
    return False


def heavy_attack(player, dragon, num):
    if num <= player.get_player_ha_acc():
        dragon.set_drag_health(dragon.get_drag_health() -
                               player.get_player_ha_dmg())
        return True
    return False


def block(player, num):
    if num <= player.get_player_bl_acc():
        return True
    return False


def dodge(player, num):
    if num <= player.get_player_do_acc():
        return True
    return False


def claw(player, dragon, block, dodge):
    if dodge:
        return -1
    elif block:
        player.set_player_health(
            player.get_player_health()-(dragon.get_drag_claw() * BLOCK_VAL))
        return 0
    else:
        player.set_player_health(
            player.get_player_health()-dragon.get_drag_claw())
        return 1


def breath(player, dragon, block, dodge):
    if dodge:
        return -1
    elif block:
        player.set_player_health(
            player.get_player_health()-(dragon.get_drag_breath() * BLOCK_VAL))
        return 0
    else:
        player.set_player_health(
            player.get_player_health()-dragon.get_drag_breath())
        return 1


def tail(player, dragon, block, dodge):
    if dodge:
        return -1
    elif block:
        player.set_player_health(
            player.get_player_health()-(dragon.get_drag_tail() * BLOCK_VAL))
        return 0
    else:
        player.set_player_health(
            player.get_player_health()-dragon.get_drag_tail())
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
    """
    TODO
    change to the get/set functions
    """
    if player.current_health <= 0:
        return 0
    elif dragon.current_health <= 0:
        dragons.clear_dragon(dragon)
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
