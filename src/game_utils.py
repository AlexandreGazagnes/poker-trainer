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
