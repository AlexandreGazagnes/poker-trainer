"""
About Actions

new : 
    class Action        30% 

"""


from random import choice, choices
from itertools import product


class Action:
    """class Action
    10% WIP a :
        -  de BB value /PO Value... pour l'instant osef que BB value
        - manque un systme d'autorisation des coup à jouer...
        si amount pour raise
        transform flop to check au BB etc etc
        - la strategy ici ????
    """

    AMOUNT_TYPES = ["BB", "PO", "ALLIN"]

    AMOUNT_BB_VALUES = [0.5, 1, 2, 3, 5, 10, 20, 30, 50, 75, 100]
    AMOUNT_POT_VALUES = [0.25, 0.3, 0.5, 0.75, 1, 2, 3, 5, 7, 10, 15, 20, 25, 50, 75, 100]

    NAME = ["call", "fold", "raise", "check", "SB", "BB"]

    def __init__(
        self,
        name,
        amount_type=None,
        amount_value=None,
        pot_value=None,
        call_value=None,
    ):
        """ """

        self.name = name

        self.bb_amount = -1
        self.pot_amount = -1

        self.amount_type = amount_type

        self.pot_value = -1

        assert name in self.NAME
        if name == "SB":
            self.bb_amount = 0.5
            self.pot_value = 1  # en vérité c'est inf mais bon ;)

        if name == "BB":
            self.bb_amount = 1
            self.pot_value = 3  # en BB on mise en fait 3 fois le pot

        if name in ["fold", "check"]:
            self.bb_amount = 0
            self.pot_amount = 0

        if (name in ["call", "raise"]) and (amount_type == "BB"):
            self.bb_amount = amount_value

    def __repr__(self):
        """ """

        return f"Action(name:{self.name}, bb_amount:{self.bb_amount}, pot_value:{self.pot_value})"

    @property
    def dict(self):
        return self.__dict__
