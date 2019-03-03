from final import getData

#

from flask import Flask, render_template, request
app = Flask(__name__)
import sqlite3

def dataFromDB():
    conn = sqlite3.connect('sensorsData.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM stat_data")
       
    data = curs.fetchall()
    conn.close()
    return data

@app.route("/")
def index():
    getData()
    #getData1()
    data = dataFromDB()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
