"""Begin a Ghost admin user session and return a session cookie."""
import requests
import jwt


class GhostSession:

    def __init__(self, Config):
        self.admin_url = Config.ghost_admin_url
        self.api_key = Config.ghost_admin_api_key
        self.user = Config.ghost_admin_user
        self.password = Config.ghost_admin_password

    @property
    def base_url(self):
        return self.admin_url

    @property
    def payload(self):
        return {"username": self.user, "password": self.password}

    @property
    def cookie(self):
        return self.__get_session_cookie()

    def __create_session_token(self):
        """Generate valid session token."""
        id, secret = self.api_key.split(':')
        headers = {'alg': 'HS256',
                   'typ': 'JWT',
                   'kid': id}
        token = jwt.encode(self.payload,
                           bytes.fromhex(secret),
                           algorithm='HS256',
                           headers=headers)
        return token

    def __get_session_cookie(self):
        """Create a user session and ibtainer a cookie."""
        token = self.__create_session_token()
        url = f'{self.base_url}/ghost/api/v3/admin/session/'
        headers = {'Authorization': 'Ghost {}'.format(token.decode()),
                   'Origin': self.base_url}
        req = requests.post(url, json=self.payload, headers=headers)
        cookie = req.headers['Set-Cookie']
        return cookie
