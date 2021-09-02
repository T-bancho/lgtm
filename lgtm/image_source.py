import requests
from io import BytesIO

class LocalImage:
    """ファイルから画像を取得する"""

    def __init__(self, path):
        self.path = path
    
    def get_image(self):
        return open(self.__path__, 'rb')

class RemoteImage:
    """URLから画像を取得する"""

    def __init__(self, path):
        self.url = path
    
    def get_image(self):
        data = requests.get(self, url)
        # バイトデータをファイルオブジェクトに変換
        return BytesIO(data.content)