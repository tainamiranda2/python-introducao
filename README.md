

# Guia de Programação em Python - Curso

Este guia oferece uma introdução abrangente aos conceitos fundamentais de programação em Python. Aqui, você aprenderá a trabalhar com diversos tipos de dados, impressões de dados na tela, manipulação de textos, listas, condições, repetições, dicionários e estruturas de dados.

## Índice

1. [Tipos de Dados e Impressões de Dados na Tela](#tipos-de-dados-e-impressões-de-dados-na-tela)
2. [Trabalhando com Textos](#trabalhando-com-textos)
3. [Trabalhando com Listas](#trabalhando-com-listas)
4. [Trabalhando com Condições](#trabalhando-com-condições)
5. [Trabalhando com Repetições](#trabalhando-com-repetições)
6. [Trabalhando com Dicionários](#trabalhando-com-dicionarios)
7. [Trabalhando com Estruturas de Dados](#trabalhando-com-estruturas-de-dados)

## Tipos de Dados e Impressões de Dados na Tela

Em Python, você pode trabalhar com vários tipos de dados, incluindo inteiros, floats, strings e booleanos.

```python
# Inteiros
numero_inteiro = 10
print(numero_inteiro)

# Floats
numero_float = 10.5
print(numero_float)

# Strings
texto = "Olá, Mundo!"
print(texto)

# Booleanos
verdadeiro = True
falso = False
print(verdadeiro, falso)
```

## Trabalhando com Textos

Manipulação de strings é uma tarefa comum em programação. Aqui estão algumas operações básicas:

```python
# Concatenando strings
nome = "Maria"
saudacao = "Olá, " + nome + "!"
print(saudacao)

# Tamanho da string
tamanho = len(nome)
print(tamanho)

# Acessando caracteres
primeira_letra = nome[0]
print(primeira_letra)

# Fatiamento
parte_do_nome = nome[1:3]
print(parte_do_nome)

# Métodos de strings
texto_maiusculo = nome.upper()
print(texto_maiusculo)
```

## Trabalhando com Listas

Listas são usadas para armazenar múltiplos itens em uma única variável.

```python
# Criando uma lista
frutas = ["maçã", "banana", "cereja"]
print(frutas)

# Acessando elementos
primeira_fruta = frutas[0]
print(primeira_fruta)

# Adicionando elementos
frutas.append("laranja")
print(frutas)

# Removendo elementos
frutas.remove("banana")
print(frutas)

# Comprimento da lista
tamanho_lista = len(frutas)
print(tamanho_lista)
```

## Trabalhando com Condições

As declarações condicionais permitem que o programa execute diferentes blocos de código com base em determinadas condições.

```python
# Condicional if
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Condicional if-elif-else
nota = 85
if nota >= 90:
    print("Aprovado com louvor.")
elif nota >= 70:
    print("Aprovado.")
else:
    print("Reprovado.")
```

## Trabalhando com Repetições

Loops são usados para executar um bloco de código várias vezes.

```python
# Loop while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Loop for
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)

# Função range
for i in range(5):
    print(i)
```

## Trabalhando com Dicionários

Dicionários armazenam pares de chave-valor.

```python
# Criando um dicionário
aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia"
}
print(aluno)

# Acessando valores
nome = aluno["nome"]
print(nome)

# Adicionando itens
aluno["cidade"] = "São Paulo"
print(aluno)

# Removendo itens
del aluno["idade"]
print(aluno)
```

## Trabalhando com Estruturas de Dados

Estruturas de dados mais complexas permitem manipulação avançada de informações.

### Tuplas

Tuplas são semelhantes a listas, mas são imutáveis.

```python
# Criando uma tupla
ponto = (2, 3)
print(ponto)

# Acessando elementos
x = ponto[0]
y = ponto[1]
print(x, y)
```

### Conjuntos

Conjuntos são coleções não ordenadas de itens únicos.

```python
# Criando um conjunto
numeros = {1, 2, 3, 4}
print(numeros)

# Adicionando itens
numeros.add(5)
print(numeros)

# Removendo itens
numeros.remove(2)
print(numeros)
```

### Listas e Dicionários Aninhados

Você pode aninhar listas e dicionários para criar estruturas de dados mais complexas.

```python
# Lista de dicionários
alunos = [
    {"nome": "Ana", "idade": 22},
    {"nome": "Carlos", "idade": 23}
]
print(alunos)

# Dicionário com listas
curso = {
    "nome": "Informática",
    "alunos": ["João", "Maria", "Pedro"]
}
print(curso)
```

---
