"""Módulo de demonstração de criptografia pós-quântica (PQC).

Este arquivo apresenta uma implementação extremamente simplificada apenas para
ilustrar conceitos básicos de geração de chaves, encriptação e decriptação.
Embora faça referência às recomendações do NIST para algoritmos pós-quânticos,
**não** representa uma solução real de segurança. O propósito principal é
educacional.
"""

import secrets

# Tamanho da chave em bytes. Em algoritmos reais, esse valor depende do método
# criptográfico adotado e pode ser significativamente maior.
KEY_SIZE = 32


def generate_keypair() -> tuple[bytes, bytes]:
    """Gera um par de chaves simétricas para demonstração.

    Nesta implementação simplificada, tanto a chave "pública" quanto a
    "privada" são idênticas, uma vez que usamos uma cifra simétrica. Em
    algoritmos pós-quânticos reais, as chaves pública e privada são diferentes e
    seguem formatos definidos pelo NIST para cada esquema.
    """
    key = secrets.token_bytes(KEY_SIZE)
    return key, key


def encrypt(key: bytes, plaintext: bytes) -> bytes:
    """Encripta os dados usando uma operação XOR simples.

    Args:
        key: chave de encriptação gerada por :func:`generate_keypair`.
        plaintext: dados a serem protegidos.

    Returns:
        bytes: resultado da operação de encriptação.
    """
    if len(key) != KEY_SIZE:
        raise ValueError(f"Tamanho de chave inválido: esperado {KEY_SIZE} bytes")
    return bytes(b ^ key[i % KEY_SIZE] for i, b in enumerate(plaintext))


def decrypt(key: bytes, ciphertext: bytes) -> bytes:
    """Decripta os dados revertendo a operação de :func:`encrypt`.

    Como a cifra utiliza XOR, a encriptação e a decriptação são operações
    idênticas. Mantemos funções separadas para tornar o fluxo mais didático.

    Args:
        key: mesma chave utilizada na encriptação.
        ciphertext: dados cifrados.

    Returns:
        bytes: texto plano original.
    """
    if len(key) != KEY_SIZE:
        raise ValueError(f"Tamanho de chave inválido: esperado {KEY_SIZE} bytes")
    return bytes(b ^ key[i % KEY_SIZE] for i, b in enumerate(ciphertext))
