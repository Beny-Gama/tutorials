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

#### Com o `taskGrup()` nos criamos um **async context manager** o que na pratica, é uma uma maneira de gerenciar vairas funções assincronas.

```py
import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)  # Simulate a network request or IO operation
    return {"id": id, "data": f"Sample data from coroutine {id}"}

async def main():
    tasks = []

    async with asyncio.TaskGroup() as tg:
        for index, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(index, sleep_time))
            tasks.append(task)

    # After the TaskGroup block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")

asyncio.run(main())
```

Vamos esplicar esse codigo:

`async with asyncio.TaskGroup() as tg:` → Precisamos usar esse `with` para dar asseso ao `as tg`. E Depois criamos o `asyncio.TaskGroup()` estanciar esse
`

`for i, sleep_time in enumerate([2, 1, 3], start=1):` → Criamos esse `for` com o `enumerate()` com a lista de `[2, 1, 3]` que vai comessar com o indice: 1 `start=1`

`task = tg.create_task(fetch_data(index, sleep_time))` → Usamos o `create_task()` como usamos anteriomente.

`tasks.append(task)` → Esse é um exemplo de tratamento de erros e possivel.

`results = [task.result() for task in tasks]` → Essa uma manera simples de ler uma lista ou json file.
Vamos reescrever sem “atalhos”:

```py
results = []

for task in tasks:
    resultado = task.result()
    results.append(resultado)
```

O que acontece em cada loop:

1. Pega uma Task
2. Chama `.result()`
3. Recupera o valor retornado pelo return da coroutine
4. Guarda esse valor em results

# Futures `set_result()`

### Temos duas situações em que o Futures pode ser utilizado:

### Imagine que você tenha uma função assíncrona e precise produzir vários resultados ao longo da sua execução. Usar `return` não funciona nesse caso, porque ele encerra a função imediatamente, impedindo que ela continue executando. Para resolver isso, usamos `set_result()`, que permite disponibilizar resultados enquanto a função ainda está em andamento. Assim, é possível obter valores específicos sem precisar esperar a função terminar completamente e sem interromper sua execução. Também podemos usar `set_result()` quando precisamos disponibilizar uma informação enquanto a função ainda não terminou sua execução.

- Podendo ser usado tanto para:

  - Múltiplos resultados na mesma função.
  - Para pegar um resultado enquanto a função ainda está em andamento.

```python
import asyncio

async def set_future_result(future, value):
    await asyncio.sleep(2)
    # Set the result of the future
    future.set_result(value)
    print(f"Set the future's result to: {value}")

async def main():
    # Create a future object
    loop = asyncio.get_running_loop()
    future = loop.create_future()

    # Schedule setting the future's result
    asyncio.create_task(
        set_future_result(future, "Future result is ready")
    )

    # Wait for the future's result
    result = await future
    print(f"Received the future's result: {result}")

asyncio.run(main())
```

vamos entender esse código:

`get_running_loop()` → Pega o event loop que já está rodando no momento.  
Ele é quem organiza e controla tudo o que acontece de forma assíncrona.

`create_future()` → Cria um `Future` vazio, como uma promessa de que um valor vai existir depois.  
Esse valor poderá ser esperado usando `await`.

`asyncio.create_task()` → Cria uma tarefa que roda **em segundo plano**, sem bloquear o resto do código. Ela agenda uma função assíncrona para começar a executar imediatamente. É usada quando você quer **disparar uma coroutine e continuar o fluxo normal** do programa.

`set_result()` → Coloca o valor final no `Future`. Isso marca o `Future` como pronto e libera quem estava esperando por ele.

# Sychronization | `.lock()`

### O `.lock()` impede que outras funções assíncronas executem o mesmo trecho de código ao mesmo tempo. Elas só conseguem entrar depois que o lock é liberado.

### Imagine que você criou uma função assíncrona, mas não quer que parte do código sejá executada ao mesmo tempo por mais de uma execução, por exemplo, por questão de segurança ou consistência dos dados. Com o `asyncio.Lock()` instanciado corretamente, o código continua rodando de forma assíncrona. Porém, quando a execução chega em `async with lock:`, apenas uma execução assíncrona por vez pode entrar nesse bloco de código. As outras execuções assíncronas ficam aguardando o lock ser liberado, sem travar o event loop. Assim que a execução sai do bloco protegido, o lock é liberado e a próxima execução pode entrar.

```py
import asyncio

# A shared variable
shared_resource = 0

# An asyncio Lock
lock = asyncio.Lock()

async def modify_shared_resource():
    global shared_resource
    async with lock:
        # Critical section starts
        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1 # Modify the shared resource
        await asyncio.sleep(1) # Simulate an IO operation
        print(f"Resource after modification: {shared_resource}")
        # Critical section ends

async def main():
    await asyncio.gather(
        *(modify_shared_resource() for _ in range(5))
    )

asyncio.run(main())
```

# Semaphore | `.Semaphore()`

### O `.Semaphore()` funciona parecido com o `.lock()` mas dessa fez permite a gente colocar **<u>QUANTAS</u>** funções (rotinas) queremos rodar ao mesmo tempo.

```py
import asyncio

async def access_resource(semaphore, resource_id):
    async with semaphore:
        # Simula o acesso a um recurso limitado
        print(f"Accessing resource {resource_id}")
        await asyncio.sleep(1)  # Simula trabalho com o recurso
        print(f"Releasing resource {resource_id}")

async def main():
    # Permite apenas 2 acessos concorrentes
    semaphore = asyncio.Semaphore(2)

    await asyncio.gather(
        *(access_resource(semaphore, i) for i in range(5))
    )

asyncio.run(main())
```

`asyncio.Semaphore()` → Nesse exemplo podemos setar <u>quantos</u> eventos quemos rodar.

# | `.Event()`

### Imagine que você tem várias funções assíncronas rodando, mas elas não podem continuar até que algo específico aconteça. Esse “algo” não é tempo (`sleep`), nem o fim de outra função, mas um **sinal**. É exatamente isso que o `asyncio.Event()` representa:

### No início, o evento está desligado (_unset_). Todas as funções que chamarem `await event.wait()` vão parar ali e ficar aguardando. Quando outra parte do código chama `event.set()`:

- O evento é ligado.
- Todas as funções bloqueadas são liberadas ao mesmo tempo.
- A execução continua normalmente.

### Diferente do `Lock`, aqui ninguém disputa um recurso. As funções apenas esperam um sinal para continuar. a execução continua normalmente.

```python
import asyncio

async def waiter(event):
    print("waiting for the event to be set")
    await event.wait()
    print("event has been set, continuing execution")

async def setter(event):
    await asyncio.sleep(2)
    event.set()
    print("event has been set!")
    # Simulate doing some work

async def main():
    event = asyncio.Event()
    await asyncio.gather(
        waiter(event),
        setter(event)
    )

asyncio.run(main())
```

`event = asyncio.Event()` →

`await event.wait()` →

`event.set()` →
