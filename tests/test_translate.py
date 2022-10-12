import pytest

from src.translate import *


def test_translate_hands():

    assert translate_hand(["5tr", "5pi"]) == "55"
    assert translate_hand(["atr", "ktr"]) == "aks"
    assert translate_hand(["kpi", "atr"]) == "ako"


def test_make_pair_plus():

    assert make_pair_plus("aa+") == ["aa"]

    pp = make_pair_plus("77+")
    expected = ["77", "88", "99", "tt", "jj", "qq", "kk", "aa"]
    for hand in expected:
        assert hand in pp
    assert len(pp) == len(expected)


def test_make_just_plus():

    pp = make_just_plus("a9o+")
    expected = ["a9o", "ato", "ajo", "aqo", "ako", "aao"]
    for hand in expected:
        assert hand in pp
    assert len(pp) == len(expected)

    pp = make_just_plus("a9+")
    expected = ["a9", "at", "aj", "aq", "ak", "aa"]
    for hand in expected:
        assert hand in pp
    assert len(pp) == len(expected)


def test_translate_answer():
    """notamment  avec (["qq+", "aq+", "jto"]) """

    """il faudrait orderize l'outupt pour pas avoir kas mais aks """

    pass