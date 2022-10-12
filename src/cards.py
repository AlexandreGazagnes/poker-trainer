"""
About cards

old : 
    funct are OK

new  : 
    class Card              OK
    class Give              OK
    class Board             OK
    class Deck              OK
    class Comb              OK
    class Hand              OK
    funct compare_hands     OK
"""

from itertools import product
from src.translate import *

from functools import reduce

from src.cards_utils import *

import random
import numpy as np
from pandas import Series


# hights values list and dict
hight_values = list(range(2, 15))
hight_list = ["2", "3", "4", "5", "6", "7", "8", "9", "t", "j", "q", "k", "a"]
hight_dict = {i: j for i, j in zip(hight_list, hight_values)}
reverse_hight_dict = {j: i for i, j in zip(hight_list, hight_values)}

# color
color_list = ("tr", "pi", "ca", "co")

# card
card_list = deck = list(product(hight_list, color_list))
card_list = deck = [f"{i}{j}" for i, j in deck]


##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################


class Card:
    """class card IS OK"""

    def __init__(self, name_color):
        """ """

        self.id = name_color

        name = name_color[0]
        color = name_color[1:]

        self.name = name.upper()

        self.value = None
        for name, value in [("A", 14), ("K", 13), ("Q", 12), ("J", 11), ("T", 10)]:
            if self.name == name:
                self.value = value
        if not self.value:
            self.value = int(self.name)

        self.color = color

    def __repr__(self):
        """ """

        return (
            f"Card(id:{self.id},name:{self.name},color:{self.color},value:{self.value})"
        )

    @property
    def dict(self):
        return self.__dict__


class Give:
    """class Give IS OK"""

    def __init__(self, card_1, card_2):
        """ """

        if not isinstance(card_1, Card):
            card_1 = Card(card_1)
        if not isinstance(card_2, Card):
            card_2 = Card(card_2)

        if card_1.id == card_2.id:
            raise AttributeError(f"{card_1} == {card_2}, which is impossible man!  ")
        self.card_1 = card_1
        self.card_2 = card_2

        self.cards = (card_1, card_2)
        self.id = (card_1.id, card_2.id)

        self.name = translate_hand(self.id)

        self.is_pair = True if self.name[0] == self.name[1] else False
        self.is_suited = True if self.name[-1] == "s" else False

        self.abs_preflop_VE = -1
        self.abs_preflop_winrate = -1

    def __repr__(self):
        """ """

        return f"Give(id:{self.id}, name:{self.name}, abs_preflop_VE/winrate:{self.abs_preflop_VE}/{self.abs_preflop_winrate})"

    @property
    def dict(self):
        return self.__dict__


class Board:
    """class Board IS OK"""

    def __init__(self, c1, c2, c3, c4, c5):
        """ """

        self.cards = [c1, c2, c3, c4, c5]
        self.flop = [c1, c2, c3]
        self.turn = c4
        self.river = c5

    def __repr__(self):
        """ """

        return f"Board(flop={[i.id for i in self.flop]}, turn={self.turn.id}, river={self.river.id})"

    @property
    def dict(self):
        return self.__dict__


class Deck:
    """class Deck IS OK"""

    HIGH_LIST = ["2", "3", "4", "5", "6", "7", "8", "9", "t", "j", "q", "k", "a"]
    COLOR_LIST = ("tr", "pi", "ca", "co")

    def __init__(self):
        """ """

        card_list = list(product(self.HIGH_LIST, self.COLOR_LIST))
        card_list = [f"{i.lower()}{j}" for i, j in card_list]
        random.shuffle(card_list)

        self.init_cards = [Card(i) for i in card_list]
        self.current_cards = [Card(i) for i in card_list]

        self.pairs_asked = 0
        self.board_asked = 0

    def give(self):
        """ask 2 cards """

        if self.board_asked:
            raise AttributeError("no pair after flop asked")

        self.pairs_asked += 1

        c1 = self.current_cards.pop()
        c2 = self.current_cards.pop()

        return Give(c1, c2)

    def board(self):
        """ """

        if self.board_asked:
            raise AttributeError("Board alerady called ")

        if not self.pairs_asked >= 2:
            raise AttributeError("2 pairs must be asked before")

        self.board_asked = 1

        c1 = self.current_cards.pop()
        c2 = self.current_cards.pop()
        c3 = self.current_cards.pop()
        c4 = self.current_cards.pop()
        c5 = self.current_cards.pop()

        return Board(c1, c2, c3, c4, c5)

    @property
    def dict(self):
        return self.__dict__


