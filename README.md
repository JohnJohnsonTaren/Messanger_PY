Messanger on Python3

Основная идея:

Model — работа с данными и БД.
View — интерфейс пользователя.
Controller — связывает View и Model.
Service — бизнес-логика.
Repository — слой доступа к данным.
Database Adapter — возможность менять SQLite на PostgreSQL, MySQL и т.д. без изменения бизнес-логики.

Ниже приведена рекомендуемая структура проекта.

project/

├── main.py

├── config/
│   └── settings.py

├── controllers/
│   ├── auth_controller.py
│   ├── chat_controller.py
│   └── user_controller.py

├── models/
│   ├── user.py
│   ├── message.py
│   └── room.py

├── views/
│   ├── login_view.py
│   ├── chat_view.py
│   └── main_window.py

├── services/
│   ├── auth_service.py
│   ├── chat_service.py
│   └── message_service.py

├── repositories/
│   ├── user_repository.py
│   ├── message_repository.py
│   └── room_repository.py

├── database/
│   ├── database_interface.py
│   ├── sqlite_adapter.py
│   └── postgres_adapter.py

├── network/
│   ├── client.py
│   └── server.py

└── utils/
├── logger.py
└── security.py


