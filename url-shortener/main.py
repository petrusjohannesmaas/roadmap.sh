from flask import Flask, request, jsonify
import sqlite3
import random
import string
import datetime

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            short_code TEXT NOT NULL UNIQUE,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            access_count INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route("/shorten", methods=["POST"])
def create_short_url():
    data = request.get_json()
    if "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    short_code = generate_short_code()
    
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO urls (url, short_code, created_at, updated_at)
        VALUES (?, ?, ?, ?)
    """, (data["url"], short_code, datetime.datetime.utcnow(), datetime.datetime.utcnow()))
    conn.commit()
    conn.close()

    return jsonify({"shortCode": short_code, "url": data["url"]}), 201

@app.route("/shorten/<short_code>", methods=["GET"])
def get_original_url(short_code):
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM urls WHERE short_code = ?", (short_code,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        return jsonify({"error": "Short URL not found"}), 404

    # Update access count
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE urls SET access_count = access_count + 1 WHERE short_code = ?", (short_code,))
    conn.commit()
    conn.close()

    return jsonify({"url": result[1], "shortCode": result[2]})

@app.route("/shorten/<short_code>", methods=["PUT"])
def update_short_url(short_code):
    data = request.get_json()
    if "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE urls SET url = ?, updated_at = ? WHERE short_code = ?", (data["url"], datetime.datetime.utcnow(), short_code))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify({"shortCode": short_code, "url": data["url"]}), 200

@app.route("/shorten/<short_code>", methods=["DELETE"])
def delete_short_url(short_code):
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM urls WHERE short_code = ?", (short_code,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Short URL not found"}), 404

    return "", 204

@app.route("/shorten/<short_code>/stats", methods=["GET"])
def get_url_stats(short_code):
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM urls WHERE short_code = ?", (short_code,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify({"shortCode": result[2], "url": result[1], "accessCount": result[5]})

def run():
    app.run(debug=True)  # This ensures Flask starts correctly

if __name__ == "__main__":
    run()
