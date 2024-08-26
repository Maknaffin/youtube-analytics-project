import json
import os
from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id видео. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        self.title = self.get_video_info()["items"][0]["snippet"]["title"]
        self.view_count = self.get_video_info()["items"][0]["statistics"]["viewCount"]
        self.like_count = self.get_video_info()["items"][0]["statistics"]["likeCount"]
        self.url = self.url = "https://www.youtube.com/watch?v=" + self.video_id

    def get_video_info(self):
        """Возвращает статистику видео по его id"""
        return self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=self.video_id
                                                ).execute()

    @staticmethod
    def get_service():
        """Возвращает объект для работы с YouTube API"""
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def print_info(self) -> None:
        """Выводит в консоль данные по видео."""
        print(json.dumps(self.get_video_info(), indent=2, ensure_ascii=False))

    def __str__(self):
        return f'{self.title}'

class PLVideo:
    def __init__(self, video_id: str, playlist_id: str) -> None:
        """Экземпляр инициализируется id видео и плейлиста. Дальше все данные будут подтягиваться по API."""
        self.video_id = video_id
        self.playlist_id = playlist_id
        self.title = self.get_video_info()["items"][0]["snippet"]["title"]
        self.view_count = self.get_video_info()["items"][0]["statistics"]["viewCount"]
        self.like_count = self.get_video_info()["items"][0]["statistics"]["likeCount"]
        self.url = self.url = "https://www.youtube.com/watch?v=" + self.video_id

    def get_playlist_info(self):
        """Возвращает данные плейлиста по его id"""
        return self.get_service().playlistItems().list(playlistId=self.playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()

    def get_video_info(self):
        """Возвращает статистику видео по его id"""
        return self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                id=self.video_id
                                                ).execute()

    @staticmethod
    def get_service():
        """Возвращает объект для работы с YouTube API"""
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def print_playlist_info(self) -> None:
        """Выводит в консоль данные по плейлисту."""
        print(json.dumps(self.get_playlist_info(), indent=2, ensure_ascii=False))

    def print_video_info(self) -> None:
        """Выводит в консоль данные по плейлисту."""
        print(json.dumps(self.get_playlist_info(), indent=2, ensure_ascii=False))

    def __str__(self):
        return f'{self.title}'