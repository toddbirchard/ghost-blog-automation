"""Ghost admin client with active connection."""
import requests


class GhostClient:

    def __init__(self, session):
        self.session = session

    def export_blog_content(self):
        """Export all content as JSON and save locally."""
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'authority': 'hackersandslackers.app',
                   'cookie': self.session.cookie,
                   'Origin': self.session.base_url,
                   'accept-encoding': 'gzip, deflate, br'}
        req = requests.get(f"{self.session.base_url}/ghost/api/v3/admin/db/",
                           json=self.session.payload,
                           headers=headers)
        return req.json()
