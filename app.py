from flask import Flask, request, render_template, send_from_directory,jsonify
from functions import find_in_posts
from main.view import main_blueprint
from loader.save import save_blueprint
import logging


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"
logger_info = logging.getLogger("info")
console_handler = logging.StreamHandler()

app = Flask(__name__)

app.register_blueprint(main_blueprint, url_prefix='/')
app.register_blueprint(save_blueprint)
app.config['JSON_AS_ASCII'] = False


@app.route('/search')
# Роут поиска
def search_page():
    s = request.args['s']
    posts = find_in_posts(s)
    logger_info.addHandler(console_handler)
    logger_info.info("Поиск прошел")
    return render_template('post_list.html', list=posts, s=s)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

