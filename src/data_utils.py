from src.cards import *
from itertools import *

import random


def name_categ_position(n_players, me_position):

    if n_players == 2:
        me_name = "SB" if not me_position else "BB"
        me_categ = "-"

    if n_players == 3:
        if not me_position:
            me_name = "SB"
            me_categ = "early"
        if me_position == 1:
            me_name = "BB"
            me_categ = "middle"
        if me_position == 2:
            me_name = "button"
            me_categ = "late"

    if n_players == 4:
        if not me_position:
            me_name = "SB"
            me_categ = "blind"
        if me_position == 1:
            me_name = "BB"
            me_categ = "early"
        if me_position == 2:
            me_name = "mp"
            me_categ = "middle"
        if me_position == 3:
            me_name = "button"
            me_categ = "late"

    if n_players == 5:
        if not me_position:
            me_name = "SB"
            me_categ = "blind"
        if me_position == 1:
            me_name = "BB"
            me_categ = "blind"
        if me_position == 2:
            me_name = "utg"
            me_categ = "early"
        if me_position == 3:
            me_name = "mp"
            me_categ = "middle"
        if me_position == 4:
            me_name = "button"
            me_categ = "late"

    if n_players == 6:
        if not me_position:
            me_name = "SB"
            me_categ = "blind"
        if me_position == 1:
            me_name = "BB"
            me_categ = "blind"
        if me_position == 2:
            me_name = "utg"
            me_categ = "early"
        if me_position == 3:
            me_name = "mp"
            me_categ = "middle"
        if me_position == 4:
            me_name = "cutoff"
            me_categ = "middle"
        if me_position == 5:
            me_name = "button"
            me_categ = "late"

    if n_players == 7:
        if not me_position:
            me_name = "SB"
            me_categ = "blind"
        if me_position == 1:
            me_name = "BB"
            me_categ = "blind"
        if me_position == 2:
            me_name = "utg"
            me_categ = "early"
        if me_position == 3:
            me_name = "utg+1"
            me_categ = "middle"
        if me_position == 4:
            me_name = "mp"
            me_categ = "middle"
        if me_position == 5:
            me_name = "cutoff"
            me_categ = "middle"
        if me_position == 6:
            me_name = "button"
            me_categ = "late"

    if n_players == 8:
        if not me_position:
            me_name = "SB"
            me_categ = "blind"
        if me_position == 1:
            me_name = "BB"
            me_categ = "blind"
        if me_position == 2:
            me_name = "utg"
            me_categ = "early"
        if me_position == 3:
            me_name = "utg+1"
            me_categ = "early"
        if me_position == 4:
            me_name = "mp"
            me_categ = "middle"
        if me_position == 5:
            me_name = "mp+1"
            me_categ = "middle"
        if me_position == 6:
            me_name = "cutoff"
            me_categ = "late"
        if me_position == 7:
            me_name = "button"
            me_categ = "late"

    return me_name, me_categ


def find_all_fold(dd):

    # si personne a parlé ==> 0
    if not dd:
        return 0

    # liste 1 / 0 si fold ou pas
    actions = list(dd.values())
    fold = ["fold" in i.lower() for i in actions]

    return 1 if all(fold) else 0


def BB_should_check(dd):

    # si on est BB, on est pas dans le dict
    if 1 not in list(dd.keys()):
        return dd

    actions = list(dd.values())

    # si one raise et
    #   return  dd no change

    one_raise = ["raise" in i.lower() for i in actions]
    if any(one_raise):
        return dd

    # # si tout le monde call la bb devient un check
    # call = ["call" in i.lower() for i in actions]
    # if all(call):
    #     dd[1] = "check"
    #     return dd

    #  toutle monde call OU fold alors la BB should check
    call_or_fold = lambda i: ("call" in i.lower()) or ("fold" in i.lower())
    call_or_fold = [call_or_fold(i) for i in actions]
    if all(call_or_fold):
        dd[1] = "check"
        return dd


def define_plays(me_position, n_players, actions, amounts):

    # plays
    plays = {
        i: (random.choice(actions), random.choice(amounts)) for i in range(n_players)
    }
    # 2 players
    if n_players == 2:
        if me_position == 0:
            # je suis sb, à 2 ca fait sb puis bb 1er de parole en preflop
            plays = {}
        else:
            # je suis bb, ca fait sb, bb, puis RE sb
            plays.pop(me_position)

    # 3 players
    if n_players == 3:
        # me se pope
        plays.pop(me_position)
        # a 3 si me au sb, seul le button (2) aura parlé
        if me_position == 0:
            plays.pop(me_position + 1)
        # a 3 si me au bbutton, je suis le 1er à parler
        if me_position == 2:
            plays = {}

    # 4 players
    if n_players == 4:
        # me se pope
        plays.pop(me_position)
        # position 2 je suis le 1er à parler apres SB et BB
        if me_position == 2:
            plays = {}
        # me au button, sb et bb n'ont pas parlé
        if me_position == 3:
            plays.pop(0)
            plays.pop(1)
        # me au sb la bb n'a pas parlé
        if me_position == 0:
            plays.pop(1)

    # more players
    if n_players > 4:
        # TODO
        pass

    clean_amount = lambda i, j: f"{i} - " if i != "raise" else f"{i} - {j}"
    plays = {k: clean_amount(*v) for k, v in plays.items()}

    return plays
