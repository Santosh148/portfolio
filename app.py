from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# DB INIT
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
name = request.form.get("name")
email = request.form.get("email")
message = request.form.get("message") 
)

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)",
        (name, email, message)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "saved"})

# ADMIN PANEL
@app.route("/admin")
def admin():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts ORDER BY id DESC")
    data = cursor.fetchall()
    conn.close()
    return render_template("admin.html", data=data)
if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
