"""Operacoes simples envolvendo entrelacamento quantico.

Este modulo demonstra a geracao de chaves identicas usando um par Bell
(|00> + |11>)/sqrt(2). Todo o codigo e simplificado e serve apenas para
fins educativos. Nao representa implementacao real de protocolos de
criptografia quantica.
"""

from __future__ import annotations

import math
import secrets
from dataclasses import dataclass


@dataclass
class BellPair:
    """Representacao basica de um par de qubits entrelacados."""

    alpha: complex = 1 / math.sqrt(2)  # Amplitude para |00>
    beta: complex = 0 + 0j             # Amplitude para |01>
    gamma: complex = 0 + 0j            # Amplitude para |10>
    delta: complex = 1 / math.sqrt(2)  # Amplitude para |11>

    def measure(self) -> tuple[int, int]:
        """Mede o par Bell retornando dois bits correlacionados."""
        # Resultado 0 -> colapso para |00>, resultado 1 -> |11>
        escolha = secrets.randbelow(2)
        if escolha == 0:
            return 0, 0
        return 1, 1


def _byte_from_bits(bits: list[int]) -> int:
    """Converte 8 bits (LSB primeiro) em um byte."""
    valor = 0
    for indice, bit in enumerate(bits):
        valor |= (bit & 1) << indice
    return valor


KEY_SIZE = 32  # Tamanho padrao das chaves geradas


def generate_keypair() -> tuple[bytes, bytes]:
    """Gera duas chaves identicas medindo varios pares Bell.

    As mediacoes de cada par Bell produzem bits identicos para
    ambos os participantes. Ao acumular essas medicoes, obtemos duas
    sequencias de bits iguais, resultando em chaves simetricas.
    """

    bits_a: list[int] = []
    bits_b: list[int] = []

    for _ in range(KEY_SIZE * 8):
        par = BellPair()
        a, b = par.measure()
        bits_a.append(a)
        bits_b.append(b)

    bytes_a = bytes(
        _byte_from_bits(bits_a[i : i + 8]) for i in range(0, len(bits_a), 8)
    )
    bytes_b = bytes(
        _byte_from_bits(bits_b[i : i + 8]) for i in range(0, len(bits_b), 8)
    )

    return bytes_a, bytes_b
