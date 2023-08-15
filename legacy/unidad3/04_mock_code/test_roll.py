# code/test_random.py

from unittest import mock

import requests


def roll(success):
    response = requests.get("http://localhost:5000/random")
    value = float(response.text)
    print(F"[Debug] {value}")
    return success <= value


#===============================================================================
# TEST
#===============================================================================

def test_win():
    response = mock.Mock(text="1")
    with mock.patch("requests.get", return_value=response) as mget:
        assert roll(1.)
        assert roll(.8)
        assert roll(.1)
    mget.assert_called()


def test_lose():
    response = mock.Mock(text="0")
    with mock.patch("requests.get", return_value=response) as mget:
        assert not roll(1.)
        assert not roll(.8)
        assert not roll(.1)
    mget.assert_called()
