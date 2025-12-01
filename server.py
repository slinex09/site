from flask import Flask, render_template
app = Flask(__name__)
from movies import movies
from facts import facts
from glossary import glossary
banner_images = [
    "/static/banner3.jpg",
    "/static/banner1.jpg",
    "/static/banner2.jpg",
]
nav = [
    { "title": "Главная", "URL": "/" },
    { "title": "Сюжет", "URL": "/plot" },
    { "title": "Персонажи", "URL": "/character" },
    { "title": "Интересные факты", "URL": "/facts" },
    { "title": "Об авторе", "URL": "/about" },
    { "title": "Глоссарий", "URL": "/glossary" },
]
@app.context_processor
def global_context():
    return {
        "banner_images":banner_images,
        "nav": nav,
        "movies": movies,
        "facts": facts,
        "glossary": glossary
    }
@app.route("/")
def main():
    return render_template("index.html",name="Главная",banner_title="Трилогия Человека-паука с Томом Холландом",)
@app.route("/facts")
def best_page_view():
    return render_template("facts.html",name="Интересные факты",banner_title="Интересные факты")
@app.route("/about")
def about_view():
    return render_template("about.html",name="Об авторе", banner_title="Об авторе")
@app.route("/plot")
def plot_view():
    return render_template("plot.html",name="Сюжет",banner_title="Сюжет трилогии",)
@app.route("/character")
def character_view():
    return render_template("character.html",name="Персонажи",banner_title="Персонажи")
@app.route("/glossary")
def glossary_view():
    return render_template("glossary.html",name="Глоссарий",banner_title="Глоссарий")