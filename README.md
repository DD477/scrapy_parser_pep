# Парсер документации PEP

## Описание:
Парсит документацию Python Enhancement Proposal (PEP), посчитывает количество PEP в каждом статусе и сохраняет результат в папку results.
Программа выводит собранную информацию в два файла .csv:

- В первый файл c префиксом `pep_` список всех PEP: номер, название и статус;
- Второй файл c префиксом `status_summary_` содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). И в конце в графе Total — общее количество.

### Используемые технологии:
[![Python](https://img.shields.io/badge/-Python%203.10.4-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/-Scrapy%202.5.1-464646?style=flat-square)](https://scrapy.org/)

### Как запустить проект:

- Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/DD477/scrapy_parser_pep
```
```
cd scrapy_parser_pep
```

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```
```
source venv/bin/activate
```

- Обновить менеджер пакетов (pip) 

```
python3 -m pip install --upgrade pip
```


- Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

- Запустить парсер 
```
scrapy crawl pep 
```

### Автор:

- [Dmitrii Dobrodeev](https://github.com/DD477)

## Лицензия
- MIT

