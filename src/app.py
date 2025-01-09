import os
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

DB_PATH = os.getenv("DB_PATH", "items.db")  # Позволява динамична настройка на пътя до базата

def init_db():
    if not os.path.exists(DB_PATH):
        with sqlite3.connect(DB_PATH) as conn:
            with open("sql/V1_Create_item_table.sql", "r") as f:
                conn.executescript(f.read())

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Items API!"}), 200

@app.route('/items', methods=['GET'])
def get_items():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ITEM")
        items = cursor.fetchall()
    return jsonify(items), 200

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ITEM (ID, NAME) VALUES (?, ?)", (item['id'], item['name']))
        conn.commit()
    return jsonify({"message": "Item added successfully!"}), 201

@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ITEM WHERE ID = ?", (id,))
        conn.commit()
    return jsonify({"message": "Item deleted successfully!"}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
