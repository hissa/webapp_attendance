from flask import Flask, render_template, request
from models.database import Database
app = Flask(__name__)

@app.route('/')
def test():
    db = Database()
    sql = 'select * from students'
    data = db.query(sql)
    return render_template("index.html", data = data)

@app.route('/input',methods=['GET'])
def input_attendance_page():
    db = Database()
    sql = 'select * from students;'
    data = db.query(sql)
    return render_template("input.html", students = data)

@app.route('/input',methods=['POST'])
def input_attendance():

    sql = 'INSERT INTO lessons(date,koma,name) VALUES(?,?,?)'
    db = Database()
    params = [
        request.form['date'],
        request.form['koma'],
        request.form['lesson-name']
    ]
    id = db.run(sql, params)

    sql_all_students = 'select * from students;'
    all_students = db.query(sql_all_students)

    form_data = dict(request.form)
    values = [
        f'({id},{student[0]},\'{"student-" + str(student[0]) in form_data.keys()}\')'
        for student in all_students   
    ]
    insert_sql = 'insert into attendances(lesson_id,student_number,is_attended) VALUES '
    insert_sql = insert_sql + ','.join(values)
    id = db.run(insert_sql)
    print(insert_sql)

    return render_template("input.html", students = [])

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000, threaded=True)