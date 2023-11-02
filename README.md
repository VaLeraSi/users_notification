# Тестовое задание для Эйс Плэйс
Микросервис уведомлений пользователей представляет собой RestAPI сервер, предназначенный для создания записей уведомлений в документе пользователя в MongoDB,
отправки электронных писем, а также предоставления листинга уведомлений из документа пользователя. Этот микросервис позволяет эффективно управлять уведомлениями,
ограничивая их количество и обеспечивая удобный доступ к информации о них.


# Инструменты и технологии
В проекте использовались следующие инструменты и технологии:

- Python: Язык программирования, на котором написан весь микросервис.
- FastAPI: Микрофреймворк для создания RESTful API.
- MongoDB: СУБД для хранения данных уведомлений пользователей.
- SMTP: Протокол для отправки электронных писем.
- Docker: Платформа для создания, развертывания и управления контейнеризированными приложениями.
- GitHub: Платформа для совместной разработки и управления исходным кодом проекта.
- Swagger: Инструмент для документирования и тестирования API.
- Pydantic: Библиотека для проверки и валидации данных и запросов.
- asyncio: Библиотека для асинхронного программирования.
- Motor: Асинхронный драйвер для работы с MongoDB.
- SMTP_SSL: Библиотека для отправки электронных писем через SMTP с использованием SSL.

  Другие библиотеки: В проекте также использовались различные библиотеки Python для обработки HTTP-запросов, работы с электронной почтой и других задач.


# Переменные окружения
Для настройки микросервиса уведомлений используются следующие переменные окружения:

- SITE_PORT - Порт, на котором будет работать приложение. Пример значения: 8000.
- TO_EMAIL - Тестовый email, который будет использоваться в случае отсутствия пользователя. Пример значения: example@example.com.
- DB_URI - Строка для подключения к MongoDB. Пример значения: mongodb://localhost:27017/notifications.
- SMTP_HOST - Хост SMTP-сервера. Пример значения: smtp.example.com.
- SMTP_PORT - Порт SMTP-сервера. Пример значения: 587.
- SMTP_LOGIN - Логин пользователя для SMTP-сервера. Пример значения: user@example.com.
- SMTP_PASSWORD - Пароль пользователя для SMTP-сервера. Пример значения: yourpassword.
- SMTP_EMAIL - Email, с которого будут отправлены уведомления. Пример значения: notifications@example.com.
- SMTP_NAME - Имя, которое будет отображаться у получателя письма.

Эти переменные окружения могут быть установлены в файле конфигурации, например, .env.

# Запуск проекта

- Клонируйте репозиторий: `git clone https://github.com/VaLeraSi/user_notification`
- Установите Docker
- Создайте Dockerfile
- Создайте docker-compose.yml
- Запустите Docker контейнеры с помощью команды: `docker-compose up`
- Откройте веб-браузер и перейдите по адресу http://127.0.0.1:8000