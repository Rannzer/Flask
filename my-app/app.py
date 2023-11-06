from flask import Flask, jsonify, render_template
from database import load_jobs_from_db
from database import load_job_with_id

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/run")
def run():
    jobs = load_jobs_from_db()
    return render_template("index.html",jobs=jobs)

@app.route("/api/jobs")
def jobs():
    jobs = load_jobs_from_db()
    # return render_template("index.html",jobs=jobs)
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    hello = load_job_with_id(id)
    # print(hello)
    if(hello==None):
        return "Nothing Found..!"
    else:
        return render_template("index.html",jobs=hello)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)