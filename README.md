<h1 align="center">ETL Group</h1>

## Описание
Сайт для логистической фирмы ETL Group. 
Данный сайт состоит из трёх секций. На сайте присуствует бэкенд(Django).
Есть форма отправки данных пользователей на рассмотрение.

### Используемые технологии
![HTML5](https://img.shields.io/badge/-HTML5-black?style=flat-square&logo=html5&logoColor=html)
![CSS3](https://img.shields.io/badge/-CSS3-black?style=flat-square&logo=css3&logoColor=css3)
![JavaScript](https://img.shields.io/badge/-JavaScript-black?style=flat-square&logo=javascript)
![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/-Django-black?style=flat-square&logo=django)

### Используемые плагины/библиотеки
![Particle](https://img.shields.io/badge/-PARTICLES-black?style=flat-square&logo=particles&logoColor=particles)
![InputMask](https://img.shields.io/badge/-InputMask-black?style=flat-square&logo=inputmask&logoColor=inputmask)
![JQuery](https://img.shields.io/badge/-JQuery-black?style=flat-square&logo=jquery&logoColor=jquery)
![Toastr](https://img.shields.io/badge/-Toastr-black?style=flat-square&logo=toastr&logoColor=toastr)

### Запуск проекта для Windows

1-Запустить проект в PyCharm

2 - Создать виртуальное окружение (venv). IDE предложит сама. 
```
python -m venv ./venv
```
3 - Активировать (venv)
```
venv\Scripts\activate.bat
```
4 - Установить все зависимости и плагины из requirements.txt
```
pip install -r requirements.txt
```
5 - Создать .env файл
```
copy example.env .env
```
6 - Сделать миграции
```
python manage.py makemigrations
```
```
python manage.py migrate
```
7 - Запустить сервер
```
python manage.py runserver
```
