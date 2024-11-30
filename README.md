# ⚡ hydra-dvc-lightning ⚡ 

## 🔷 Подготовка
###  brew
macOs
```bash
    brew install make
    brew install gcc
```
### venv 
создаем виртуалку на версии 3.10, чтобы не было проблем с зависимостями
```bash
    python3.10 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
```
собрать MeanVector
```bash
    make MeanVector
    python3 -m build
    pip3 install --force-reinstall dist/*.whl
    python3 performance.py
```
*в Makefile флаг -undefined dynamic_lookup нужен для работы на ARM
## 🔷 Данные
Чтобы установить данные (MNIST) вызываем метод install_data:
```bash
    python3 install_data.py
```

## DVC

```bash
  dvc init
```

добавить трекинг данынх
```bash
  dvc add data/MNIST/raw
```
закоммитим
```bash
  git add data/MNIST/raw.dvc data/MNIST/.gitignore
```

```bash
    dvc add data/MNIST/raw
    git add data/MNIST/raw.dvc
```


## 🔷 Логи

```bash
    dvc add logs
    git add logs.dvc
    git commit -m "Add training logs"
    dvc push
```

## 🔒все запустить
```bash
    python3 train.py
```