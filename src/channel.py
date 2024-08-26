import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.title = self.get_channel_info()["items"][0]["snippet"]["title"]
        self.view_count = self.get_channel_info()["items"][0]["statistics"]["viewCount"]
        self.video_count = self.get_channel_info()["items"][0]["statistics"]["videoCount"]
        self.sub_count = self.get_channel_info()["items"][0]["statistics"]["subscriberCount"]
        self.description = self.get_channel_info()["items"][0]["snippet"]["description"]
        self.url = "https://www.youtube.com/" + self.get_channel_info()["items"][0]["snippet"][
            "customUrl"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # api_key: str = os.getenv('YT_API_KEY')
        # youtube = build('youtube', 'v3', developerKey=self.api_key)
        # channel = self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        print(json.dumps(self.get_channel_info(), indent=2, ensure_ascii=False))

    @staticmethod
    def get_service():
        """Возвращает объект для работы с YouTube API"""
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        """Сохраняет в файл значения атрибутов экземпляра Channel"""
        data = {
            "channel_id": self.__channel_id,
            "title": self.title,
            "view_count": self.view_count,
            "video_count": self.video_count,
            "sub_count": self.sub_count,
            "description": self.description,
            "url": self.url,
        }
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    @property
    def channel_id(self):
        """Геттер для атрибута channel_id"""
        return self.__channel_id

    def get_channel_info(self):
        """Возвращает json информацию о канале."""
        return self.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
