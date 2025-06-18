"""Simulador qu\u00e2ntico simplificado.

Este m\u00f3dulo prov\u00ea uma classe :class:`QuantumSimulator` que utiliza o
modelo de :class:`~cryptoquantum.qubit.Qubit` para demonstrar, de forma
b\u00e1sica, opera\u00e7\u00f5es de encripta\u00e7\u00e3o e decripta\u00e7\u00e3o.
"""

from __future__ import annotations

from typing import Iterable

from . import pqc
from .qubit import Qubit


def _bits_from_byte(value: int) -> list[int]:
    """Converte um byte em uma lista de bits (LSB primeiro)."""
    return [(value >> i) & 1 for i in range(8)]


def _byte_from_bits(bits: Iterable[int]) -> int:
    """Converte uma sequ\u00eancia de bits em um byte."""
    result = 0
    for i, bit in enumerate(bits):
        result |= (bit & 1) << i
    return result


class QuantumSimulator:
    """Pequeno simulador para opera\u00e7\u00f5es de criptografia."""

    def encrypt(self, key: bytes, plaintext: bytes) -> bytes:
        """Encripta dados aplicando opera\u00e7\u00f5es qu\u00e2nticas simples."""
        resultado = bytearray()
        for idx, byte in enumerate(plaintext):
            chave = key[idx % pqc.KEY_SIZE]
            bits_cifrados = []
            for b, k in zip(_bits_from_byte(byte), _bits_from_byte(chave)):
                q = Qubit(alpha=1 + 0j, beta=0 + 0j)
                if b:
                    q.apply_x()
                if k:
                    q.apply_x()
                bits_cifrados.append(q.measure())
            resultado.append(_byte_from_bits(bits_cifrados))
        return bytes(resultado)

    def decrypt(self, key: bytes, ciphertext: bytes) -> bytes:
        """Decripta revertendo as opera\u00e7\u00f5es de :meth:`encrypt`."""
        return self.encrypt(key, ciphertext)

