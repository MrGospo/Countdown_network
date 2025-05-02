from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_folder='static')
socketio = SocketIO(app, cors_allowed_origins="*")

server_settings = {
    "theme": "light",
    "font": "Arial",
    "fontSize": 150,
    "textColor": "#000000",
    "minutes": 1,
    "seconds": 0,
    "duration": 60
}

@app.route('/')
def index():
    return send_from_directory('static', 'timer.html')

@socketio.on('connect')
def handle_connect():
    emit('init_settings', server_settings)

@socketio.on('update_styles')
def handle_update_styles(data):
    data["fontSize"] = int(data.get("fontSize", 150))
    server_settings.update(data)
    emit('apply_styles', server_settings, broadcast=True)

@socketio.on('start_timer')
def handle_start_timer(data):
    server_settings["duration"] = data.get("duration", 60)
    emit('start_timer', server_settings, broadcast=True)

@socketio.on('reset_timer')
def handle_reset_timer(data):
    server_settings.update({
        "minutes": int(data.get("minutes", 1)),
        "seconds": int(data.get("seconds", 0))
    })
    emit('reset_timer', server_settings, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
