import json
import sys
from datetime import datetime as date
from os import path
from loguru import logger
from .session import GhostSession
from .client import GhostClient


logger.add(sys.stderr, format="{time} {message}", level="INFO")


def init(Config):
    """Begin session with Ghost admin and perform automations."""
    session = create_admin_session(Config)
    exported_data = export_blog_data(session)
    save_blog_data_locally(exported_data)


def create_admin_session(Config):
    """Start admin session in Ghost."""
    session = GhostSession(Config)
    return session


def export_blog_data(session):
    """Save JSON of blog data."""
    client = GhostClient(session)
    exported_data = client.export_blog_content()
    return exported_data


def save_blog_data_locally(exported_data):
    """Store JSON in /data directory."""
    file = f'{path.dirname(path.dirname(path.abspath(__file__)))}/data/blog-export-{date.now().strftime("%m-%d-%Y")}.json'
    with open(file, 'w+', encoding='utf-8') as f:
        json.dump(exported_data, f, ensure_ascii=False, indent=4)
    logger.info(f'Successfully exported all blog data to {file}')
