
"""Módulo de demonstração de criptografia pós-quântica (PQC).

Este arquivo apresenta uma implementação extremamente simplificada apenas para
ilustrar conceitos básicos de geração de chaves, encriptação e decriptação.
Embora faça referência às recomendações do NIST para algoritmos pós-quânticos,
**não** representa uma solução real de segurança. O propósito principal é
educacional.
"""

from . import entanglement
from .simulator import QuantumSimulator

# Tamanho da chave em bytes definido pelo módulo de entrelaçamento.
KEY_SIZE = entanglement.KEY_SIZE


def generate_keypair() -> tuple[bytes, bytes]:
    """Gera um par de chaves utilizando entrelaçamento quântico.

    Este método delega a criação das chaves ao módulo :mod:`entanglement`, que
    simula a geração de duas chaves idênticas a partir de pares Bell. As chaves
    resultantes possuem tamanho :data:`KEY_SIZE` e devem ser empregadas em todas
    as operações de encriptação e decriptação.
    """
    return entanglement.generate_keypair()


def encrypt(key: bytes, plaintext: bytes) -> bytes:
    """Encripta os dados utilizando o simulador qu\u00e2ntico.

    Esta fun\u00e7\u00e3o delega a opera\u00e7\u00e3o de cifragem ao
    :class:`~cryptoquantum.simulator.QuantumSimulator`, garantindo que o
    processo recorra \u00e0 computa\u00e7\u00e3o qu\u00e2ntica representada no
    projeto.

    Args:
        key: chave de encripta\u00e7\u00e3o gerada por :func:`generate_keypair`.
        plaintext: dados a serem protegidos.

    Returns:
        bytes: resultado da cifragem.
    """
    sim = QuantumSimulator()
    return sim.encrypt(key, plaintext)


def decrypt(key: bytes, ciphertext: bytes) -> bytes:
    """Decripta os dados utilizando o simulador qu\u00e2ntico."""

    sim = QuantumSimulator()
    return sim.decrypt(key, ciphertext)
