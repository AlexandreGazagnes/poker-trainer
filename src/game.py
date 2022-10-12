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


class Round:
    """class Preflop is 30% WIP """

    PHASE = ["preflop", "flop", "turn", "river"]

    def __init__(self, players):
        """ """

        self.init_players = players

        self.position_orders = []
        self.postion_names = []
        self.positions_categ = []

        self.action_list = []

        self.deck = Deck()

        self.is_finished = 0
        self.winner = -1
        self.next_to_play = 0

        self.phase = "preflop"

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

    @property
    def hand_list(self):
        """ """
        # define board en fonction de la phase
        n_board_cards = {"preflop": 0, "flop": 3, "turn": 4, "river": 5}
        board = self.board.cards[: n_board_cards[self.phase]]

        # card and hands
        cards_list = [list(i.cards) + board for i in self.give_list]
        hand_list = [Hand(*cards) for cards in cards_list]

        return hand_list

    @property
    def best_hand(self):
        """ """

        return [i.best_comb for i in self.hand_list]

    @property
    def theorical_winner(self):
        """ """

        winners = compare_hands(self.hand_list)
        winners = [j for i, j in zip(winners, self.init_players) if i]

        return winners

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

        # board
        self.board = self.deck.board()

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
        sb = Action("SB", phase=self.phase)

        # add to preflop action list
        self.action_list.append((self.init_players[0], sb))

        # update player
        self.init_players[0].make_action(sb)

        # update next to play
        self._manage_end_play()

    def big_blind(self):

        # action
        bb = Action("BB", phase=self.phase)

        # add to preflop action list
        self.action_list.append((self.init_players[1], bb))

        # update player
        self.init_players[1].make_action(bb)

        # update next to play
        self._manage_end_play()

    def play(self, action):

        action.phase = phase = self.phase

        # check round Ok
        if self.is_finished:
            raise AttributeError("round finised")

        # player
        p = self.init_players[self.next_to_play]

        # update action list
        self.action_list.append((p, action))

        # update player
        p.make_action(action)

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


class CashGame:
    """un cashgame c'est plusieurs round """

    pass


if __name__ == "__main__":

    # import
    from src.game import *

    # players
    names = ["alex", "isa", "elo", "ana", "max", "teo"]
    init_stack = 100
    players = [Player(i, init_stack=init_stack) for i in names]

    # init preold
    self = Round(players)


#     # actions

#     # p2_fold
#     p2_fold = Action("fold")
#     self.play(p2_fold)

#     # p3_fold
#     p3_fold = Action("fold")
#     self.play(p3_fold)

#     # p0_call
#     p0_call = Action("call", amount_type="BB", amount_value=0.5)
#     self.play(p0_call)

#     # p1_raise
#     p1_raise = Action("raise", amount_type="BB", amount_value=2)
#     self.play(p1_raise)

#     # p0_call_2
#     p0_call_2 = Action("call", amount_type="BB", amount_value=2)
#     self.play(p0_call_2)