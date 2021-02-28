from django.conf import settings
from django.core.files.images import ImageFile
from django.core.files.storage import Storage

import BunnyCDNStorage


class BunnyStorage(Storage):
    def __init__(self):
        self.conn = BunnyCDNStorage.CDNConnector(
            settings.BUNNY_PASSWORD,
            settings.BUNNY_ZONENAME,
            storage_zone_region='ny'
        )

    def _open(self, name, mode='rb'):
        f = self.conn.get_file(name)

        return ImageFile(f)

    def _save(self, name, content):
        self.conn.upload_file('/media/', name, content)

        return name

    def delete(self, name):
        self.conn.remove(name)

    def exists(self, name):
        try:
            self.conn.get_file(name)
        except ValueError:
            return False

        return True

    def listdir(self, path):
        pass

    def size(self, name):
        pass

    def url(self, name):
        return f'https://inginerium.b-cdn.net/media/{name}'

