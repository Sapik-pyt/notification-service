### notification-service
Стэк проекта:
- Python 3.9
- Django 4.1.3
- DRF 3.14.0
- Swagger
- Redis 4.4.0
- Flower 1.2.0
- Postgresql 15.0


**Техническое задание:** 
https://www.craft.do/s/n6OVYFVUpq0o6L](https://www.craft.do/s/n6OVYFVUpq0o6L

### В проекте реализованы следующие API-адрес
```
1) GET /api/client/ - получение списка клиентов

2) POST /api/client/ - добавление клиента

3) GET /api/client/<pk> - получение информации о клиенте

4) DELETE /api/client/<pk> - удаление клиента

5) PUT /api/client/<pk> - добавление информации о клиенте

6) GET /api/send_message/ - получения общей статистики по созданным рассылкам и количеству отправленных сообщений по ним с группировкой по статусам

2) POST /api/send_message/ - добавление рассылки

3) GET /api/send_message/<pk> - получения детальной статистики отправленных сообщений

4) DELETE /api/send_message/<pk> - удаления рассылки

5) PUT /api/send_message/<pk> - изменение информации о рассылки
```
## Установка и запуск

1. Склонировать репозиторий с Github:

````
git clone git@github.com:Sapik-pyt/notification-service.git
````
2. Перейти в директорию проекта
/notification-service
````
cd notification-service/
````
3. Создать виртуальное окружение:

````
python -3.9 -m venv venv
````

4. Активировать окружение: 

````
source \venv\Scripts\activate
````
5. Файл .env.example переименовать в .env
   Заполнить все недостающие поля
````
6. Установка зависимостей:

```
pip install -r requirements.txt
```

7. Создать и применить миграции в базу данных:
```
python manage.py makemigrations
python manage.py migrate
```
8. Запустить сервер
```
python manage.py runserver
```
***

## Установка проекта с помощью Docker

1. Склонировать репозиторий с Github
```
git clone git@github.com:Sapik-pyt/notification-service.git
```
2. Перейти в директорию проекта
3. Файл .env.example переименовать в .env и изменить данные в нем на подходящие вам 
4. Запустить контейнеры 
``` 
sudo docker-compose up -d
 ```

## Дополнительные задания, которые я выполнил
```
1) подготовить docker-compose для запуска всех сервисов проекта одной командой
2) сделать так, чтобы по адресу <i> /docs/ </i> открывалась страница со Swagger UI и в нём отображалось описание разработанного API. 
3) удаленный сервис может быть недоступен, долго отвечать на запросы или выдавать некорректные ответы. Необходимо организовать обработку ошибок и откладывание запросов при неуспехе для последующей повторной отправки. Задержки в работе внешнего сервиса никак не должны оказывать влияние на работу сервиса рассылок.
