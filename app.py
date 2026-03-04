from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)

def read_csv():
    movies = []
    # Make sure the filename matches your actual CSV file!
    with open('tamil_movies_final.csv', mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies.append(row)
    return movies

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/movies')
def get_movies():
    return jsonify(read_csv())

if __name__ == '__main__':
    app.run(debug=True)