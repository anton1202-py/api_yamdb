# api_yamdb. Командный проект.
  
### Роли участников:
**Кузнецов Антон - Team Lead**  
Зона разработки: Review/Comments  
**Пригарин Вадим - разработчик**  
Зона отвественности: Categories/Genres/Titles  
**Пиманов Даниил - разработчик**  
Зона отвественности: Auth/Users  
  
## Описание  
Задача — написать бэкенд проекта (приложение reviews)  
и API для него (приложение api) так, чтобы они полностью соответствовали документации.  
Документация — это ваше техническое задание.  
  
Установка проекта  
Чтобы развернуть проект локально, нужно:  
  
Клонировать его с репозитория.  
Установить виртуальное окружение. (python -m venv venv)  
Активировать виртуальное окружение. (. venv/scripts/activate)  
Установить зависимости (pip install -r requirements.txt)  
Сделать миграции(python manage.py migrate)  
  
## Для взаимодействия с ресурсами настроены эндпоинты:  
  
### AUTH  
  
POST http://127.0.0.1:8000/api/v1/auth/signup/ - Регистрация нового пользователя  
  
POST http://127.0.0.1:8000/api/v1/auth/token/ - Получение JWT-токена  
  
### CATEGORIES  
  
GET http://127.0.0.1:8000/api/v1/categories/ - Получение списка всех категорий  
  
POST http://127.0.0.1:8000/api/v1/categories/ - Добавление новой категории  
  
DEL http://127.0.0.1:8000/api/v1/categories/{slug}/ - Удаление категории  
  
### GENRES
  
GET http://127.0.0.1:8000/api/v1/genres/ - Получение списка всех жанров  
  
POST http://127.0.0.1:8000/api/v1/genres/ - Добавление жанра  
  
DEL http://127.0.0.1:8000/api/v1/genres/{slug}/ - Удаление жанра  
  
### TITLES  
  
GET http://127.0.0.1:8000/api/v1/titles/ - Получение списка всех произведений  
  
POST http://127.0.0.1:8000/api/v1/titles/ - Добавление произведения  
  
GET http://127.0.0.1:8000/api/v1/titles/{titles_id}/ - Получение информации о произведении  
  
PATCH http://127.0.0.1:8000/api/v1/titles/{titles_id}/ - Частичное обновление информации о произведении  
  
DEL http://127.0.0.1:8000/api/v1/titles/{titles_id}/ - Удаление произведения  
  
### REVIEWS  
  
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/ - Получение списка всех отзывов  
  
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/ - Добавление нового отзыва  
  
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/ - Получение отзыва по id  
  
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/ - Частичное обновление отзыва по id  
  
DEL http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/ - Удаление отзыва по id  
  
### COMMENTS  
  
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Получение списка всех комментариев к отзыву  
  
POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/ - Добавление комментария к отзыву  
  
GET http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ - Получение комментария к отзыву  
  
PATCH http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ - Частичное обновление комментария к отзыву  
  
DEL http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/ - Удаление комментария к отзыву  
  
### USERS  
  
GET http://127.0.0.1:8000/api/v1/users/ - Получение списка всех пользователей  
  
POST http://127.0.0.1:8000/api/v1/users/ - Добавление пользователя  
  
GET http://127.0.0.1:8000/api/v1/users/{username}/ - Получение пользователя по username  
