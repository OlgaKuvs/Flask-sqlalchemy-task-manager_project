from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    # By using the .all() method, this is actually what's known as a Cursor Object
    # To convert this Cursor Object into a standard Python list - list()
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods= ['GET','POST'])
# When a user clicks the "Add Category" button, this will use the "GET"
# method and render the 'add_category' template.
def add_category():
    # Once they submit the form, this will call the same function, but will check if the request
    # being made is a “POST“ method, which posts data to a database.
    if request.method == 'POST':
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods= ['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == 'POST':
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)