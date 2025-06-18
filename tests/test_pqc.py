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

    # Encripta a mensagem usando a chave "pública"
    cifrado = pqc.encrypt(pub, mensagem)

    # A função decripta deve retornar o texto original
    assert pqc.decrypt(priv, cifrado) == mensagem
