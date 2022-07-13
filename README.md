# Проект парсинга pep
Парсер предназначен для сбора информации о нововведениях Python и
количестве статусов документов PEP

### Используемые технологии:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy-464646?style=flat-square)](https://scrapy.org/)

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/DD477/scrapy_parser_pep
```
```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```
```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

### Как пользоваться парсером:

Парсер выводит собранную информацию в два файла .csv:
+ В первый файл список всех PEP: номер, название и статус.
+ Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество)

Что бы запустить парсер необходимо выполнить команду

```
scrapy crawl pep 
```
Команда спарсит документацию PEP посчитает количество PEP в каждом
статусе и сохранит результат сбора информации в папку results
