# autocaster


### Dependências (Ubuntu):

```bash
sudo apt-get install scrot python3-tk python3-dev
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev python-tk python3-tk tk-dev
```

**PS:** Caso você instale as depedências e dê problema no Tkinter, é interessante "reinstalar" o Python.

### Instalando bibliotecas necessárias

Crie uma virtualenv e ative-a:

```
python -m venv env
source env/bin/activate
```

Instalando as bibliotecas:

```
make install
```

### Executando o script

```bash
python -m core --filename=<nome_do_arquivo>.json
```


### Formato do arquivo

```json
[
    {
        "hotkey": ["ctrl", "alt", "del"],
        "many_times": 1,
        "interval_between_hotkeys": 0,
        "sleep_time": 666
    },
    {
        "hotkey": ["alt", "f4"],
        "many_times": 1337,
        "interval_between_hotkeys": 1,
        "sleep_time": 10
    },
]
```
