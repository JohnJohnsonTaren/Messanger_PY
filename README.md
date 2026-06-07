Messanger on Python3

Основная идея:

<br/><b>Model</b> — работа с данными и БД.
<br/><b>View</b> — интерфейс пользователя.
<br/><b>Controller</b> — связывает View и Model.
<br/><b>Service</b> — бизнес-логика.
<br/><b>Repository </b>— слой доступа к данным.
<br/><b/>Database Adapter</b>— возможность менять SQLite на PostgreSQL, MySQL и т.д. без изменения бизнес-логики.

Ниже приведена рекомендуемая структура проекта.
<br/>
project/
<br/>
├── main.py
<br/>├── config/
<br/>│   └── settings.py
<br/>├── controllers/
<br/>│   ├── auth_controller.py
<br/>│   ├── chat_controller.py
<br/>│   └── user_controller.py
<br/>├── models/
<br/>│   ├── user.py
<br/>│   ├── message.py
<br/>│   └── room.py
<br/>├── views/
<br/>│   ├── login_view.py
<br/>│   ├── chat_view.py
<br/>│   └── main_window.py
<br/>├── services/
<br/>│   ├── auth_service.py
<br/>│   ├── chat_service.py
<br/>│   └── message_service.py
<br/>├── repositories/
<br/>│   ├── user_repository.py
<br/>│   ├── message_repository.py
<br/>│   └── room_repository.py
<br/>├── database/
<br/>│   ├── database_interface.py
<br/>│   ├── sqlite_adapter.py
<br/>│   └── postgres_adapter.py
<br/>├── network/
<br/>│   ├── client.py
<br/>│   └── server.py
<br/>└── utils/
<br/>├── logger.py
<br/>└── security.py


