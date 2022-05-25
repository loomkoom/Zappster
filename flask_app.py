import secrets
import sqlite3
import string
import os.path

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


def generate_uid(db_id):
    alphabet = string.ascii_lowercase + string.digits
    return f"{db_id}-" + ''.join(secrets.choice(alphabet) for _ in range(4))


def dict_factory(cursor, row):
    dic = dict()
    for idx, col in enumerate(cursor.description):
        dic[col[0]] = row[idx]
    return dic


def db_connect():
    connection = sqlite3.connect('database.db')
    connection.row_factory = dict_factory
    cursor = connection.cursor()
    return cursor, connection


@app.route('/')
def home():
    print(os.getcwd())
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("base.html")


@app.route('/cards')
def list_cards():
    cur, conn = db_connect()
    cards = cur.execute('SELECT * FROM card;').fetchall()
    conn.close()
    return render_template("cards.html", cards=cards)


@app.route('/wish/<card_id>')
def wish_form(card_id):
    cur, conn = db_connect()
    card = cur.execute(f'SELECT * FROM card WHERE cardid={card_id};').fetchall()
    conn.close()
    return render_template("send_wish.html", card=card[0])


@app.route('/wish_insert', methods=['POST'])
def wish_insert():
    sender = request.form.get("sender")
    message = request.form.get("message")
    card_id = request.form.get("card_id")

    cur, conn = db_connect()

    max_id = cur.execute('select MAX(wishid) as wishid from wish;').fetchone()['wishid']
    if max_id is None:
        db_id = 1
    else:
        db_id = max_id + 1
    uid = generate_uid(db_id)

    card = cur.execute('SELECT * FROM card WHERE cardid' + '=' + str(card_id) + ';').fetchone()
    conn.execute(
        f"INSERT INTO wish (uid, sender, message, cardid) VALUES (\'{uid}\', \'{sender}\', \'{message}\', {card_id})")
    conn.commit()
    conn.close()
    return render_template("confirm_wish.html", card=card)


@app.route('/get_wish')
def get_wish():
    return render_template("get_wish.html")


@app.route('/show_wish', methods=['POST'])
def result_wish():
    uid = request.form.get("uuid")
    cur, conn = db_connect()
    personal_card = cur.execute(f"SELECT * FROM wish WHERE uid=\'{uid}\';").fetchone()
    conn.close()
    return render_template("show_wish.html", card=personal_card)


# extra route for our API to request the personal message
# use the http get method in the web request
@app.route('/api/get_wish', methods=['GET'])
def get_personal_wish():
    # the function has one parameter, the unique code
    # get the value of this parameter
    code = request.args.get('code')

    # connect and open the database file database.db
    cur, conn = db_connect()
    # read the associated personal wish, you will need an extra integer field code in your wish table!
    wish = cur.execute(f"SELECT * FROM wish WHERE code={code}").fetchall()
    conn.close()
    # there's only one wish because the code is unique
    response = jsonify(wish[0])

    # allow cross-domain Ajax requests, more info in later years
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response