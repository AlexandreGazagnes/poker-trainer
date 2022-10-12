import pandas as pd


import random

from src.translate import *
from src.game import *
from src.utils import *
from src.data_utils import *


AMOUNTS = [
    "BB-1",
    "BB-2",
    "BB-4",
    "BB-5",
    "BB-10",
    "PO-0.3",
    "PO-0.5",
    "PO-1",
    "PO-2",
    "PO-3",
    "PO-5",
    "PO-10",
    "all_in",
]


def find_from_df(df, BB, position):

    ans = df.loc[df.BB == BB, position]
    ans = ans.values[0]
    ans = ans.split(",")

    return ans


def give_answer(df, BB, position):

    answer = find_from_df(df, BB, position)
    print(answer)
    print(len(answer))

    answer = translate_answer(answer)
    # print(answer)
    # print(len(answer))

    return answer


def simulate_prefold(
    n_players=None,
    game_format="cash_game",
    stacks_poss=[20, 50, 75, 100, 150, 200, 400],
    stacks_prob=[0.05, 0.15, 0.2, 0.2, 0.2, 0.15, 0.05],
    actions=["call", "fold", "raise"],  # no check at first round
    amounts=AMOUNTS,
    game_style=["thight", "normal", "loose", "limper"],
    bet_strategy=["passive", "normal", "agressive"],
):

    # sanity checks
    assert sum(stacks_prob) == 1
    assert len(stacks_poss) == len(stacks_prob)
    assert (
        isinstance(n_players, int)
        or isinstance(n_players, list)
        or isinstance(n_players, tuple)
        or isinstance(n_players, str)
    )

    # manage game format
    if not game_format:
        game_format = random.choice(["cash_game", "tournois", "sit_n_go"])

    # manage n_players
    # if not n_players OR if not a list

    if isinstance(n_players, int):
        assert 8 >= n_players >= 2
    elif (
        isinstance(n_players, list)
        or isinstance(n_players, tuple)
        or isinstance(n_players, str)
    ):
        n_players = list(n_players)
        n_players = random.choice(n_players)
    elif not n_players:
        n_players = random.choice(list(range(2, 9)))
    else:
        raise AttributeError("n_players not good")

    # manage stacks
    # define random stacks form specific distrib
    rand = lambda i: random.choices(stacks_poss, weights=stacks_prob, k=1)[0]
    # build the dict
    players_stacks = {i: rand(i) for i in range(n_players)}

    # pick cards (WITHOUT REPLACEMENT)
    # pick up the good nb of card from the deck
    cards = pickup((n_players * 2) + 5)
    # board cards
    __board_cards = (cards.pop(), cards.pop(), cards.pop(), cards.pop(), cards.pop())
    # players cards
    __players_cards = {i: (cards.pop(), cards.pop()) for i in range(n_players)}

    # me position & cards
    # choice a random position for me
    me_position = random.choice(list(range(n_players)))
    # find the cards
    me_cards = __players_cards[me_position]

    # game style and bet strategy
    # define for all
    players_game_style = {i: random.choice(game_style) for i in range(n_players)}
    players_bet_strategy = {i: random.choice(bet_strategy) for i in range(n_players)}
    # pop me
    players_game_style.pop(me_position)
    players_bet_strategy.pop(me_position)

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

    me_name, me_categ = name_categ_position(n_players, me_position)

    return {
        "game_format": game_format,
        "n_players": n_players,
        "players_stacks": players_stacks,
        "__players_cards": __players_cards,
        "__board_cards": __board_cards,
        "me_position": me_position,
        "me_name": me_name,
        "me_categ": me_categ,
        "me_cards": me_cards,
        "me_hand": translate_hand(me_cards),
        "players_action": plays,
        "me_action": "",
        "me_playing": "",
        "_players_game_style": players_game_style,
        "_players_bet_strategy": players_bet_strategy,
    }


def make_clean_games(
    n_players=[2, 3, 4],
    n=300,
    dest="./games.csv",
):

    # build df
    L = [simulate_prefold(n_players=[2, 3, 4]) for _ in range(500)]
    df = pd.DataFrame(L)

    # apply all fold
    __all_fold = df.players_action.apply(find_all_fold)
    # clean
    df = df.loc[__all_fold == 0]

    df["players_action"] = df["players_action"].apply(BB_should_check)

    df.to_csv(dest, index=False)

    return df