from flask import Blueprint, render_template, request
from functions import add_post
import logging

logger_info = logging.getLogger("info")
console_handler = logging.StreamHandler()


save_blueprint = Blueprint('save_blueprint', __name__, template_folder='template')


@save_blueprint.route("/post", methods=["GET"])
def page_post_form():
    # Форма для загрузки поста
    return render_template('post_form.html')


@save_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    # Форма загруженного успешно поста
    ALLOWED_EXTENSIONS = {'png', 'jpeg'}
    picture = request.files.get("picture")
    if picture:
        '''Проверка на успешную загрузку файла'''
        picture_name = picture.filename
        extension = picture_name.split(".")[-1]
        if extension in ALLOWED_EXTENSIONS:
            '''Проверка на поддерживаемый тип данных'''
            picture.save(f"./uploads/images/{picture_name}")
            data = request.form['content']
            picture_link = f"./uploads/images/{picture_name}"
            add_post(data, picture_link)
            return render_template('post_uploaded.html', data=data, picture_link=picture_link )
        else:
            logger_info.addHandler(console_handler)
            logger_info.info("Файл не картинка")
            return "Тип файлов не поддерживается"
    else:
        return "Ошибка загрузки"


