from datetime import datetime

from peewee import *

# MODEL
# Configuración de la base de datos
db = SqliteDatabase("todos.db")


class BaseModel(Model):
    class Meta:
        database = db


class TodoModel(BaseModel):
    title = CharField()
    done = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        table_name = "todos"



    # @classmethod
    # def create_todo(cls, title: str) -> "TodoModel":
    #     return cls.create(title=title)

    # def mark_as_done(self) -> None:
    #     self.done = True
    #     self.save()


# Inicialización de la base de datos
def initialize_db():
    db.connect()
    db.create_tables([TodoModel])
    db.close()
