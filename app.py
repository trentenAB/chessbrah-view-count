from flask import Flask, render_template
from youtube import Channel
from utils import get_latest_entry

app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def home():
    # Renders the HTML template
    channel='chessbrah'
    last_entry = get_latest_entry(channel=channel)
    view_count = f"{last_entry['views']:,}"
    timestamp = last_entry['logged_at'].strftime('%B %d, %Y @ %H:%M')
    return render_template('index.html', view_count=view_count, timestamp=timestamp)

app.run(host='0.0.0.0', port=5000, debug=True)
