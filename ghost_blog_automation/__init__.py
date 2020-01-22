from .session import GhostSession
from .client import GhostClient
import json
from os import path
from datetime import datetime as date


def create_admin_session(Config):
    """"""
    session = GhostSession(Config)
    session = session.get_session_cookie()
    return session


    export = ghost.export_blog_content(cookie)
    file = f'{path.dirname(path.dirname(path.abspath(__file__)))}/data/blog-export-{date.now().strftime("%m-%d-%Y")}.json'
    with open(file, 'w+', encoding='utf-8') as f:
        json.dump(export, f, ensure_ascii=False, indent=4)
    print(export)
