
# api_final_yatube

## Описание

API для Yatube — это RESTful интерфейс для социальной сети Yatube, позволяющий пользователям взаимодействовать с контентом через сторонние приложения или скрипты.

## Возможности API

**Работа с постами:**

Получение списка публикаций.

Создание, обновление и удаление постов.

**Комментирование:**

Просмотр комментариев к публикациям.

Добавление, редактирование и удаление комментариев.

**Управление подписками:**

Подписка на авторов и просмотр списка подписок.

**Работа с группами:**

Получение информации о сообществах.

## Как запустить проект:

1.Клонируйте репозиторий:
```bash
git clone https://github.com/okhotnaks/api_final_yatube.git
```
```bash
cd api_final_yatube
```

2. Создайте и активируйте виртуальное окружение:
```bash
python -m venv venv
```
```bash
source venv/Scripts/acrivate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Выполните миграции:
```bash
python manage.py migrate
```

5. Запустите сервер:
```bash
python manage.py runserver
```
## Примеры запросов к API
**Создание публикации**

POST-запрос /api/v1/posts/:
```bash
{
"text": "string",
"image": "string",
"group": 0
}
```
Ответ:
```bash
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```

**Добавление комментария**

POST-запрос /api/v1/posts/{post_id}/comments/:
```bash
{
  "text": "string"
}
```
Ответ:
```bash
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

**Список групп**

GET-запрос /api/v1/groups/

Ответ:
```bash
[
  {
    "id": 0,
    "title": "string",
    "slug": "^-$",
    "description": "string"
  }
]
```

**Подписка**

POST-запрос /api/v1/follow/:
```bash
{
  "following": "string"
}
```
Ответ:
```bash
{
  "user": "string",
  "following": "string"
}
```
