import pygame

from src.cards import *


def test_hight_values():

    assert len(hight_values) == 13
    assert 1 not in hight_values
    assert 14 in hight_values


def test_hight_list():

    assert len(hight_list) == 13
    assert "1" not in hight_list
    assert "3" in hight_list
    assert "a" in hight_list
    assert "A" not in hight_list
    assert "j" in hight_list
    assert "v" not in hight_list


def test_hight_dict():

    assert isinstance(hight_dict, dict)
    assert len(hight_dict.values()) == 13
    assert hight_dict["2"] == 2
    assert hight_dict["k"] == 13
    assert hight_dict["a"] == 14


def test_reverse_hight_dict():

    assert isinstance(reverse_hight_dict, dict)
    assert len(reverse_hight_dict.values()) == 13
    assert reverse_hight_dict[2] == "2"
    assert reverse_hight_dict[13] == "k"
    assert reverse_hight_dict[14] == "a"


def test_colors():

    assert len(color_list) == 4


def test_card_list():

    assert len(card_list) == 52
    assert "4tr" in card_list
    assert "api" in card_list
    assert "tco" in card_list
    assert "jca" in card_list


def test_Card():
    """ """

    c = Card("Aco")

    assert c.id == "Aco"
    assert c.color == "co"
    assert c.name == "A"
    assert c.value == 14


def testHand():
    """ """

    c1 = Card("Aco")
    c2 = Card("Atr")

    hand = Hand(Card("Aco"), Card("Atr"))

    assert hand.id == ("Aco", "Atr")


def testBoard():
    """ """

    c1 = Card("Aco")
    c2 = Card("Atr")
    c3 = Card("Tca")
    c4 = Card("2ca")
    c5 = Card("Tco")

    b = Board(c1, c2, c3, c4, c5)


def test_Deck():
    """ """

    d = Deck()

    assert len(d.current_cards) == 52

    h1 = d.hand()
    h2 = d.hand()
    b = d.board()
