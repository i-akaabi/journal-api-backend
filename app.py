from flask import Flask, jsonify

app = Flask(__name__)

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
    app.run(debug=True)