from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    entries = {
        "invalid_message": None,
        "invalid_key": "invalid_key",
        "valid_message": "valid_message",
        "valid_key": 1
    }

    with pytest.raises(TypeError):
        """Falha com key invalida"""
        encrypt_message(entries["valid_message"], entries["invalid_key"])

    with pytest.raises(TypeError):
        """Falha com mensagem"""
        encrypt_message(entries["invalid_message"], entries["valid_key"])

    """se a key for maior que a quantidade de caráteres, inverte a string"""
    assert encrypt_message("teste", 7) == "teste"[::-1]

    """Testa o caso de sucesso"""
    assert encrypt_message("teste", 2) == "ets_et"
