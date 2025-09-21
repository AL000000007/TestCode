from flask import Flask, render_template, Response
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/datetime')
def datetime_page():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('datetime.html', current_time=current_time)

@app.route('/stream')
def stream():
    def event_stream():
        while True:
            yield f"data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
            time.sleep(1)
    
    return Response(event_stream(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(debug=True, threaded=True)