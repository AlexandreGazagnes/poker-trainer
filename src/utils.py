from src.cards import *
from itertools import *

# hights values list and dict
hight_values = list(range(2, 15))
hight_list = ["2", "3", "4", "5", "6", "7", "8", "9", "t", "j", "q", "k", "a"]
hight_dict = {i: j for i, j in zip(hight_list, hight_values)}
reverse_hight_dict = {j: i for i, j in zip(hight_list, hight_values)}


def orderize(txt):
    """transform 2as in a2s """

    if txt[1] == "x":
        return txt

    sub_txt = txt[:2]
    sup_txt = txt[2:] if len(txt) >= 2 else ""

    cc = [hight_dict[i] for i in sub_txt]
    cc = sorted(cc, reverse=True)
    cc = [reverse_hight_dict[i] for i in cc]

    return "".join(cc) + sup_txt


def make_permutations(txt):
    """
    TODO TEST + DOCSTRING
    """

    n = txt[0]
    perms = list(permutations(color_list, 2))
    perms = [(str(n) + i, str(n) + j) for i, j in perms]
    return perms


def flatten(arg):
    """just flatten a nested list  """

    if not isinstance(arg, list):  # if not list
        return [arg]
    return [x for sub in arg for x in flatten(sub)]  # recurse and collect