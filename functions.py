import json
from json import JSONDecodeError
import logging

logger_info = logging.getLogger("info")
console_handler = logging.StreamHandler()


def load_posts():
    """Функция загрузки файла json"""
    try:
        with open('posts.json') as file:
            posts = json.load(file)
        return posts
    except FileNotFoundError:
        return "Файл не открывется"
    except JSONDecodeError:
        logger_info.addHandler(console_handler)
        logger_info.error("Файл не загрузился")
        return "Файл не удается преобразовать"


def find_in_posts(s):
    """Поиск по вложенности"""
    all_posts = load_posts()
    found_posts = []
    for post in all_posts:
        if s.lower() in post['content'].lower():
            found_posts.append(post)
        else:
            continue

    return found_posts


def add_post(data, picture):
    """Запись полученного поста в файл"""
    all = load_posts()
    all.append({"content": data, "pic": picture})
    try:
        with open('posts.json', "w", encoding="utf-8") as file:
            json.dump(all, file, ensure_ascii=False, indent=4)
        return
    except FileNotFoundError:
        return "Файл не открывется"
    except JSONDecodeError:
        return "Файл не удается преобразовать"