class Comb:
    """class COMB IS OK """

    EN_LABELS = [
        "high_card",
        "pair",
        "2_pairs",
        "three_of_kind",
        "straight",
        "flush",
        "full_house",
        "four_of_kind",
        "straight_flush",
        "royal_straight_flush",
    ]

    ORDER_VALUE = {v: 100 * k for k, v in enumerate(EN_LABELS)}

    def __init__(self, name, max_value, color=None):

        self.value = self.ORDER_VALUE[name] + max_value
        self.name = name
        self.color = color
        self.max_value = max_value

    def __repr__(self):
        return f"Comb(val:{self.value}, name:{self.name}, color:{self.color}, max_value:{self.max_value})"

    @property
    def dict(self):
        return self.__dict__


class Hand:
    """class HAND
    ALOMOST OK, IL MANQUE DES METHODES DE _eval"""

    def __init__(self, c0, c1, c2=None, c3=None, c4=None, c5=None, c6=None):

        # self.c0 = c0
        # self.c1 = c1
        # self.c2 = c2
        # self.c3 = c3
        # self.c4 = c4
        # self.c5 = c5
        # self.c6 = c6

        self.comb_list = []

        # self.give = Give(c0, c1)

        self.cards = [i for i in [c0, c1, c2, c3, c4, c5, c6] if i]

        self.eval_all()

    @property
    def best_comb(self):
        """IS OK """

        return sorted(self.comb_list, key=lambda i: i.value, reverse=True)[0]

    def _eval_high_card(self):
        """IS OK """

        for card in self.cards:
            comb = Comb("high_card", card.value)
            self.comb_list.append(comb)

    def _eval_pairs(self):
        """ IS OK"""

        # colors
        values = Series([i.value for i in self.cards])

        # nb cards by value
        val_counts = values.value_counts().to_dict()

        # only 5 or more same color
        val_counts = {i: j for i, j in val_counts.items() if j >= 2}

        # if nothing
        if not len(val_counts.keys()):
            return None

        # print("find a pair")

        for i in val_counts.keys():

            comb = Comb("pair", i)
            self.comb_list.append(comb)

    def _eval_three_of_kind(self):
        """ IS OK"""

        # colors
        values = Series([i.value for i in self.cards])

        # nb cards by value
        val_counts = values.value_counts().to_dict()

        # only 5 or more same color
        val_counts = {i: j for i, j in val_counts.items() if j >= 3}

        # if nothing
        if not len(val_counts.keys()):
            return None

        # print("find a three_of_kind")

        for i in val_counts.keys():

            comb = Comb("three_of_kind", i)
            self.comb_list.append(comb)

    def _eval_2_pairs(self):
        """IS OK BUT NOT MAX_VAL.... """

        pairs = [i.value for i in self.comb_list if i.name == "pair"]
        pairs = sorted(pairs, reverse=True)

        if not (len(pairs) >= 2):
            return None

        # print("find a 2_pairs")

        pairs = pairs[:2]
        val = sum(pairs)
        comb = Comb("2_pairs", val)
        self.comb_list.append(comb)

    def _eval_four_of_kind(self):
        """ is OK"""

        # colors
        values = Series([i.value for i in self.cards])

        # nb cards by value
        val_counts = values.value_counts().to_dict()

        # only 5 or more same color
        val_counts = {i: j for i, j in val_counts.items() if j >= 4}

        # if nothing
        if not len(val_counts.keys()):
            return None

        # print("find a four_of_kind")

        for i in val_counts.keys():
            comb = Comb("four_of_kind", i)
            self.comb_list.append(comb)

    def _eval_straight(self):
        """ IS Ok"""

        values = sorted([i.value for i in self.cards])

        val = is_straight(values)

        if val == -1:
            return None

        # print("find a straight")

        comb = Comb("straight", val)
        self.comb_list.append(comb)

    def _eval_flush(self):
        """IS OK """

        # colors
        colors = Series([i.color for i in self.cards])

        # nb cards by color
        val_counts = colors.value_counts().to_dict()

        # only 5 or more same color
        val_counts = {i: j for i, j in val_counts.items() if j >= 5}

        # if nothing
        if not len(val_counts.keys()):
            return None

        # print("find a flush")

        # else there is a flush / color & max val
        color = list(val_counts.keys())[0]
        max_value = max([i.value for i in self.cards])

        # comb & comb_list
        comb = Comb("flush", max_value, color)
        self.comb_list.append(comb)

    def _eval_full_house(self):
        """ """

        # flush = [i.value for i in self.comb_list if i.name == "flush"]
        # straight = [i.value for i in self.comb_list if i.name == "straight"]

        # if flush and straight:
        #     print("full house found")
        #     comb = Comb("full_house", 0)
        #     self.comb_list.append(comb)

        pass

    def _eval_straight_flush(self):
        """IS OK """

        flush = [i for i in self.comb_list if i.name == "flush"]
        straight = [i for i in self.comb_list if i.name == "straight"]

        if flush and straight:
            val = max([i.max_value for i in straight])
            color = flush[0].color

            # print("straight_flush found")

            comb = Comb("straight_flush", val, color=color)
            self.comb_list.append(comb)

    def _eval_royal_straight_flush(self):
        """IS OK """

        straight_flush = [i for i in self.comb_list if i.name == "straight_flush"]

        if straight_flush:

            val = straight_flush[0].max_value
            color = straight_flush[0].color

            # if as
            if val == 14:
                print("royal_straight_flush found")
                comb = Comb("royal_straight_flush", val)
                self.comb_list.append(comb)

    def eval_all(self):
        """IL EN MANQUE """

        # high card
        self._eval_high_card()

        # a 2 cartes
        # pairs
        if len(self.cards) >= 2:
            self._eval_pairs()

        # a 3 cartes
        # three_of_kind
        if len(self.cards) >= 3:
            self._eval_three_of_kind()

        # a 4 cartes
        #  2 pairs
        if len(self.cards) >= 4:
            self._eval_2_pairs()

        #  four_of_kind
        if len(self.cards) >= 4:
            self._eval_four_of_kind()

        # a 5 cartes
        # straight
        if len(self.cards) >= 5:
            self._eval_straight()

        # flush
        if len(self.cards) >= 5:
            self._eval_flush()

        # full_house
        if len(self.cards) >= 5:
            self._eval_full_house()

        # straight_flush
        if len(self.cards) >= 5:
            self._eval_straight_flush()

        # royal_straight_flush
        if len(self.cards) >= 5:
            self._eval_royal_straight_flush()

    @property
    def dict(self):
        return self.__dict__


