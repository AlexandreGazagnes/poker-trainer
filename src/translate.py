from itertools import *
from src.utils import *

# hights values list and dict
hight_values = list(range(2, 15))
hight_list = ["2", "3", "4", "5", "6", "7", "8", "9", "t", "j", "q", "k", "a"]
hight_dict = {i: j for i, j in zip(hight_list, hight_values)}
reverse_hight_dict = {j: i for i, j in zip(hight_list, hight_values)}


def translate_hand(hand):
    """from a given hand return the symbolic translation
    ie  : ['5tr', '5pi'] is "55", ["atr", "ktr"] is "aks", ["atr", "kpi"] is "ako"

    """

    # pair
    if hand[0][0] == hand[1][0]:
        n = hand[0][0]
        return n + n

    # suited
    if hand[0][1:] == hand[1][1:]:
        n = hand[0][0]
        return orderize(hand[0][0] + hand[1][0] + "s")

    # offsuit
    return orderize(hand[0][0] + hand[1][0] + "o")


def make_pair_plus(txt):
    """si on donne 77+ renvoie les paires 77 est supp cad ['77', '88', '99', 'tt', 'jj', 'qq', 'kk', 'aa'] """

    # sanity check
    if (txt[0] != txt[1]) or (txt[2] != "+"):
        return "error"

    # take 1st val
    n = txt[0]

    # if a number :
    if n.isdigit():
        ll = list(range(int(n), 10)) + ["t", "j", "q", "k", "a"]
        ll = [str(i) + str(i) for i in ll]
        return ll

    # else return specific patern
    dd = {
        "a": "a",
        "k": "ka",
        "q": "qka",
        "j": "jqka",
        "t": "tjqka",
    }

    return [i + i for i in dd[n]]


def make_just_plus(txt):
    """si on donne a9+ renvoie les pairs as et 7+ est supp cad ['a9', 'at', 'aj', 'aq', 'ak' , 'aa']"""

    # sanity check
    if len(txt) == 3:
        if (txt[0] == txt[1]) or (txt[2] != "+"):
            return "error_1"
    if len(txt) == 4:
        if (txt[0] == txt[1]) or (txt[3] != "+"):
            return "error_2"

    # suited or offsuited
    spec = txt[2] if len(txt) == 4 else ""

    # take 1st val
    n = txt[1]

    # if a number :
    if n.isdigit():
        ll = list(range(int(n), 10)) + ["t", "j", "q", "k", "a"]

        ll = [txt[0] + str(i) for i in ll]

    else:
        dd = {
            "a": "a",
            "k": "ka",
            "q": "qka",
            "j": "jqka",
            "t": "tjqka",
            "x": "23456789tjqka",
        }

        ll = [txt[0] + i for i in dd[n]]

    if spec:
        return [i + spec for i in ll]
    else:
        return [i + "o" for i in ll] + [i + "s" for i in ll]


def translate_answer(ans):

    # sep plus from other "ie 22+ or ax+"
    plus = [i for i in ans if ("+" in i)]

    # sep pair plus "22+" from just plus "ax+"
    pair_plus = [i for i in plus if (i[0] == i[1])]
    just_plus = [i for i in plus if (i[0] != i[1])]

    # all not plus
    not_plus = [i for i in ans if ("+" not in i)]

    # translate plus
    pair_plus = [make_pair_plus(i) for i in pair_plus]
    just_plus = [make_just_plus(i) for i in just_plus]

    return flatten(pair_plus + just_plus + not_plus)


# def re_order_actions(dd, me_position):

#     DD = {}
#     dd[me_position] = "-1"

#     if len(dd.values()) == 2:
#         return dd
#     if len(dd.values()) == 3:
#         DD = {k: dd[k] for k in [2]}
