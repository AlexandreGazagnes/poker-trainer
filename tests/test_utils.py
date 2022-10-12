import pytest

from src.utils import *


def test_orderize():

    assert orderize("5ks") == "k5s"
