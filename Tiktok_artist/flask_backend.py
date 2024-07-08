from flask import Flask, request, render_template, jsonify
from db import create_artist_table, insert_artist, create_user_table, generate_random_user_data, query, counts
from db2 import create_inf_table,insert_inf
from visualization import plot,plot2
import json, plotly
import sqlite3
import pandas as pd
import numpy as np

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tiktok_hackathon', methods=['GET', 'POST'])
def submit_frequency():
    frequency = request.form['frequency']
    track_id = request.form['track_id']
    country = request.form['programmmingLang']
    if frequency == "":
        frequency = None
    if country == "":
        country = None
    records, c = query(track_id, frequency, country)
    vals = counts(records, frequency, c)
    if frequency is None:
        fig = plot2(vals)
    else:
        fig = plot(vals, frequency)
    fig.write_html("./templates/output.html")
    return render_template('output.html')

@app.route('/potential_influencer_collaborator')
def potential_influencer_collaborator():
    return render_template('potential_influencer_collaborator.html')

@app.route('/get_data', methods=['POST'])
def get_data():
    country = request.form['country']
    genre = request.form['genre']

    conn = sqlite3.connect('inf.db')

    sql = """
    SELECT *
    FROM ARTIST
    WHERE Country = ? AND Genre = ?
    ORDER BY Like DESC;
    """

    cursor = conn.execute(sql, (country, genre))
    results = cursor.fetchall()
    conn.close()

    df = pd.DataFrame(results, columns=['TikTokID', 'Like', 'Country', 'Genre'])
    table_html = df.to_html(classes='data', header="true", index=False)

    return render_template('result.html', table_html=table_html)

if __name__ == '__main__':
    create_artist_table()
    insert_artist()
    create_user_table()
    generate_random_user_data()
    create_inf_table()
    insert_inf()
    app.run(debug=True)
