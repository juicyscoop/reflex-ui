import reflex as rx

config = rx.Config(
    app_name="my_app",
    db_config=rx.DBConfig(
        engine="postgresql+psycopg2",
        username="your-db-username",
        password="your-db-password",
        host="localhost",
        port=5432,
        database="test",
    ),
)