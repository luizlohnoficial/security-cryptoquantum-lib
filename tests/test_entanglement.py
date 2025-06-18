import os
import sys

# Permite importar o pacote diretamente do diretório pai durante os testes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cryptoquantum.entanglement import generate_keypair, KEY_SIZE


def test_generate_keypair_identical():
    """Verifica se as chaves geradas via entrelaçamento são idênticas."""
    a, b = generate_keypair()
    assert a == b
    assert len(a) == KEY_SIZE
