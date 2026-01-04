# How create a venv in python (virtual anbince)

### Install venv

In the file location, go to the terminal and install:

```bash
python3 -m venv filename
```

For best practice reasons, the recommended name is `.venv`. But you can name it whatever you want.

```bash
python3 -m venv .venv
```

to be sure that we are in the virtual environment:

```bash
source .venv/bin/active
```

<br/>

# Considerations

First, you have to know if you already have `pip` and `Python` installed

### List liberys

We need to know what types of libraries we already have installed:

```bash
pip list
```

This is important because we need to now eat liberty this context has been watching

<br/>

### Install updadete pip

```bash
-m pip install --upgrade pip
```

### deactivate VENV

```bash
deactivate
```

<br/>

# requirements.txt | Liberty and Version Control | Controle de Biblotecas e Verção

#### we need to now eache libery is dowloded on the file.

Esse é o padrão mais usado no Python.

📄 requirements.txt

Ex:

```txt
requests==2.31.0
flask==3.0.0
numpy==1.26.2
```

### Listar / registrar as bibliotecas instaladas:

```bash
pip freeze > requirements.txt
```

### 🔁 Depois, em outro computador / servidor

Recriar o ambiente idêntico:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
