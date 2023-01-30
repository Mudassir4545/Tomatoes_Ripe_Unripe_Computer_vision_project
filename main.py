
from flask import Flask, render_template
import sqlite3
from flask_basicauth import BasicAuth

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = '12345'

basic_auth = BasicAuth(app)
db_file = 'C:/Users/mudas/Desktop/Ripe-unripe-Database.db'

conn = sqlite3.connect(db_file)

cursor = conn.cursor()

query = 'SELECT  * FROM tomatoes'
results = cursor.execute(query).fetchall()
for row in results:
    print(row)

@app.route('/')
@basic_auth.required
def display_data():
    return render_template('table.html', results=results)

app.run(debug=True)