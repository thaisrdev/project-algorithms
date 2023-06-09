from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():

    # Se key for par:
    # divide message no índice key, inverte a posição das partes, inverte os
    # caracteres de cada parte, e retorna a união das partes novamente com "_"
    # entre elas
    result = encrypt_message("Python", 2)
    assert result == "noht_yP"

    # Se key for ímpar:
    # divide message no índice key, inverte os caracteres de cada parte, e
    # retorna a união das partes novamente com "_" entre elas
    result = encrypt_message("Hello World", 3)
    assert result == "leH_dlroW ol"

    # Se key não for um índice positivo válido de message, retorna
    # a string message invertida
    result = encrypt_message("oi", 10)
    assert result == "io"

    # Se key e message não possuírem os tipos corretos
    # uma exceção deve ser lançada
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(0, 0)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("string", "number")
