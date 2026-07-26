from dotenv import load_dotenv
import os
import googleapiclient.discovery

class YT_Client:

    def __init__(self):
        self.env_path = os.path.expanduser('~/.env_yt')
        load_dotenv(self.env_path)
        self.api_key = os.getenv('YT_API_KEY')
        self.version = 'v3'
        self.service_name = 'youtube'
        self.base_url = f'https://www.googleapis.com/youtube/{self.version}/'
        self.youtube = googleapiclient.discovery.build(self.service_name, self.version, developerKey=self.api_key)

    def get_channel(self, channel: str):
        return self.youtube.channels().list(part='statistics', forHandle=f'@{channel}').execute()
    
class Channel:

    def __init__(self, channel: str):
        client = YT_Client()
        self.channel = client.get_channel(channel=channel)
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

