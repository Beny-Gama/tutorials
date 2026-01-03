# [How to Create a Asyncio](youtube.com/watch?v=Qb9s3UiMSTA&t)

#### Uma função Assíncrona é a maneira que temos de rodar várias funções ao mesmo tempo. Sem precisar esperar uma função parar, para que a outra comese.

<img src="img/Screenshot 2026-01-03 at 10.14.19 AM.png">

A manira mais simples para que entendamos essa maneira de escrever codigo é:

```py
import asyncio

async def main():
    print ("Start of main coroutine")

asyncio.run(main())
```

`import asyncio` → Importa a biblioteca (nativa do python)

`async def` → Colocamos o `async` antes do `def`. Para dizer ao python que a nossa função é assíncroma.

`asyncio.run()` → Vai comesar o nosso evento
<br/>

# async → await (simples)

1. #### Quando executamos uma função que possui `async`, quando rodar o programa, ao se deparar com um `await`, libera o fluxo para que a próxima função agendada possa ser executada.

Em uma função normal (sem `async`), é necessário aguardar toda a execução da função para que outra possa começar.

```python

import asyncio
# Define a coroutine that simulates a time-consuming task.
async def fetch_data(delay):
    print ("1 - Fetching data...")
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep.
    print ("2 - Data fetched")
    return {"data": "Some data"}
    # Return some data.

# Define another coroutine that calls the first coroutine
async def main():
    print ("3 - Start of main coroutine")
    task = fetch_data(2)
    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    result = await task
    print (f"4 - Received result: {result}")
    print ("5 - End of main coroutine")

# Run the main coroutine
asyncio.run(main())
```

Terminal: <br/>

```bash
3 - Start of main coroutine
1 - Fetching data...
(espera 2 segundos sem bloquear)
2 - Data fetched
4 - Received result: {'data': 'Some data'}
5 - End of main coroutine
```

`async def fetch_data(delay):`
→ Declaramos uma função assíncrona (coroutine). Ela só será executada quando for aguardada (await).

`await asyncio.sleep(delay)` → Indica um ponto onde a função vai demorar.
Enquanto isso, o Python não bloqueia o programa. Ele pode executar outras tarefas assíncronas.

`task = fetch_data(2)`
→ Criamos a coroutine, mas ela ainda não está rodando de verdade.
É apenas um objeto que representa a tarefa.

`result = await task`
→ Aqui o código diz: “Espere essa tarefa terminar antes de continuar”. Enquanto espera, o event loop pode executar outras coroutines

2. Vamos tentar quebrar esse colocando o `result = await task` no final do nosso codigo. e ver o resltado:

```python
import asyncio
# Define a coroutine that simulates a time-consuming task.
async def fetch_data(delay):
    print ("1 - Fetching data...")
    await asyncio.sleep(delay) # Simulate an I/O operation with a sleep.
    print ("2 - Data fetched")
    return {"data": "Some data"}
    # Return some data.

# Define another coroutine that calls the first coroutine
async def main():
    print ("3 - Start of main coroutine")
    task = fetch_data(2)
    print ("4 - End of main coroutine")

    result = await task
    print (f"5 - Received result: {result}")

# Run the main coroutine
asyncio.run(main())
```

terminal:

```bash
3 - Start of main coroutine
4 - End of main coroutine
1 - Fetching data...
2 - Data fetched
5 - Received result: {'data': 'Some data'}
```

Veja que agora nosso código parece estar fora de ordem e não funciona como muitos esperariam.
Isso acontece porque a função assíncrona só começa a ser executada quando encontra um `await`.

Até esse momento, a coroutine apenas foi criada, mas não está rodando de fato. É como se a função ficasse em standby, aguardando ser acionada pelo `await`.

Em outras palavras:
criar uma função `async` não executa o código automaticamente.
Somente quando usamos `await` é que o Python entrega essa função para o event loop e inicia sua execução.

# async tasks | `create_task()`

1. #### Imagine que você quer que todos das as funções rodem em paralelo, sem precisar que as funções esperem. Para isso podemos usar as funçao `create_task()`:

```py
import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    # Create tasks for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

asyncio.run(main())
```

- Ao Inves de Simplimete criarmos:

  - `task1 = fetch_data(1, 2)`

- podemos usar o `asyncio.create_task`:

  - `task1 = asyncio.create_task(fetch_data(1, 2))`

2. #### Agora, imagine que você que as duas funções escutem primero, e depois, a terceira execute de maneira posterior basta escrever o mesmo codigo dessa maneira:

```py
import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    # Create tasks for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    result1 = await task1
    result2 = await task2

    task3 = asyncio.create_task(fetch_data(3, 1))
    result3 = await task3

    print(result1, result2, result3)

asyncio.run(main())

```

Agora a `task1` e `task2` vam executar primero que a `task3`.

# multi-async function | `gather()`

1. #### Imagine que vc quera rodar varias funções ao mesmo tempo, mas não queira estanicar uma por vez. Basta usar a função `gather()`:

```py
import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)  # Simulate a network request or IO operation
    # Return some data as a result
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    # Run coroutines concurrently and gather their return values
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3)
    )

    # Process the results
    for result in results:
        print(f"Received result: {result}")


# Run the main coroutine
asyncio.run(main())

```

`results = await asyncio.gather()` → criamos essa função que diz quais funções `async` vam sem colocadas entrar nela.

- Obs: por mais que ele deixe o codigo mais limpo. O `asyncio.gather()` não é muito utilizado por dois motivos principais:
  - Não consigo ter controle de qual funcão usar por cada ves.
  - Não consigo ter controle de erros.

<br/>

# `taskGrup()` Function

#### Nas mais novas verções do python podemos emcontrar esse `taskGrup()` para tratar trarar de vairas funções `async` ao mesmo tempo. Mas agora, difernete do `gather()` podemos fazer tratamento de erros. As custas de deixar o codigo mais verboso.

```py
import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)  # Simulate a network request or IO operation
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # After the TaskGroup block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())
```
