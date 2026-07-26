import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import *

channel = 'chessbrah'
view_count = get_channel_view_count(channel=channel)

insert_view_count(channel='chessbrah', view_count=view_count)