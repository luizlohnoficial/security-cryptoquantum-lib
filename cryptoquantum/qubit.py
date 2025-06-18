"""Representação didática de um qubit.

Este módulo define a classe :class:`Qubit`, que modela um bit quântico de forma
extremamente simplificada. Ele serve apenas para ilustrar conceitos como
superposição e medição em um contexto educacional. Não realiza simulação
quântica real.
"""

from __future__ import annotations

import math
import secrets
from dataclasses import dataclass


@dataclass
class Qubit:
    """Modelo simples de um qubit."""

    alpha: complex = 1 + 0j
    """Amplitude do estado |0>"""

    beta: complex = 0 + 0j
    """Amplitude do estado |1>"""

    def normalize(self) -> None:
        """Normaliza o vetor de estado para que |alpha|^2 + |beta|^2 = 1."""
        norm = math.sqrt(abs(self.alpha) ** 2 + abs(self.beta) ** 2)
        if norm == 0:
            self.alpha, self.beta = 1 + 0j, 0 + 0j
        else:
            self.alpha /= norm
            self.beta /= norm

    def apply_hadamard(self) -> None:
        """Aplica a porta de Hadamard ao qubit."""
        a = (self.alpha + self.beta) / math.sqrt(2)
        b = (self.alpha - self.beta) / math.sqrt(2)
        self.alpha, self.beta = a, b
        self.normalize()

    def apply_x(self) -> None:
        """Aplica a porta Pauli-X (bit flip)."""
        self.alpha, self.beta = self.beta, self.alpha

    def measure(self) -> int:
        """Mede o qubit e colapsa o estado retornando 0 ou 1."""
        p0 = abs(self.alpha) ** 2
        if secrets.randbelow(1_000_000) / 1_000_000 < p0:
            # Colapsa para |0>
            self.alpha, self.beta = 1 + 0j, 0 + 0j
            return 0
        else:
            # Colapsa para |1>
            self.alpha, self.beta = 0 + 0j, 1 + 0j
            return 1
