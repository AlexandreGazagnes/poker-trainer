"""
About player 

    class Player        30% 

"""

from random import choice, choices
from itertools import product


class Player:
    """class Player
    encore bcp bcp de taff mais ca fonctionne
    - manque les autorisation de action
    - manque plein de choses
    """

    NAMES = [i + j + k for i, j, k in list(product("AIOU", "bdfjklmnprt", "aioue"))]

    STACKS_VAL = [5, 10, 20, 50, 75, 100, 150, 200, 400, 800]
    STACKS_PROB = [0.01, 0.015, 0.025, 0.15, 0.2, 0.2, 0.2, 0.15, 0.045, 0.005]

    GAME_STYLE = ["thight", "normal", "loose", "limper"]
    BET_STRAT = ["passive", "normal", "agressive"]

    POS_ORDER = range(0, 10)
    POS_NAME = ["SB", "BB", "UTG", "UTG+1", "UTG+2", "MP", "MP+1", "cutoff", "button"]
    POS_CAT = ["blinds", "early", "middle", "late"]

    def __init__(
        self,
        name=None,
        init_stack=None,
        game_style=None,
        bet_strat=None,
    ):

        self.current_pos_order = -1
        self.current_pos_name = -1
        self.current_pos_categ = -1

        self.current_give = None

        self.name = choice(self.NAMES) if not name else name

        rand = lambda: choices(self.STACKS_VAL, weights=self.STACKS_PROB, k=1)[0]
        self.init_stack = rand() if not init_stack else init_stack
        self.begin_round_stack = self.init_stack
        self.current_stack = self.init_stack

        self.game_style = choice(self.GAME_STYLE) if not game_style else game_style
        self.bet_strat = choice(self.BET_STRAT) if not bet_strat else bet_strat

        # self.actions_all = {"preflop": [], "flop": [], "turn": [], "river": []}
        self.current_round_actions = []

        self.is_at_table = 1
        self.is_in_round = 1
        self.round_played = 0

        self.current_bb_bet = 0
        self.total_bb_bet = 0

    def make_action(self, action):
        """ """

        # self.actions_all[categ].append(action)
        self.current_round_actions.append(action)
        self.current_stack -= action.bb_amount
        self.current_bb_bet += action.bb_amount
        self.total_bb_bet += action.bb_amount

        if action.name == "fold":
            self.is_in_round = 0
            # self.current_give = -1

    def new_round(
        self, current_give, current_pos_order, current_pos_name, current_pos_categ
    ):
        """ """

        # reset round action
        self.round_played += 1
        self.begin_round_stack = self.current_stack
        self.current_bb_bet = 0

        self.current_give = current_give
        self.current_pos_order = current_pos_order
        self.current_pos_name = current_pos_name
        self.current_pos_categ = current_pos_categ

    def win_round(self):
        pass

    def loose_round(self):
        pass

    def quit(self):
        """ """

        self.is_playing = 0

    def __repr__(self):
        """ """

        return f"Player(name:{self.name}, pos:{self.current_pos_order}/{self.current_pos_name}/{self.current_pos_categ}, stack:{self.init_stack}/{self.begin_round_stack}/{self.current_stack} ) "

    @property
    def dict(self):
        return self.__dict__
