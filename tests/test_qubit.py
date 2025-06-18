import os
import sys

# Permite importar o pacote diretamente do diretório pai durante os testes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cryptoquantum.qubit import Qubit


def test_hadamard_superposition():
    """Aplica Hadamard e verifica distribuição das amplitudes."""
    q = Qubit()
    q.apply_hadamard()
    # Após Hadamard no |0>, as probabilidades devem ser aproximadamente 0.5
    assert abs(abs(q.alpha)**2 - 0.5) < 1e-6
    assert abs(abs(q.beta)**2 - 0.5) < 1e-6


def test_measure_collapse():
    """Mede o qubit e garante que o estado colapsa."""
    q = Qubit()
    resultado = q.measure()
    assert resultado in (0, 1)
    if resultado == 0:
        assert q.alpha == 1 + 0j and q.beta == 0 + 0j
    else:
        assert q.alpha == 0 + 0j and q.beta == 1 + 0j
