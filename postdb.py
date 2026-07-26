import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import RealDictCursor

class Postdb:

    def __init__(self, host: str=None, port: int= 5432, db_name: str=None, user: str=None, password: str=None):
        load_dotenv(os.path.expanduser('~/.env_yt'))
        self.host = os.getenv('DB_HOST') if host is None else host
        self.port = os.getenv('DB_PORT') if port is None else port
        self.db_name = os.getenv('DB_NAME') if db_name is None else db_name
        self.user = os.getenv('DB_USER') if user is None else user
        self.password = os.getenv('DB_PASSWORD') if password is None else password

    def get_connection(self):
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            cursor_factory=RealDictCursor
        )

# engine = Postdb()
# engine.get_connection()