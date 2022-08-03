from flask import Blueprint, render_template, request


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='template')


@main_blueprint.route('/')
# Главная страница
def main_page():
    return render_template("index.html")

