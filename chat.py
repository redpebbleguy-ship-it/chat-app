from flask import Flask, render_template_string
from flask_socketio import SocketIO, send
from flask_cors import CORS

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Chat</title>
    <style>
        body { font-family: Arial; background: #f2f2f2; }
        #chat { width: 400px; margin: 40px auto; background: white; padding: 20px; border-radius: 8px; }
        #messages { height: 300px; overflow-y: scroll; border: 1px solid #ccc; padding: 10px; }
        input { width: 80%; padding: 10px; }
        button { padding: 10px; }
    </style>
</head>
<body>
    <div id="chat">
        <h2>Public Chat</h2>
        <div id="messages"></div>
        <input id="msg" placeholder="Type message...">
        <button onclick="sendMessage()">Send</button>
    </div>

    <script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>
    <script>
        const socket = io();

        socket.on("message", msg => {
            const p = document.createElement("p");
            p.textContent = msg;
            document.getElementById("messages").appendChild(p);
        });

        function sendMessage() {
            const text = document.getElementById("msg").value;
            socket.send(text);
            document.getElementById("msg").value = "";
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html)

@socketio.on("message")
def handle_message(msg):
    send(msg, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
