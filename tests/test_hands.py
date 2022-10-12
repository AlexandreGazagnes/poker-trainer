import pytest

from src.hands import *


def test_pair_list():

    assert len(pair_list) == 13
    assert "22" in pair_list
    assert "33" in pair_list
    assert "jj" in pair_list
    assert "qq" in pair_list


def test_pair_dict():

    assert ("2tr", "2pi") in pair_dict["22"]
    assert ("2pi", "2co") in pair_dict["22"]
    assert ("2co", "2pi") in pair_dict["22"]
    assert ("2pi", "2tr") in pair_dict["22"]


def test_suited_list():

    # bien sorted
    assert "23s" not in suited_list

    # doit y etre
    assert "kqs" in suited_list
    assert "k3s" in suited_list
    assert "k7s" in suited_list
    assert "k2s" in suited_list

    # pas de paires
    assert "aa" not in suited_list
    assert "aas" not in suited_list

    # doit pas y etre
    assert "tk" not in suited_list
    assert "tko" not in suited_list
    assert "kto" not in suited_list
    assert "kt" not in suited_list


def test_suited_dict():

    pass


def test_offsuit_list():

    pass


def test_offsuit_dict():

    pass


def test_all_hands():

    assert len(all_hands) == 325
