# Como Programar em Python

- [ ] Declaração de variavel inputs e Tipagens

<img src="img/Screenshot 2026-01-01 at 8.07.00 PM.png" />

- [ ] Operadores matematica

<img src="img/Screenshot 2026-01-01 at 8.12.10 PM.png" />

| Operador Matemático | Símbolo |
| ------------------- | ------- |
| Addition            | `+`     |
| Subtraction         | `-`     |
| Multiplication      | `*`     |
| Exponentiation      | `**`    |
| Division            | `/`     |
| Floor division      | `//`    |
| Remainder (modulus) | `%`     |

- [ ] Operadores logicos e indentação

<img src="img/Screenshot 2026-01-01 at 8.13.53 PM.png" />

| Categoria         | Operador | Descrição                                              |
| ----------------- | -------- | ------------------------------------------------------ |
| Controle de fluxo | `if`     | Executa um bloco se a condição for verdadeira          |
| Controle de fluxo | `elif`   | Testa outra condição se a anterior for falsa           |
| Controle de fluxo | `else`   | Executa se todas as condições anteriores forem falsas  |
| Comparação        | `==`     | Igual a                                                |
| Comparação        | `!=`     | Diferente de                                           |
| Comparação        | `<`      | Menor que                                              |
| Comparação        | `>`      | Maior que                                              |
| Comparação        | `<=`     | Menor ou igual a                                       |
| Comparação        | `>=`     | Maior ou igual a                                       |
| Lógico            | `and`    | Retorna True se ambas as condições forem verdadeiras   |
| Lógico            | `or`     | Retorna True se pelo menos uma condição for verdadeira |
| Lógico            | `not`    | Inverte o valor lógico                                 |
| Booleano          | `True`   | Valor verdadeiro                                       |
| Booleano          | `False`  | Valor falso                                            |
| Identidade        | `is`     | Verifica se dois objetos são o mesmo                   |
| Associação        | `in`     | Verifica se um valor está dentro de outro              |

- [ ] Listas, Tuplas, Dicionários

<img src="img/Screenshot 2026-01-01 at 8.15.50 PM.png" />

https://www.youtube.com/watch?v=0zYuLLIzPIQ

```python
# Lista é uma coleção ordenada e mutável. Permite membros duplicados.)
lista = ["carro", True, 2, 3.5]
print(lista)
print(type(lista))
print([listall])
print("-"*30)

# Tupla é uma coleção ordenada e imutável. Permite membros duplicados.
tupla = ("carro", True, 2, 3.5)
print(tupla)
print(type(tupla))
print(tupla [3])
print("-"*30)

# O dicionário é uma coleção ordenada e mutável. Nenhum membro duplicado.
dicionario = {"nome": "carro", "logica": True, "numero": 2, "outroNumero": 3.5}
print(dicionario)
print(type(dicionario))
print(dicionario["logica"])
print("_"*30)

# Set é uma coleção não ordenada e não indexada. Nenhum membro duplicado.
conjunto = {"carro", True, 2, 3.5}
print(conjunto)
print(type(conjunto))
print(conjunto[1])
```

- [ ] Laços de Repetição
      <img src="img/Screenshot 2026-01-01 at 8.14.53 PM.png" />

https://www.youtube.com/watch?v=o-1ciQ_I8-4

## Como usar o `while`

```py
i = 1

while i ‹ 10:
    print（i）
    i += 1

print("terminou")
```

## Como usar o `for`

### como usar o `for` em uma lista:

```py
criancas = ["Manu", "Vini", "Selina"]
for item in criancas:
    print (item)
```

Nesse caso ele vai printar cada item na lista

### como usar o `for` em uma string:

```py
canal = "Refatorando"

for letra in canal:
    print(letra)
```

Nesse caso ele vai printar cada letra em um string.

### Como usar o `for` com o `range`:

```py
for i in range(20):
    print(i)
```

Nesse caso, os numeros printados são 0 ao 19

#### podemos usar o `renge` com as sequintes condicionais:

qando de declara duas variavis vc limida o intervalo de numero. dessa maniera: `range(inicio,final)`

```py
for i in range(6,20):
    print(i)
```

Nesse caso, os numeros printados são: 5 a 19

#### podemos dizer qual o intervalo em que nos colocamos esses numeros:

se colocar um numero no terceira virgula: `renge(inicio,final,intervalo)` podemos dizer de quanto em qunato os numeros seram printados:

```py
for i in range(6,20,2):
    print(i)
```

Nesse caso, os numeros printados são: 5 a 19, mas pulando de 1 em 1:

Ex: 5, 7, 9, 11, 13, 15, 17, 19

### Como usar o `for` com o `renge` e `len`:

Baseado no tamanho da nossa lista o `for` e vai nos entregar o `index` dessa lista.

```py
criancas = ["Manu", "Vini", "Selina"]
for index in range(len(criancas):
    print(index)
```

Nesse caso, os numeros printados são: 0 a 2,

<br/>

Podemos combinar isso com o `index` na nossa declaracão de dados:

```py
Criancas = ["Manu", "Vini", "Selina"]
for index in range(len(criancas):
    print(criancas[index], index)
```

Nesse caso, os numeros printados são. Ex:

```cmd
Manu 0
Vini 1
Selina 2
```

<br/>

### Como usar o `for` com o `enumerate`:

O `enumerate` conseque entretar tando o `index` quanto o `valor` ao mesmo tempo de uma lista.

```py
characters = ["Krillin", "Goku", "Vegeta", "Gohan", "Piccolo"]

print(enumerate(characters))
```

```cmd
[(O, 'Krillin'), (1, 'Goku'), (2, 'Vegeta'), (3, 'Gohan'), (4, 'Piccolo')]
```

o `enumerate` combinado com `for` redus a complexidade do cogido:

```py
for index, character in enumerate(characters):
    print(index, character)
```

```cmd
0 Krillin
1 Goku
2 Vegeta
3 Gohan
4 Piccolo
```

`obs: É melhor usar o enumerate puro, porque reduz a complexidade.`

---

### Como usar o `for` com o `if`:

podemos usar `if` dentro de um `for` para analizar determinado para analizar varios dados.

```py
criancas = ["Manu", "Vini", "Selina"]
for index in range(len(criancas)):
    if index == 0:
        print(f'primenira linha: {criancas[index]}')
    else:
```

Nesse caso gostaria de saber qual crinça está em primerio lugar.

### Loops Aninhados: `for` dentro de `for`

Um loops aninhados exitem por exemlo, em casos de matrixes, ou quando tempos listas dentro de outras lista.

```py
matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]
```

```py
for linha in matrix_numeros:
    print(linha)
```

Nesse caso o que foi alinhado foi a pior cosa de verdade

```py
for linha in matrix_numeros:
    for clona in linha
        print(coluna)
```

Dessa meneira pegar cada elento de uma lista dentro de outra lista no python.

    Obs: Um loops aninhados não é recomendado para evidar algritmos muito lentos: Big(O) Notation.

### `for` sem indentação:

```py
for i in range(3): print(i)
```

```py
for index, character in enumerate(characters)
    character_map|character].append(index)
character_map
```

#### podemos crar uma validaçao em uma linha:

- [ ] Função

<img src="img/Screenshot 2026-01-01 at 8.17.10 PM.png" />

- [ ] classes

<img src="img/Screenshot 2026-01-01 at 8.18.06 PM.png" />
