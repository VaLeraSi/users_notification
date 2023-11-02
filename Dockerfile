FROM python
# Установим Poetry в контейнер
RUN pip install poetry

# хост базы данных для докера
ENV DB_URI=mongodb://0.0.0.0:27017/
# хост сайта
ENV SITE_HOST=127.0.0.1

# установка рабочей директории
WORKDIR /

# установка зависимостей
COPY pyproject.toml poetry.lock ./
# Устанавливаем зависимости через Poetry
RUN poetry config virtualenvs.create false && poetry install
# копирование проекта
COPY . .

# запуск приложения
CMD [ "python", "./main.py"]