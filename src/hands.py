import random
from itertools import product, combinations, permutations

import pandas as pd
import numpy as np

from src.cards import *
from src.utils import *


# pairs
pair_list = [f"{i}{i}" for i in hight_list]


# pair dict --> list pairs pour une clé
pair_dict = {i: make_permutations(i) for i in pair_list}


# suited_list
suited_list = list(product(hight_list, hight_list))
suited_list = [f"{i}{j}" for i, j in suited_list]
suited_list = [i for i in suited_list if i not in pair_list]
suited_list = list(map(orderize, suited_list))
suited_list = list(map(lambda i: i + "s", suited_list))


# suited_dict
def make_suited_comb(txt):
    cards = [(txt, color) for color in color_list]
    cards = [(f"{i[0]}{j}", f"{i[1]}{j}") for i, j in cards]
    return cards


suited_dict = {i: make_suited_comb(i) for i in suited_list}


# offsuit_list
offsuit_list = list(map(lambda i: i[:-1] + "o", suited_list))


# offsuit_dict
def make_offsuit_comb(i):

    cards = list(product(i[:-1], color_list))
    cards = [i + j for i, j in cards]
    cards = list(permutations(cards, 2))
    cards = [(i, j) for i, j in cards if i[0] != j[0]]
    cards = [(i, j) for i, j in cards if i[-2:] != j[-2:]]
    return cards


offsuit_dict = {i: make_offsuit_comb(i) for i in offsuit_list}


# all hands
all_hands = offsuit_list + suited_list + pair_list
