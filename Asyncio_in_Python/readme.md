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

## async → await (simples)

#### Quando executamos uma função que possui `async`, quando rodar o programa, ao se deparar com um `await`, libera o fluxo para que a próxima função agendada possa ser executada.

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

##

####

```python

```
