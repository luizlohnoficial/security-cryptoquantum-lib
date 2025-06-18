# security-cryptoquantum-lib

Este repositório serve como ponto de partida para um estudo de criptografia pós-quântica baseado nas recomendações do **NIST** (National Institute of Standards and Technology). Aqui você encontra exemplos simples e comentados que ajudam a compreender os princípios básicos desses algoritmos.

## Objetivos

- Explorar diretrizes do NIST para criptografia pós-quântica.
- Fornecer implementações de exemplo (não destinadas à produção) para fins de aprendizado.
- Manter código didático, bem comentado e testável.

## Estrutura do projeto

```
cryptoquantum/
    __init__.py       # Descrição do pacote e importação do módulo pqc
    pqc.py            # Implementação de demonstração
    qubit.py          # Classe Qubit conceitual

tests/
    test_pqc.py       # Testes unitários
```

## Exemplos de uso

Um exemplo rápido de como utilizar o módulo `pqc`:

```python
from cryptoquantum import pqc

# Gera chaves para a sessão
public_key, private_key = pqc.generate_keypair()

mensagem = b"hello quantum"

# Encripta e decripta utilizando a chave gerada
cifrado = pqc.encrypt(public_key, mensagem)
texto_plano = pqc.decrypt(private_key, cifrado)

print(texto_plano.decode())  # imprime: hello quantum
```

Também podemos instanciar a classe `Qubit` para demonstrar estados
quânticos conceituais:

```python
from cryptoquantum.qubit import Qubit

q = Qubit()
q.apply_hadamard()     # cria superposição
resultado = q.measure()  # colapsa para 0 ou 1
print(resultado)
```

Lembre-se de que essa implementação é apenas educativa e não deve ser usada em produção. Consulte as publicações do NIST para diretrizes oficiais e algoritmos recomendados.

## Referências úteis

- [NIST - Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [NISTIR 8316 - Considerations for Migration to Post-Quantum Cryptographic Algorithms](https://doi.org/10.6028/NIST.IR.8316)

Contribuições são bem-vindas!
