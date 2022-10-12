"""
about game 

old : 
    is OK

new : 
    class Preflop           50% 
    class Flop              0% 
    class Turn              0%
    class River             0%
    class Round             0%
    class CashGame          0%


"""

import random
import numpy as np

from src.cards import *

from src.players import Player
from src.actions import Action
from .game_utils import name_categ_position


def pickup(k=2):

    return list(np.random.choice(deck, size=k, replace=False))


##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################


class Preflop:
    """class Preflop is 30% WIP """

    def __init__(self, players, deck):
        """ """

        self.init_players = players

        self.position_orders = []
        self.postion_names = []
        self.positions_categ = []

        self.action_list = []

        self.deck = deck
        self.board = []

        self.is_finished = 0
        self.winner = -1
        self.next_to_play = 0

        # Auto actions
        self.init_round()
        self.small_blind()
        self.big_blind()

    @property
    def give_list(self):

        return [i.current_give for i in self.init_players]

    @property
    def init_n_players(self):
        """ """
        return len(self.init_players)

    @property
    def pot_value(self):
        """ """
        if not len(self.action_list):
            return 0

        vals = [i[1].bb_amount for i in self.action_list]
        return sum(vals)

    @property
    def current_live_players(self):
        """ """

        return [i for i in self.init_players if i.is_in_round]

    @property
    def current_live_n_players(self):
        """ """

        return len([i for i in self.init_players if i.is_in_round])

    def _find_position_names(self):
        """ """

        ll = [name_categ_position(self.init_n_players, k) for k in self.position_orders]

        return [i[0] for i in ll]

    def _find_positions_categ(self):
        """ """

        ll = [name_categ_position(self.init_n_players, k) for k in self.position_orders]

        return [i[1] for i in ll]

    def init_round(self):
        """ """

        # cards
        give_list = [self.deck.give() for _ in self.init_players]

        # define position order name and categ
        self.position_orders = [i for i, _ in enumerate(self.init_players)]
        self.postion_names = self._find_position_names()
        self.positions_categ = self._find_positions_categ()

        # update players
        _ = [
            player.new_round(i, j, k, l)
            for player, i, j, k, l in zip(
                self.init_players,
                give_list,
                self.position_orders,
                self.postion_names,
                self.positions_categ,
            )
        ]

    def _update_next_to_play(self):
        """ """

        # next to play +1
        self.next_to_play += 1

        # if end of list go back 0
        if self.next_to_play == self.init_n_players:
            self.next_to_play = 0

    def _manage_end_play(self):
        """ """

        # next to play
        self._update_next_to_play()

        # if only one player this the end
        if self.current_live_n_players == 1:
            self.is_finished = 1
            self.winner = self.current_live_players[0]
            return None

        # else find if next next player is alive
        while True:
            if not self.init_players[self.next_to_play].is_in_round:
                self._update_next_to_play()
            else:
                break

    def small_blind(self):
        """ """

        # action
        sb = Action("SB")

        # add to preflop action list
        self.action_list.append((self.init_players[0], sb))

        # update player
        self.init_players[0].make_action("preflop", sb)

        # update next to play
        self._manage_end_play()

    def big_blind(self):

        # action
        bb = Action("BB")

        # add to preflop action list
        self.action_list.append((self.init_players[1], bb))

        # update player
        self.init_players[1].make_action("preflop", bb)

        # update next to play
        self._manage_end_play()

    def play(self, action):

        # check round Ok
        if self.is_finished:
            raise AttributeError("round finised")

        # player
        p = self.init_players[self.next_to_play]

        # update action list
        self.action_list.append((p, action))

        # update player
        p.make_action("preflop", action)

        self._manage_end_play()

    def end(self):
        """dispatch the money / close the round """
        pass

    @property
    def dict(self):
        return self.__dict__

    # def __repr__(self):
    #     """ """

    #     return str(self.__dict__)


class Turn:
    """ turn"""

    pass


class River:
    """la river """

    pass


class Round:
    """un round c'est preflop + (si players live) flop turn river """

    pass


class CashGame:
    """un cashgame c'est plusieurs round """

    pass


# if __name__ == "__main__":

#     # import
#     from src.game import *

#     # players
#     p0 = Player(name="ale", init_stack=100)
#     p1 = Player(name="isa", init_stack=100)
#     p2 = Player(name="elo", init_stack=100)
#     p3 = Player(name="ana", init_stack=100)

#     # round
#     deck = Deck()

#     # init preold
#     pre = Preflop([p0, p1, p2, p3], deck=deck)

#     # actions

#     # p2_fold
#     p2_fold = Action("fold")
#     pre.play(p2_fold)

#     # p3_fold
#     p3_fold = Action("fold")
#     pre.play(p3_fold)

#     # p0_call
#     p0_call = Action("call", amount_type="BB", amount_value=0.5)
#     pre.play(p0_call)

#     # p1_raise
#     p1_raise = Action("raise", amount_type="BB", amount_value=2)
#     pre.play(p1_raise)

#     # p0_call_2
#     p0_call_2 = Action("call", amount_type="BB", amount_value=2)
#     pre.play(p0_call_2)