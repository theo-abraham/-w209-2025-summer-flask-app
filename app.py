from flask import Flask, render_template
app = Flask(__name__)

import pandas as pd
import os
import sqlite3

APP_FOLDER = os.path.dirname(os.path.realpath(__file__))


@app.route('/')
def w209():
    file='about9.jpg'
    return render_template('w209.html',file=file)

@app.route('/map')
def map():
    return render_template('index.html')

@app.route("/getData/<int:year>")
def getData(year):
    # Load the CSV file from the static folder, inside the current path
    revenue = pd.read_csv(os.path.join(APP_FOLDER,"static/data/1_Revenues.csv"))

    if year < 1942 or year > 2008:
        return "Error in the year range"

    filteredRevenue = revenue[revenue['Year4']==year][["Name","Year4", "Total Revenue","Population (000)"]]

    # show the post with the given id, the id is an integer
    return filteredRevenue.to_json(orient='records')


@app.route("/api")
def api():
    return {"x": 10}


@app.route("/players/count")
def db():
    con = sqlite3.connect(APP_FOLDER + "/players_20.db")
    cur = con.cursor()
    cur.execute("select count(*) from players")
    res = cur.fetchall()
    return {"count": res[0][0]}


if __name__ == '__main__':
    app.run()
