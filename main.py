from flask import Flask, render_template
from models.database import Database
app = Flask(__name__)

@app.route('/')
def test():
    db = Database()
    sql = 'select * from students'
    data = db.query(sql)
    return render_template("index.html", data = data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000, threaded=True)