import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    message = "jubileu"
    assert encrypt_message(message, 2) == ("uelib_uj")
    assert encrypt_message(message, 7) == ("uelibuj")

    with pytest.raises(TypeError):
        encrypt_message(message, "")
