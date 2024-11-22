import models, controllers

if __name__ == "__main__":
    models.initialize_db()

    # Crear algunos todos de ejemplo si la base está vacía
    if models.TodoModel.select().count() == 0:
        models.TodoModel.create(title="Aprender MVC con Flask")
        models.TodoModel.create(title="Practicar Peewee ORM")
        models.TodoModel.create(title="Hacer ejercicio")

    controllers.app.run(debug=True)