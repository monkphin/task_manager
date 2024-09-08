from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    categories = Category.query.order_by(Category.category_name).all()
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category_name = request.form.get("category_name")
        print(f"Received category_name: {category_name}")  # Debugging output
        if category_name:
            category = Category(category_name=category_name)
            db.session.add(category)
            db.session.commit()
            return redirect(url_for("categories"))
        else:
            # Handle the case where category_name is None
            return redirect(url_for("add_category"))
    return render_template("add_category.html")
