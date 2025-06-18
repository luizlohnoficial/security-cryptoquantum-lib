import os
import sys

# Permite importar o pacote diretamente do diret\u00f3rio pai durante os testes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cryptoquantum.pqc import generate_keypair
from cryptoquantum.simulator import QuantumSimulator


def test_simulator_encrypt_decrypt():
    """Valida cifragem e decifragem usando o simulador qu\u00e2ntico."""
    pub, priv = generate_keypair()
    sim = QuantumSimulator()
    mensagem = b"quantum"
    cifrado = sim.encrypt(pub, mensagem)
    assert cifrado != mensagem
    assert sim.decrypt(priv, cifrado) == mensagem

