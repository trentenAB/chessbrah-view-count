from youtube import Channel
from postdb import Postdb

def get_channel_view_count(channel: str):
    channel=Channel(channel=channel)
    return channel.view_count

def insert_view_count(channel: str, view_count: int):
    # env_path = os.path.expanduser('~/.env_yt')
    # load_dotenv(env_path)
    # api_key = os.getenv('DATADOG_API_KEY')
    engine = Postdb()
    command = '''INSERT INTO VIEW_COUNTS (VIEWS) VALUES (%(view_count)s);'''
    params = dict(view_count=view_count)
    with engine.get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(command, params)

def get_latest_entry(channel: str):
    '''returns the last row in the db. Columns: Views and Logged_at'''
    engine = Postdb()
    query = '''SELECT VIEWS, LOGGED_AT FROM VIEW_COUNTS ORDER BY LOGGED_AT DESC LIMIT 1;'''
    with engine.get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            row = cursor.fetchone()
            return row
