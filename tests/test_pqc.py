import os
import sys

# Permite importar o pacote diretamente do diretório pai durante os testes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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