def compare_hands(hand_list):
    """IS OK """

    # best val of all combs
    max_val = max([i.best_comb.value for i in hand_list])

    # id, best_comb val
    li = [(i, v.best_comb.value) for i, v in enumerate(hand_list)]

    # sort by val reverse
    li = sorted(li, key=lambda i: i[1], reverse=True)

    # select only best
    winers = [i for i, v in li if v == max_val]

    # final
    result = [0] * len(hand_list)
    for i in winers:
        result[i] = 1

    return result


if __name__ == "__main__":

    from src.cards import *

    L = list()
    L.append(["ttr", "8pi", "7co", "6co", "2tr"])  # High_card
    L.append(["9tr", "9pi", "7co", "6co", "2tr"])  # Pair
    L.append(["9tr", "9ca", "api", "aca", "3ca"])  # 2 pairs
    L.append(["9tr", "9pi", "9co", "6co", "5tr"])  # three_of_kind

    L.append(["6tr", "5pi", "4co", "3co", "2tr"])  # straight
    L.append(["ttr", "8tr", "7tr", "6tr", "2tr"])  # Flush
    # full_house
    L.append(["9tr", "9ca", "9pi", "9co", "3ca"])  # four_of_kind
    L.append(["6tr", "5tr", "4tr", "3tr", "2tr"])  # straight_flush
    L.append(["atr", "ktr", "qtr", "jtr", "ttr"])  # straight_flush

    hand_list = list()
    for cards in L:

        objs = [Card(i) for i in cards]
        hand = Hand(*objs)
        hand_list.append(hand)

        # print(hand.comb_list)
        print(cards)
        print(hand.best_comb)
        print("\n")

        # li = [(i, v.best_comb) for i, v in enumerate(hand_list)]
        # print(li)

        # winer = compare_hands(hand_list)
        # print(winer)
