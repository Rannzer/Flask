from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 1000000
    },
    {
        'id':2,
        'title': 'Frontend Developer',
        'location': 'Delhi, India',
        'salary': 1500000
    },
    {
        'id':3,
        'title': 'Android Developer',
        'location': 'Gurgaon, India',
        'salary': 2000000
    },
    {
        'id':4,
        'title': 'Data Scientist',
        'location': 'Pune, India',
        'salary': 1000000
    }
]

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/run")
def run():
    return render_template("home.html",jobs=JOBS)

@app.route("/api/jobs")
def jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)