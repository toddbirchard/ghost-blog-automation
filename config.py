from os import environ


class Config:
    ghost_admin_api_key = environ.get('GHOST_ADMIN_API_KEY')
    ghost_admin_url = environ.get('GHOST_ADMIN_URL')
    ghost_admin_user = environ.get('GHOST_ADMIN_USER')
    ghost_admin_password = environ.get('GHOST_ADMIN_PASSWORD')
