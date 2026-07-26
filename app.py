from flask import Flask, render_template
from youtube import Channel

app = Flask(__name__, template_folder='templates')
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def home():
    # Renders the HTML template
    channel = Channel('chessbrah')
    return render_template('index.html', channel=channel)

app.run(host='0.0.0.0', port=5000, debug=True)
