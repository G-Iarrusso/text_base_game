import random

BLOCK_VAL = 0.05
"""
    TODO
    add docstrings to each function/flush it out
"""


def is_in_combat(player, room):
    """
    is the player currently in combat
    args:
        player - the player object
        room - the current room situation
    returns:
        True if player in combat, False if not
    """
    dragons = ["earth", "water", "fire"]
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
    return False


def quick_attack(player, dragon, acc_num):
    """
    execute a quick attack
    args:
        player - the player object
        dragon - the dragon the player is in combat with
        acc_num - the random accuracy number
    returns:
        True if player in combat, False if not
    """
    if acc_num <= player.get_player_qa_acc():
        dragon.set_drag_health(dragon.get_drag_health() -
                               player.get_player_qa_dmg())
        return True
    return False


def heavy_attack(player, dragon, acc_num):
    """
    execute a heavys attack
    args:
        player - the player object
        dragon - the dragon the player is in combat with
        acc_num - the random accuracy number
    returns:
        True if player in combat, False if not
    """
    if acc_num <= player.get_player_ha_acc():
        dragon.set_drag_health(dragon.get_drag_health() -
                               player.get_player_ha_dmg())
        return True
    return False


def block(player, acc_num):
    """
    execute a block
    args:
        player - the player object
        dragon - the dragon the player is in combat with
        acc_num - the random accuracy number
    returns:
        True if player in combat, False if not
    """
    if acc_num <= player.get_player_bl_acc():
        return True
    return False


def dodge(player, acc_num):
    """
    execute a dodge
    args:
        player - the player object
        dragon - the dragon the player is in combat with
        acc_num - the random accuracy number
    returns:
        True if player in combat, False if not
    """
    if acc_num <= player.get_player_do_acc():
        return True
    return False


def claw(player, dragon, block, dodge):
    """
    execute a dragon claw
    args:
        player - the player object
        dragon - the dragon the player is in combat with
        block - player block outcome
        dodge - player dodge outcome
    returns:
        -1 - dodge successful
        0 - block succesful minor damage taken
        1 - attack connects
    """
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
    """
    execute a dragon breath
    args:
        player - the player object
        dragon - the dragon the player is in combat with
        block - player block outcome
        dodge - player dodge outcome
    returns:
        -1 - dodge successful
        0 - block succesful minor damage taken
        1 - attack connects
    """
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
    """
    execute a dragon tail
    args:
        player - the player object
        dragon - the dragon the player is in combat with
        block - player block outcome
        dodge - player dodge outcome
    returns:
        -1 - dodge successful
        0 - block succesful minor damage taken
        1 - attack connects
    """
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
    """
    execute the player combat
    args:
        player - the player object
        dragon - the dragon the player is in combat with
        action - the user input  - string
    returns:
        value coresponding to outcome of user action
        -1 if user inputs incorrect value
    """
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
    """
    execute a dragon combat
    args:
        player - the player object
        dragon - the dragon the player is in combat with
        block - player block outcome
        dodge - player dodge outcome
    """
    drag_action = random.randint(1, 3)
    if drag_action == 1:
        claw(player, dragon, block, dodge)

    elif drag_action == 2:
        tail(player, dragon, block, dodge)

    elif drag_action == 3:
        breath(player, dragon, block, dodge)


def check_deaths(player, dragon, dragons):
    """
    check if there anyone died
    args
        player - player in the game
        dragon - current dragon in combat
        dragons - the current list of dragons
    returns
        0 - if player dies
        1 - if dragon dies
        -1 - if nothing dies
    """
    if player.get_player_health() <= 0:
        return 0
    elif dragon.get_drag_health() <= 0:
        dragons.clear_dragon(dragon)
        return 1
    return -1


def combat(player, dragon, dragons, action):
    """
    base combat function
    args
        player - player in the game
        dragon - current dragon in combat
        dragons - the current list of dragons
        action - player action
    """
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
