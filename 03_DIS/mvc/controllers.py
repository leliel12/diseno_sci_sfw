from flask import Flask, render_template, request, redirect, url_for

from models import TodoModel


app = Flask(__name__)



# VIEWS (Rutas de Flask)
@app.route("/")
def index():
    todos = TodoModel.select().order_by(TodoModel.created_at.desc())
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()

    todo = TodoModel(title=title)
    todo.save()

    return redirect(url_for("index"))


@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    todo = TodoModel.get_by_id(todo_id)
    todo.done = True
    todo.save()

    return redirect(url_for("index"))



