import requests
import jwt


class GhostSession:

    def __init__(self, Config):
        self.base_url = Config.ghost_admin_url
        self.api_key = Config.ghost_admin_api_key
        self.user = Config.ghost_admin_user
        self.password = Config.ghost_admin_password
        self.payload = {"username": self.user, "password": self.password}

    def __create_session_token(self):
        """Generate valid session token."""
        id, secret = self.api_key.split(':')
        # iat = int(date.now().timestamp())
        headers = {'alg': 'HS256',
                   'typ': 'JWT',
                   'kid': id}
        token = jwt.encode(self.payload,
                           bytes.fromhex(secret),
                           algorithm='HS256',
                           headers=headers)
        return token

    def get_session_cookie(self):
        """Create a user session and ibtainer a cookie."""
        token = self.__create_session_token()
        url = f'{self.base_url}/ghost/api/v3/admin/session/'
        headers = {'Authorization': 'Ghost {}'.format(token.decode()),
                   'Origin': self.base_url}
        r = requests.post(url, json=self.payload, headers=headers)
        return r.headers['Set-Cookie']

    def export_blog_content(self, cookie):
        """Export all content as JSON and save locally."""
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'authority': 'hackersandslackers.app',
                   'cookie': cookie,
                   'Origin': self.base_url,
                   'accept-encoding': 'gzip, deflate, br'}
        r = requests.get(f'{self.base_url}/ghost/api/v3/admin/db/',
                         json=self.payload,
                         headers=headers)
        return r.json()
