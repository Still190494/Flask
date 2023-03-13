from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound


articles_app = Blueprint("articles_app", __name__)


ARTICLES = {
1: {
    "text" : "blabla1",
    "user_id" : 3
    },
2: {
    "text" : "blabla2",
    "user_id" : 2
    },
3: {
    "text" : "blabla3",
    "user_id" : 1
    },
}

@articles_app.route("/", endpoint="list")

def articles_list():
    return render_template("articles/list.html", articles=ARTICLES)


@articles_app.route("/<int:article_id>/", endpoint="details")
def article_details(article_id: int):
    try:
        article_name = ARTICLES[article_id]
        article_text = ARTICLES[article_id].get('text')
        article_user_id = ARTICLES[article_id].get('user_id')
    except KeyError:
        raise NotFound(f"Article #{article_id} doesn't exist!")
    return render_template('articles/details.html', article_id=article_id,
        article_name=article_name, article_text=article_text, article_user_id=article_user_id)