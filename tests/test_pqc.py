import os
import sys

# Permite importar o pacote diretamente do diretório pai durante os testes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import cryptoquantum.pqc as pqc


def test_encrypt_decrypt():
    """Verifica se uma mensagem pode ser encriptada e decriptada corretamente."""
    # Gera par de chaves de demonstração
    pub, priv = pqc.generate_keypair()
    mensagem = b"teste"

    print("Mensagem antes da criptografia:", mensagem)
    print("Iniciando processo de criptografia")

    # Encripta a mensagem usando a chave "pública"
    cifrado = pqc.encrypt(pub, mensagem)

    print("Durante a criptografia: dados cifrados ->", cifrado.hex())

    # A função decripta deve retornar o texto original
    texto_plano = pqc.decrypt(priv, cifrado)
    print("Depois da criptografia: resultado decriptado ->", texto_plano)

    assert texto_plano == mensagem


def test_encrypt_invalid_key_size():
    """Certifica que chaves com tamanho incorreto geram erro."""
    key = b"k" * (pqc.KEY_SIZE - 1)
    with pytest.raises(ValueError):
        pqc.encrypt(key, b"fail")


def test_decrypt_invalid_key_size():
    """Certifica que chaves com tamanho incorreto geram erro na decriptação."""
    key = b"k" * (pqc.KEY_SIZE - 1)
    with pytest.raises(ValueError):
        pqc.decrypt(key, b"fail")
