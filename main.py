import flask
import sqlite3


app = flask.Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)


conn = sqlite3.connect('rsvps.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rsvps (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               email TEXT NOT NULL
    )


               ''')
conn.commit()
conn.close()

@app.get("/")
def index():
    return flask.send_from_directory("static", "index.html")
if __name__ == "__main__":
    app.run

@app.post("/rsvps")
def add_rsvp():
    data = flask.request.get_json()
    name = data.get('name')
    email = data.get('email')

    conn = sqlite3.connest('rsvps.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO rsvps (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

    return 'Response Successful', 201

#^^^ 201 is not an error code, it is the code for a successful response recieved.

@app.get("/rsvps")
def get_rsvps():
    conn = sqlite3.connect('rsvps.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, email FROM rsvps')
    rows = cursor.fetchall()
    conn.close()

    rsvps = [{'id': row[0],
               'name': row[1], 
               'email': row[2]
              } for row in rows]
    
    return flask.jsonify(rsvps)

    

