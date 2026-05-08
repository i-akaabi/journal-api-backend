from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


# Erstellt die Datenbank und Tabelle
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

    cursor.execute("""
        INSERT INTO entries (title, content)
        VALUES (?, ?)
    """, ("Test Eintrag", "SQLite funktioniert"))

    connection.commit()

    connection.close()


# Startseite der API
@app.route("/")
def home():
    return "Journal API läuft"


# Gibt alle Einträge als JSON zurück
@app.route("/entries")
def get_entries():

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM entries")

    entries = cursor.fetchall()

    connection.close()

    return jsonify(entries)

@app.route("/entries", methods=["POST"])
def create_entry():

    data = request.get_json()

    title = data["title"]

    content = data["content"]

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO entries (title, content)
        VALUES (?, ?)
    """, (title, content))

    connection.commit()

    connection.close()

    return jsonify({
    "message": "Neuer Eintrag erstellt"
})


if __name__ == "__main__":

    init_db()

    app.run(debug=True)