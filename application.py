
import os
from random import randint


from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from flask_session import Session
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config['CORS_HEADERS'] = 'Content-Type'
Session(app)

cors = CORS(app)
socketio = SocketIO(app)


hexa = ["0", "1", "2", "3", "4", "5", "6", "7",
        "8", "9", "A", "B", "C", "D", "E", "F"]

channels_multi = []
channels = []
users = []
inicio = True
msg = {"asdf": ["hola como estas?", "bien y tu", "cuando y donde?", "bien y tu",
                "cuando y donde?", "bien y tu", "cuando y donde?", "bien y tu", "cuando y donde?"]}


def random_color():
    c = "#"
    for i in range(6):
        c += hexa[(randint(0, 1000)*randint(0, 1000) +
                   randint(0, 500)*randint(0, 500)) % len(hexa)]
    return c


@app.route("/", methods=["POST", "GET"])
def index():
    codigo = 1

    if request.method == "POST":
        channel = request.form.get("channel_name")
        if (channel not in channels):
            channels_multi.append((channel, session['user'], session['color']))
            channels.append(channel)
            msg[channel] = []
        else:
            codigo = 420
    return render_template("index.html", channels=channels_multi, codigo=codigo)


@app.route("/logout")
def logout():
    users.remove(session["user"])
    session.clear()
    return redirect(url_for("index"))


@app.route("/register", methods=["POST", "GET"])
def register():
    codigo = 1
    print(session, "/////////////SESSION")
    if 'user' in session:
        print("--------------------------------qqqqqqqqqqqqqqqqqqqqq\n-----------")
        redirect(url_for("index"))
    elif request.method == "POST":
        user = request.form.get("nickname")
        if (user not in users):
            users.append(user)
            session["user"] = user
            # session["color"] = colores[randint(0, len(colores)});-1)]
            #session["color"] = colores[i[0] % len(colores)]
            session["color"] = random_color()
            print(session, "------\n----")

            return render_template("logged.html", user=user, color=session["color"])
        else:
            codigo = 69
    return render_template("register.html", users=users, codigo=codigo)

    # if request.method == "GET":
    #    return render_template("register.html")
    # else:
    #    return redirect(url_for('index'))


@app.route("/channel/<string:channel>", methods=["GET"])
def channel_creation(channel):
    try:
        return render_template(
            "channels.html",
            channel=channel,
            msg=msg[channel],
            user=session["user"]
        )
    except:
        print("-------------------------")

        return redirect(url_for('index'))


@socketio.on('send message')
def newMessage(msg2):
    if (len(msg[msg2['channel']]) == 100):
        msg[msg2['channel']].pop(0)
    msg[msg2['channel']].append(msg2)

    print(msg2, "*************************************")
    emit(
        "new message",
        {
            "mensaje": msg2['mensaje'],
            "username": msg2['username'],
            "date": msg2['date'],
            "channel": msg2['channel'],
            "color": msg2['color']

        },
        broadcast=True
    )
