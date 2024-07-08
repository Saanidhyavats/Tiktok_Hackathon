from flask import Flask, request, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
    FROM Tracks
    WHERE Country = ? AND Genre = ?
    ORDER BY Like DESC;
    """

    cursor = conn.execute(sql, (country, genre))
    results = cursor.fetchall()
    conn.close()

    df = pd.DataFrame(results, columns=['TikTokID', 'Like', 'Country', 'Genre'])

    return render_template('result.html', tables=[df.to_html(classes='data', header="true")])

if __name__ == '__main__':
    app.run(debug=True)
