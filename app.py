from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os  # ← 追加！

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print(f"Received: {data}")
    emit('response', {'msg': f"サーバー受信: {data}"}, broadcast=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # ← Renderが指定したポート番号を使う
    socketio.run(app, host='0.0.0.0', port=port)
