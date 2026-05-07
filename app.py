from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
def init_db():

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

    connection.commit()

    connection.close()

@app.route("/")
def home():
    return "Journal API läuft"

@app.route("/entries")
def get_entries():

        entries = [
            {
                "id": 1,
                "title": "Mein erster Eintrag",
                "content": "Heute habe ich Flask verstanden"
            },
            {
                "id": 2,
                "title": "Backend Lernen",
                "content": "APIs sind interessant"
            }
        ]

        return jsonify(entries)
    

if __name__ == "__main__":
    init_db()
    app.run(debug=True)