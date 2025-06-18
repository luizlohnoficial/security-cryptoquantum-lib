"""Biblioteca de demonstração para conceitos de criptografia pós-quântica.

Este pacote contém implementações simplificadas e comentadas que servem como
introdução aos algoritmos recomendados pelo NIST. Todo o código é educativo
apenas e **não deve** ser utilizado em cenários de produção.
"""

from . import pqc  # Reexporta módulo de funções de exemplo
from . import qubit  # Define classe Qubit ilustrativa
from . import simulator  # Simulador qu\u00e2ntico simplificado

__all__ = ["pqc", "qubit", "simulator"]
