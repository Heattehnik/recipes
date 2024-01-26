# Тестовое задание на позицию Python-разработчик
## Django приложение для составления списка покупок

Приложение реализовано на основе Django и служит для сохранения и отображения списка покупок,
хранит информацию в базе данных postgres.
Приложение упаковано с помощью Docker Compose и может быть без труда развернуто на удаленном сервере.

Перед запуском приложения необходимо в корне проекта создать файл .env с необходимыми переменными окружения. В качестве
примера можете воспользоваться файлом .env_example.

После запуска по адресу http://0.0.0.0:8000/ будет доступна главная страница, на которой можно добавлять, редактировать 
и удалять покупки.

Используемые в проекте технологии:

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=green)
![](https://img.shields.io/badge/Framework-Django-informational?style=flat&logo=django&logoColor=white&color=green)
![](https://img.shields.io/badge/Database-postgreSQL-informational?style=flat&logo=postgresql&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=green)

### Настройка

Убедитесь, что у вас установлены Docker и Docker Compose.

1. Перейдите в каталог с проектом:
2. Создайте файл `.env` с необходимыми переменными окружения.

### Структура Файлов

- `./config`: содержаться основные настройки проекта.
- `./shoppinglist`: содержится приложение.
- `docker-compose.yml`: Файл конфигурации для Docker Compose.
- `.env`: Переменные окружения, необходимые для работы приложения.
- `requirements.txt`: Необходимые для работы зависимости

### Запуск проекта

1. Выполните `sudo docker-compose build` для сборки образов
2. Выполните `sudo docker-compose up -d`, чтобы запустить сервисы.


### Использование

После запуска пользователю по адресу http://0.0.0.0:8000/ будет доступно приложение.

