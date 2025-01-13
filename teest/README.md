Инструкции по запуску приложения:

1. **Установите Docker и Docker Compose:**
   - Если Docker и Docker Compose еще не установлены, загрузите и установите их с [официального сайта Docker](https://www.docker.com/).

2. **Склонируйте репозиторий:**
   ```bash
   git clone <URL_репозитория>
   cd gym_subscription_app
   ```

3. **Создайте и активируйте виртуальное окружение (опционально):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate   # Для Windows
   ```

4. **Установите зависимости (если не используете Docker):**
   ```bash
   pip install -r requirements.txt
   ```

5. **Запустите приложение с помощью Docker:**
   - Убедитесь, что в корневой директории проекта находится файл `docker-compose.yml`.
   - Запустите контейнеры:
     ```bash
     docker-compose up --build
     ```

6. **Примените миграции базы данных:**
   - В новом терминале, подключенном к контейнеру `web`, выполните:
     ```bash
     docker exec -it gym_web python manage.py makemigrations
     docker exec -it gym_web python manage.py migrate
     ```

7. **Создайте суперпользователя (для доступа к админке):**
   ```bash
   docker exec -it gym_web python manage.py createsuperuser
   ```

8. **Запустите приложение локально (без Docker, если нужно):**
   - Убедитесь, что PostgreSQL работает на вашем локальном хосте.
   - Примените миграции и запустите сервер разработки:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     python manage.py runserver
     ```

9. **Откройте приложение в браузере:**
   - Для локального запуска: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Для Docker: [http://localhost:8000](http://localhost:8000)

10. **Доступ к API:**
    - API доступен по пути `/api/`.
    - Используйте такие маршруты, как:
      - `/api/gyms/` для работы со спортзалами.
      - `/api/subscriptions/` для подписок.
      - `/api/trainers/` для списка тренеров.
      - `/api/training-sessions/` для списка тренировок.

11. **Доступ к авторизации:**
    - Регистрация: [http://localhost:8000/auth/register/](http://localhost:8000/auth/register/)
    - Вход: [http://localhost:8000/auth/login/](http://localhost:8000/auth/login/)
    - Выход: [http://localhost:8000/auth/logout/](http://localhost:8000/auth/logout/)